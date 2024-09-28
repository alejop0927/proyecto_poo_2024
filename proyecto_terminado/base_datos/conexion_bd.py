from flask import Flask, request, send_file
from flask_mysqldb import MySQL
import io

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'A0927lejop#'
app.config['MYSQL_DB'] = 'proyecto'

mysql = MySQL(app)
