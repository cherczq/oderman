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
 


@app.get("/menu/")
def get_menu():
    return render_template("menu.html")


if __name__ == '__main__':
    app.run(port=8020, debug=True)
