import sqlite3
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("top.html")


@app.route('/top',methods=["POST"])
def top_post():
    birthday = request.form.get('birthday')
    d = datetime.strptime(birthday, "%Y-%m-%d")
    o = d + timedelta(days=6)
    hb = d + timedelta(days=31)
    hg = d + timedelta(days=32)
    m = d + timedelta(days=100)
    hbd = d + relativedelta(months=6)
    bd = d + relativedelta(years=1)

    targets = [datetime.strptime(birthday, "%Y-%m-%d")]
    from_dt = datetime(2021, 1, 1)
    to_dt = datetime(2021, 1, 31)

    for target in targets:
      if from_dt <= target <= to_dt: # 1/31より小さく1/1よりも大きい 1/1から1/31のあいだ
        print(target)
        msk = int(d.year)
      else:
        print(d)
        msk = int(d.year) + 1

    targets = [datetime.strptime(birthday, "%Y-%m-%d")]
    from_dt = datetime(2021, 1, 1)
    to_dt = datetime(2021, 4, 5)

    for target in targets:
      if from_dt <= target <= to_dt: # 4/5より小さく1/1よりも大きい 1/1から4/5のあいだ
        print(target)
        tsk = int(d.year)
      else:
        print(d)
        tsk = int(d.year) + 1

    km = int(d.year) + 2
    ht = int(d.year) + 3
    go = int(d.year) + 4
    na = int(d.year) + 6

    targets = [datetime.strptime(birthday, "%Y-%m-%d")]
    from_dt = datetime(2021, 1, 1)
    to_dt = datetime(2021, 4, 2)

    for target in targets:
      if from_dt <= target <= to_dt: # 4/2より小さく1/1よりも大きい 1/1から4/2のあいだ
        print(target)
        jhs = int(d.year) + 6
      else:
        print(d)
        jhs = int(d.year) + 7

    return render_template("kekka.html",birthday = birthday, o = o, hb = hb, hg = hg, m = m, hbd = hbd, bd = bd, msk = msk, tsk = tsk, km = km, ht=ht,go=go,na=na,jhs=jhs)



if __name__ == '__main__':
    app.run(debug=True)