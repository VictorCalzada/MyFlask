from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#Una funcion representa una página dentro de la wed

@app.route("/") #Representa el path a la pagina a la que queremos acceder 
def home():
    """
    Pagina principal
    """
    return "Hello! main page here <h1>HELLO</h1>"


@app.route("/<name>") #Lo que queda dentro de <> se pasa a la función
def user(name):
    return(f'hello {name}')

@app.route("/admin")
def admin():
    """
    Nos redirecciona a home 
    """
    return redirect(url_for("user", name = "Admin!"))


if __name__ == '__main__':
    app.run()