from flask import render_template, request, session, redirect
from flask_app import app


from flask_app.models.dojos import Dojo
#Importar Bcryp si es necesario




@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/proceso', methods=['POST'])

def proceso():
    
    if not Dojo.valida_dojo(request.form):
        return redirect('/index')


#creo un diccionario con todos los datos de request.form
    formulario = {
        "nombre": request.form['nombre'],
        "ubicacion": request.form['ubicacion'],
        "idioma": request.form['idioma'],
        "comentario": request.form['comentario']
    }

    id = Dojo.save(formulario)   #recivo el nuevo ID dojo
    session['dojo_id'] = id   #Guardo en session el identificador del usuario



    # session['nombre']= request.form['nombre']
    # session['ciudad']= request.form['ciudad']
    # session['lenguaje']= request.form['lenguaje']
    # session['comentario']= request.form['comentario']


    return redirect('/result')
    # return redirect('/index')

@app.route('/result')
def result():
    formulario = {"id": session['dojo_id']}

    dojo = Dojo.get_all_of_id(formulario) #Recibo la instancia del usuario en base a su id 
    return render_template('result.html', dojo=dojo)







