from flask import Flask, render_template, request, redirect, url_for, session, Response, flash, jsonify
import MySQLdb.cursors
import re
from flask_mysqldb import MySQL
import mysql.connector
from mysql import connector

app = Flask(__name__)
app.secret_key = 'your secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456789'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'medico'


mysql = MySQL(app)


@app.route("/", methods=["POST", "GET"])
def login():
    return render_template('login.html')


@app.route("/register", methods=["POST", "GET"])
def resister():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'pwd' in request.form:
        name = request.form['name']
        mail = request.form['mail']
        pwd = request.form['pwd']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql = 'insert into patient (name,mail,pwd) values(%s,%s,%s)'
        values = (name, mail, pwd)
        cursor.execute(sql, values)
        mysql.connection.commit()
        print('hi')

        return jsonify({'success': 'Account not found'})
    return render_template('login.html')


@app.route("/home", methods=["POST", "GET"])
def home():
    msg = ''
    if request.method == 'POST' and 'mail' in request.form and 'pwd' in request.form:
        mail = request.form['mail']
        pwd = request.form['pwd']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'select * from patient where mail= %s and pwd =%s', (mail, pwd))
        account = cursor.fetchone()
        cursor.execute('select * from doctor')
        doctor = cursor.fetchall()

        cursor.execute('select * from queries')
        queries = cursor.fetchall()

        cursor.execute('select * from consult where patient_mail= %s', [mail])
        consult = cursor.fetchall()
        if consult:

            c = []
            for i in range(0, len(consult)):
                c.append(consult[i]['doctor_id'])
        else:
            c = []

        cursor.execute(
            "SELECT distinct a.name , a.dept, a.link, b.status , b.timing from doctor a, consult b where a.id=b.doctor_id and b.patient_mail= %s ", [mail])
        status = cursor.fetchall()
        if status:
            status = status
            len1 = len(status)
        else:
            status = 0
            len1 = 0

        if account:
            session['loggedin'] = True
            session['s_mail'] = account['mail']
            session['s_pwd'] = account['pwd']
            return render_template('index.html', doctor=doctor, len=len(doctor), patient=account, c=c, status=status, len1=len1, queries=queries, len2=len(queries))
        else:
            return render_template('login.html', msg='incorrect username/password')

    elif 's_mail' in session:
        mail = session.get('s_mail')
        pwd = session.get('s_pwd')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from consult where patient_mail= %s', [mail])
        consult = cursor.fetchall()

        c = []
        for i in range(0, len(consult)):
            c.append(consult[i]['doctor_id'])

        cursor.execute(
            "SELECT distinct a.name , a.dept, a.link, b.status , b.timing from doctor a, consult b where a.id=b.doctor_id and b.patient_mail= %s ", [mail])

        status = cursor.fetchall()

        cursor.execute(
            'select * from patient where mail= %s and pwd =%s', (mail, pwd))
        account = cursor.fetchone()

        cursor.execute('select * from queries')
        queries = cursor.fetchall()

        cursor.execute('select * from doctor')
        doctor = cursor.fetchall()

        return render_template('index.html', doctor=doctor, len=len(doctor), patient=account, c=c, status=status,
                               len1=len(status), queries=queries, len2=len(queries))

    else:
        return redirect(url_for('login'))


@app.route("/consult", methods=["POST", "GET"])
def consult():
    if 's_mail' in session:
        patient_mail = request.args.get('a')
        doctor_id = request.args.get('b')
        # print(patient_mail)
        # print(doctor_id)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'insert into consult (patient_mail,doctor_id) values (%s,%s)', (patient_mail, doctor_id))
        mysql.connection.commit()
        return redirect(url_for('home'))

    else:
        return redirect(url_for('login'))


@app.route("/update", methods=["POST", "GET"])
def update():
    if 's_mail' in session and request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        location = request.form['location']
        BMI = request.form['bmi']
        mail = session.get('s_mail')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('update patient set name = %s , age=%s, gender= %s , location=%s , BMI=%s where mail =%s',
                       (name, age, gender, location, BMI, mail))
        mysql.connection.commit()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/askquery', methods=["POST", "GET"])
def askquery():
    if 's_mail' in session and request.method == 'POST':
        usrquestion = request.form['usrquestion']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'insert into queries (question) values(%s)', [usrquestion])
        mysql.connection.commit()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    if 's_mail' in session:
        # Remove session data, this will log the user out
        session.clear()

        # Redirect to login page
        return redirect(url_for('login'))


@app.route('/doctor', methods=["POST", "GET"])
def doctorLogin():
    msg = ''
    if request.method == 'POST' and 'mail' in request.form:
        mail = request.form['mail']
        pwd = request.form['pwd']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'select * from doctor where mail= %s and pwd =%s', (mail, pwd))
        doctor = cursor.fetchone()
        if doctor:
            session['loggedin'] = True
            session['d_id'] = doctor['id']
            session['d_pwd'] = doctor['pwd']
            return redirect(url_for('docpage'))
        else:
            return render_template('doctor_login.html', msg='Invalid Credentials')

    return render_template('doctor_login.html', msg='')


@app.route('/docpage/')
def docpage():
    if 'd_id' in session:
        id = session.get('d_id')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from doctor where id= %s ', [id])
        doctor = cursor.fetchone()

        cursor.execute('select * from queries')
        queries = cursor.fetchall()

        cursor.execute('SELECT a.name , b.patient_mail ,b.status,b.timing  from patient a, consult b where a.mail =  b.patient_mail and b.doctor_id= %s and b.status=%s', (id, 'Accepted'))
        check = cursor.fetchall()
        if check:
            check = len(check)
        else:
            check = 0
        cursor.execute(
            'SELECT a.name , b.patient_mail ,b.status,b.timing  from patient a, consult b where a.mail =  b.patient_mail and b.doctor_id= %s ', [id])
        reques = cursor.fetchall()

        return render_template('doctor_main_page.html', reques=reques, len=len(reques), doctor=doctor, check=check, queries=queries, len2=len(queries))
    else:
        return render_template('doctor_login.html', msg='')


@app.route('/consult_update', methods=["POST", "GET"])
def consult_update():
    if 'd_id' in session and request.method == 'POST':
        id = session.get('d_id')
        patient_mail = request.form['patient_mail']
        bday = request.form['bday']
        timing = request.form['timing']

        timing = bday + " "+timing
        status = 'Accepted'

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('update consult set status = %s, timing=%s  where patient_mail = %s and doctor_id = %s',
                       (status, timing, patient_mail, id))
        mysql.connection.commit()
        return redirect(url_for('docpage'))
    else:
        return render_template('doctor_login.html', msg='')


@app.route('/answerquery', methods=["POST", "GET"])
def answerquery():
    if 'd_id' in session and request.method == 'POST':
        sno = request.form['sno']
        answer = request.form['answer']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'update queries set answer = %s, status = %s where sno= %s ', (answer, 'answered', sno))
        mysql.connection.commit()
        return redirect(url_for('docpage'))
    else:
        return render_template('doctor_login.html', msg='')


@app.route('/doctorLogout/')
def doctorLogout():
    if 'd_id' in session:
        # Remove session data, this will log the user out
        session.clear()

        # Redirect to login page
        return redirect(url_for('doctorLogin'))


if __name__ == '__main__':
    app.run(debug=True)
