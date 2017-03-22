#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',hello = "hello world" )

@app.route('/hermanos')
def pagHermanos():
    lista  = ['hugo', 'rodolfo', 'tadeo']
    return render_template('hermanos.html',hello = "hello world", lista = lista)

#http://127.0.0.1:8000/params?param1=isidro&param2=rivera 
@app.route('/params')
def params():
    param = request.args.get('param1', 'No contiene el parametro1')
    param2 = request.args.get('param2', 'No contiene el parametro2')
    return 'los parametro 1 Nombre: {} , el parametro 2 Apellido: {}'.format(param, param2)

#http://127.0.0.1:8000/datos/isidro/28
#http://127.0.0.1:8000/datos/isidro/
#http://127.0.0.1:8000/datos
@app.route('/datos')
@app.route('/datos/<nombre>')
@app.route('/datos/<nombre>/<int:edad>')
def datos(nombre = 'No contiene nombre', edad = 0):
    return 'el nombre es {0} y su edad es : {1}'.format(nombre, edad)


#http://127.0.0.1:8000/validar/isidro?param1=Rivera&param2=28
@app.route('/validar/<nombre>')
def validar(nombre = 'Sin'):
    param1 = request.args.get('param1', ' sin')
    edad   = request.args.get('param2', 0, type=int)
    lista  = ['hugo', 'rodolfo', 'adrian']
    #lista  = request.args.get('param3', [], type=list)
    return render_template('validar.html', nombre = nombre, apellidos = param1, edad = edad, lista = lista)

@app.route('/inicio')
def paginaInicio():
    return render_template('inicial.html')

@app.route('/article1')
def article1():
    return render_template('article1.html')

if __name__ == '__main__':
    app.run(debug=True , port=8000)


#app = Flask(__name__, template_folder = '<nombre carpeta de archivos html>')  si se quiere utilizar otra carpeta para los archivos html
#@app.route('/usuarios/<usuario>', methods=['GET'])
#def usuario(usuario):
#    if (usuario == 'isidro'):
#        user = "el nombre del usuario es {0} es correcto".format(usuario)
#    else:
#        user = "el nombre del usuario es {0} no existe".format(usuario)
#    return user
#
#@app.route('/login')
#def login(usuario, contraseña):
#    if (usuario == "isidro" and contraseña == "123"):
#        return render_template('index.html',hello = "ok si" )
#    else:
#        return render_template('index.html',hello = "ok no" )