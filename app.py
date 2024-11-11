from flask import Flask, render_template, request, redirect, url_for, abort
import sqlite3
app = Flask(__name__)  # main
ADMIN = "admin"
@app.get("/")
def help():
    return render_template("help.html")


@app.get("/oderman/")
def main():
    return render_template("index.html", title="pizza", title2="20")

# @app.get("/login/")
# def get_login():
#     return render_template("login.html")


# @app.post("/login/")
# def post_login():
#     user = request.form["name"]
#     password = request.form["password"]
#     if password == ADMIN:
#         return redirect(url_for("admin"))
#     else:
#         return redirect(url_for("menu"))

max_price = 50
name = "Oderman-menu"
menu = [
  {"name": "Hawaiian Pizza",  "composition": "ham,pineapple,tomato sauce,ham","price":30},
  {"name": "Pepperoni Pizza","composition": "Tomato sauce, mozzarella cheese, and pepperoni", "price":40},
  {"name": "Margherita Pizza", "composition": "Fresh mozzarella, tomato sauce,and basil","price":17},
  {"name": "Meat Lovers Pizza", "composition": "Tomato sauce, mozzarella cheese, pepperoni, sausage, bacon, and ham","price": 26},
  {"name": "White Pizza",  "composition": "Mozzarella cheese, ricotta cheese, garlic, and spinach.","price": 34},
]
@app.get('/menu/')
def results():
  context={
     "title": "Oderman",
     "Pizzas": menu,
     "pizzas_name": name,
     "max_prise": max_price,
  }
  return  render_template("menu.html",**context)

@app.get("/")
@app.get("/home/")
def index():
    create_table()
    return render_template("index.html")


def create_table():
    sql_connection = sqlite3.connect('database.db')
    cursor = sql_connection.cursor()

    sqlite_create_table_query = """CREATE TABLE IF NOT EXISTS PIZZAS
                                    (name TEXT NOT NULL,
                                    ingredients TEXT NOT NULL,
                                    price REAL NOT NULL)"""

    cursor.execute(sqlite_create_table_query)
    sql_connection.commit()


@app.get("/join/")
def get_join():
    return render_template("join.html")


@app.post("/join/")
def post_join():
    name = request.form["name"]
    ingredients = request.form["ingredients"]
    price = request.form["price"]

    with sqlite3.connect('database.db') as pizza:
        cursor = pizza.cursor()
        data = (name, ingredients, price)
        cursor.execute("""
        INSERT INTO PIZZAS (name, ingredients, price)
        VALUES (?, ?, ?)""", data)
        pizza.commit()
        return render_template("index.html")


@app.get("/pizzas/")
def pizzas():
    with sqlite3.connect('database.db') as pizza:
        cursor = pizza.cursor()

        cursor.execute("""
        SELECT * FROM PIZZAS""")
        data = cursor.fetchall()

        return render_template("pizzas.html", data=data)


if __name__ == '__main__':
    app.run(port=8077, debug=True)
