from flask import Flask, redirect, url_for, render_template
"""
Template inheritance:
    Compartir por ejemplo la barra de navegación dentro de las 
    diferentes páginas de la web 

Bootstrap:
    Es un framework de css
"""
app = Flask(__name__)

#Una funcion representa una página dentro de la wed

@app.route("/") #Representa el path a la pagina a la que queremos acceder 
def home():
    """
    Pagina principal
    """
    return render_template("index3.html", content="Testing")

if __name__ == '__main__':
    app.run(debug = True ) #Importante debug = True. Actualiza la pagina directamente y da información de los errores  