from database import db

 # tabla usuario en Mysql
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer,primary_key=True)
    usuario = db.Column(db.String(70),nullable=False,unique=True)
    clave = db.Column(db.String(100),nullable=False)

    def __init__(self,usuario,clave):
        self.usuario = usuario
        self.clave = clave