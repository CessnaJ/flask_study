from flask import Flask, request, redirect
import pymysql

app = Flask(__name__)

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='root',
                     db='dbname',
                     charset='utf8')

cursor = db.cursor()

@app.route('/')
def index():
    return 'hello?'

@app.route('/read/<id>/')
def read(id):
    return id


if __name__ == '__main__':
    app.run(port=5000, debug=True)
