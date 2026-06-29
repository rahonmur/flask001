from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index(): #Página principal
    #return '<H1>Hola Mundo!!!</H1>'
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    #return '<H1>Esta es la página de servicios</H1>'
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    #return '<H1>Esta es la página de contacto</H1>'
    return render_template('base.html')


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('page_not_found.html'), 404
