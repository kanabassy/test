import sqlite3
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("top.html")

'''
@app.route('/db')
def db():
    conn = sqlite3.connect('event.db')
    c = conn.cursor()
    c.execute("select event_name,image,memo from event where id = 2")
    event_info = c.fetchone()
    c.close
    print(event_info)
    return render_template("db.html",event_info = event_info)
'''


@app.route('/toptop',methods=["GET"])
def top_get():
    return render_template("toptop.html")

@app.route('/toptop',methods=["POST"])
def top_post():
    birthday = request.form.get('birthday')
    d = datetime.strptime(birthday, "%Y-%m-%d")
    o = d + timedelta(days=6)
    hb = d + timedelta(days=31)
    hg = d + timedelta(days=32)
    m = d + timedelta(days=100)
    hbd = d + relativedelta(months=6)
    bd = d + relativedelta(years=1)
    sk = int(d.year) + 1
    km = int(d.year) + 2
    ht = int(d.year) + 3
    go = int(d.year) + 4
    na = int(d.year) + 6
    jhs = int(d.year) + 7
    return render_template("kekka.html",birthday = birthday, o = o, hb = hb, hg = hg, m = m, hbd = hbd, bd = bd, sk = sk, km = km, ht=ht,go=go,na=na,jhs=jhs)

''''
@app.route('/db',methods=["GET"])
def db_get():
    return render_template("db.html")

@app.route('/db',methods=["POST"])
def db_post():

    conn = sqlite3.connect('event.db')
    c = conn.cursor()
    c.execute("select event_name,image,memo from event where id = ?")
    event_info = c.fetchone()
    for row in c.fechall():
        event_info.append(("id":row[o],"event_name":row[1]))
    print(event_info)
    return render_template("db.html",event_info = event_info)
'''




if __name__ == '__main__':
    app.run(debug=True)