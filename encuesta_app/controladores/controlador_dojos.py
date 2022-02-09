from flask import Flask, render_template, request , redirect 
from encuesta_app import app
from encuesta_app.modelos.modelo_dojos import Dojo
from flask import flash


@app.route ('/', methods = ['GET'])
def Encuesta():
    return render_template('index.html')


@app.route('/envio', methods=['POST'])
def create_dojo():
    
    if Dojo.validate_dojo(request.form):
        Dojo.agregar(request.form)
        return redirect("/result")

    return redirect('/')
    


@app.route('/result', methods = ['GET'])
def result():
    return render_template ('result.html', dojo = Dojo.obtenerDatosDojos())





