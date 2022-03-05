from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

"""
Message Flashing:
    Mostrar mensajes
"""

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes = 5)

@app.route("/")
def home():
    return render_template("index6.html")

@app.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        session.permanet = True
        user = request.form["nm"] # almacena el valor dado en el tag correspondiente a <input name="nm"/> en login.html
        session["user"] = user # Almacena datos como un diccionario 
        flash("Login Succesful!") # mensaje flash que hará display en user debido a que se encuentra en user6.html el display
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login6.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user6.html", user = user)
    else:
        flash("You Are Not Logged In!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    
    flash("You have been logged out", "info")
    session.pop("user",None)
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)