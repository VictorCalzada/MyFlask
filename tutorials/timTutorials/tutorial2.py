from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#Una funcion representa una página dentro de la wed

@app.route("/<name>") #Representa el path a la pagina a la que queremos acceder 
def home(name):
    """
    Pagina principal
    """
    return render_template("index.html", content=name,r=2)

if __name__ == '__main__':
    app.run()