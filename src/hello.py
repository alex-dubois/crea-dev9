import os
import sys
import mysql.connector

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Crea!</p>"

@app.route("/version")
def version():
    return sys.version

@app.route("/environment")
def environment():
    host = os.getenv("MYSQL_HOST")
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    return f"Host: {host}\nUser: {user}\nPassword: {password}"

@app.route("/mysql-db")
def mysql_db():
    host = os.getenv("MYSQL_HOST")
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    db_name = request.args.get("db-name", "crea")

    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    curs = conn.cursor()

    try: 
        curs.execute(f"CREATE DATABASE {db_name}")
        return f"Database {db_name} created!"
    except mysql.connector.Error as err:
        return "Failed creating database: {}".format(err)
    finally:
        curs.close()
        conn.close()


