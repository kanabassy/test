import sqlite3
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("toptop.html")


@app.route('/dbtest')
def dbtest():
    conn = sqlite3.connect('event.db')
    c = conn.cursor()
    c.execute("select event_name,image,memo from event where id = 4")
    event_info = c.fetchone()
    c.close
    print(event_info)
    return render_template("db.html",event_info = event_info)


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
    km = d + relativedelta(years=2)
    ht = d + relativedelta(years=3)
    go = d + relativedelta(years=4)
    na = d + relativedelta(years=6)
    jhs = d + relativedelta(years=6)
    return render_template("kekka.html",birthday = birthday, o = o, hb = hb, hg = hg, m = m, hbd = hbd, bd = bd, km = km, ht=ht,go=go,na=na,jhs=jhs)



if __name__ == '__main__':
    app.run(debug=True)