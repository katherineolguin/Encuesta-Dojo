from flask_app import app

#Importar controladores
from flask_app.controllers import dojos_controllers



#Ejecutamos variable app
if __name__=="__main__":
    app.run(debug=True)