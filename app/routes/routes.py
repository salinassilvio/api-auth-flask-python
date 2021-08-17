import flask
from flask import Blueprint,request,jsonify
from models.models import Usuario
import bcrypt 
blue_print = Blueprint('app',__name__)

#Ruta Home o Inicio
@blue_print.route('/',methods=['GET'])
def inicio():
    return jsonify(respuesta='Rest API con Flask y Mysql')

#Ruta Home o Inicio
@blue_print.route('/auth/registrar',methods=['POST'])
def registrar_usuario():
    try:
        #Obtener el usuario
        usuario = request.json.get('usuario')
        #Obtener la Clave
        clave = request.json.get('clave')
        
        if not usuario or not clave:
            return jsonify(respuesta='Campos invalidos'),400

        #consultar la BD
        exist_usuario = Usuario.query.filter_by(usuario=usuario).first()

        if exist_usuario:
            return jsonify(respuesta='Usuario ya existe'),400

        #Encriptar password
        clave_encriptada = bcrypt.hashpw(clave.encode('utf-8'),bcrypt.gensalt())

        #Creamos el modelo a guardar en BD
        nuevo_usuario = Usuario(usuario,clave_encriptada)
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        return jsonify(respuesta='Usuario Creado Exitosamente'),201

    except Exception:
        return jsonify(respuesta='Error al crear usuario'),500