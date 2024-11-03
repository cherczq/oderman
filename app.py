from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)  # main

@app.get("/")
def help():
    return render_template("help.html")


@app.get("/oderman/")
def main():
    return render_template("index.html", title="pizza", title2="20")

@app.get("/login/")
def get_login():
    return render_template("login.html")


@app.post("/login/")
def post_login():
    user = request.form["name"]
    info = request.user_agent
    if user == "admin":
        return f"Are you is {user} from {info}"
    else:
        return redirect(url_for("get_login"), code=302)

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


if __name__ == '__main__':
    app.run(port=8020, debug=True)
