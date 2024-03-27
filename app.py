from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Patrick in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://psharp725_hello_world_user:mki9WoZr1id3v32XMjXRxuFsgI9ycc1j@dpg-co1rlv821fec73d3uqv0-a/psharp725_hello_world")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect('postgres://psharp725_hello_world_user:mki9WoZr1id3v32XMjXRxuFsgI9ycc1j@dpg-co1rlv821fec73d3uqv0-a/psharp725_hello_world')
    cur = conn.cursor()
    cur.execute)('''
    CREATE TABLE IF NOT EXISTS Basketball(
    First varchar(255),
    Last varchar(255),
    City varchar(255),
    Name carchar(255),
    Number int
    );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
