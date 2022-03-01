from flask import Flask, redirect, url_for, render_template, request

"""
Metodos HTTP:
    GET
    POST
"""

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index4.html")

@app.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"] # almacena el valor dado en el tag correspondiente a <input name="nm"/> en login.html 
        return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug = True)