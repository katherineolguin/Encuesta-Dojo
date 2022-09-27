from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key= "It's september 26!"

@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/proceso', methods=['POST'])

def proceso():

    # return(request.form)

    session['nombre']= request.form['nombre']
    session['ciudad']= request.form['ciudad']
    session['lenguaje']= request.form['lenguaje']
    session['comentario']= request.form['comentario']


    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')












if __name__=="__main__":
    app.run(debug=True)