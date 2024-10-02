import sqlite3

import uvicorn
from fastapi import FastAPI

from data import db_session
from data.Table import Cat

app = FastAPI()
con = sqlite3.connect("cats_db", check_same_thread=False)
cur = con.cursor()
db_session.global_init("db/cats_db")


@app.get("/colors")
async def all_colors(clr=""):
    if clr:
        db_sess = db_session.create_session()
        color = db_sess.query(Cat).filter(Cat.color == str(clr)).all()
        db_sess.close()
        ans = []
        for x in color:
            a = str(x).split(",")
            ans.append(a[1])
        return ans
    db_sess = db_session.create_session()
    color = db_sess.query(Cat).all()
    db_sess.close()
    ans = []
    for x in color:
        a = str(x).split(",")
        ans.append(a[1])
    return ans


@app.get("/cats")
async def all_cats():
    db_sess = db_session.create_session()
    cats = db_sess.query(Cat).all()
    db_sess.close()
    return cats


@app.get("/desc")
async def desc(id=""):
    db_sess = db_session.create_session()
    dsc = db_sess.query(Cat).filter(Cat.id == id).first()
    db_sess.close()
    return str(dsc).split(",")[3]


@app.get("/add")  #пример запроса /add?color=black&age=37&dsc=кот
async def add_cat(color, age, dsc):
    db_sess = db_session.create_session()
    db_sess.add(Cat(
        color=color,
        age=age,
        discription=dsc
    ))
    db_sess.commit()
    db_sess.close()
    return


@app.get("/change")
async def change(id, param, data):
    dct = {"color": Cat.color,
           "age": Cat.age,
           "description": Cat.description,
           "id": Cat.id}
    if data.isdigit():
        data = int(data)
    db_sess = db_session.create_session()
    db_sess.query(Cat).filter(Cat.id == int(id)).update({dct[param]: data})
    db_sess.commit()
    db_sess.close()
    return


@app.get("/del")
async def dlt(id):
    db_sess = db_session.create_session()
    db_sess.query(Cat).filter(Cat.id == id).delete()
    db_sess.commit()
    db_sess.close()
    return


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
