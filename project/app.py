from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'loginpage'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        fname = details['fullname']
        UID= details['uid']
        email= details['email']
        Company_name = details['compname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(fname,UID,Company_name,email) VALUES (%s,%s,%s,%s)", (fname,UID,Company_name,email))
        mysql.connection.commit()
        cur.close()
        return render_template('welcome.html',fid=fname, uid=UID, cid=Company_name, eid=email)
    return render_template('index.html')
@app.route('/welcome')
def welcomepage():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run()
