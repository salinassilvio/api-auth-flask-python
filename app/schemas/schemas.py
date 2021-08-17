from flask_marshmallow import Marshmallow

ma = Marshmallow()

# Esquema de usuario para la serializacion de los datos de mi tabla
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id','usuario','clave')
        
