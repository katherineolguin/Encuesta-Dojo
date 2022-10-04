from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #Encargado de mostrar mensajes o errores

import re #Importamos expresiones regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email

class Dojo:

    def __init__(self, data):

        self.id = data['id']
        self.nombre = data['nombre']
        self.ubicacion = data['ubicacion']
        self.idioma = data['idioma']
        self.comentario = data['comentario']
        self.created_at = data['created_at']
        self.update_at = data['update_at']


    @staticmethod

    def valida_dojo(formulario):
        
        es_valido=True
    
#Valido que tenga al menos 3 caracteres
        if len(formulario['nombre'])<3:
            flash('Nombre debe tener al menos 3 caracteres!','prosess')
            es_valido = False
#Valido que elija una ubicacion
        if len(formulario['ubicacion'])<1:
            flash('Elija una ubicación','prosess')
            es_valido = False
#Valido que elija un idioma
        if len(formulario['idioma'])<1:
            flash('Elija un idioma','prosess')
            es_valido = False
#Valido que tenga al menos 3 caracteres
        if len(formulario['comentario'])<3:
            flash('Comentario debe tener al menos 3 caracteres!','prosess')
            es_valido = False

        return es_valido

    @classmethod
    def save(cls, formulario):
        query= "INSERT INTO dojos (nombre, ubicacion, idioma, comentario) VALUES (%(nombre)s, %(ubicacion)s, %(idioma)s, %(comentario)s)"
        result = connectToMySQL('esquema_encuesta_dojo').query_db(query, formulario)
        return result  #El ID del nuevo registro!

    @classmethod 
    def get_all_of_id(cls, formulario):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL('esquema_encuesta_dojo').query_db(query, formulario)
        #result =[
        #     {id:1, nombre:salvador, idioma:JavaScript, Ubicacion:China, comentario:Blablabla}
        # ]
        
        dojo = cls(result[0]) #Creo una instancia Dojo
        return dojo

