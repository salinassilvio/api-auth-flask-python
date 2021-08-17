import flask


from flask import Blueprint,request,jsonify

blue_print = Blueprint('app',__name__)


#Ruta Home o Inicio
@blue_print.route('/',methods=['GET'])
def inicio():
    return "<h1>Flask API</h1>"