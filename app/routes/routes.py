from types import resolve_bases
import flask
from flask import Blueprint,request,jsonify
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required
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

#Ruta para Iniciar Sesion
@blue_print.route('/auth/login',methods=['POST'])
def iniciar_sesion():
    try:
         #Obtener el usuario
        usuario = request.json.get('usuario')
        #Obtener la Clave
        clave = request.json.get('clave')
        
        if not usuario or not clave:
            return jsonify(respuesta='Campos invalidos'),400

        #consultar la BD
        exist_usuario = Usuario.query.filter_by(usuario=usuario).first()

        if not exist_usuario:
            return jsonify(respuesta='Usuario no encontrado'),404

        es_clave_valida = bcrypt.checkpw(clave.encode('utf-8'),exist_usuario.clave.encode('utf-8'))

        #Se validan que las contraseñas sean iguales.
        if es_clave_valida:
            access_token = create_access_token(identity=usuario)
            return jsonify(access_token=access_token),200
        return jsonify(respuesta='Clave o Usuario Incorrecto'),404
        
    except Exception:
        return jsonify(respuesta='Error en peticion'),500