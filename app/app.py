from flask import Flask
from database import db
from sqlalchemy_utils import create_database, database_exists
from routes.routes  import blue_print
import datetime

app = Flask(__name__)

#Base de Datos
db_usuario = 'root'
db_clave = 'sjsa'
db_host = 'localhost'
db_nombre='db_api_auth_python'

DB_URL = f'mysql+pymysql://{db_usuario}:{db_clave}@{db_host}/{db_nombre}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = "2d3lt-5s-M1-Cl5v95"
app.config['JWT_ACCES_TOKEN_EXPIRES'] = datetime.timedelta(hours=4) #Token Expire en cuatro horas

#JWT
jwt = JWTManager(app)

#Inicializamos SQLAchemy para inicializar mi bd
db.init_app(app)


#Instanciamos las rutas de nuestro api
app.register_blueprint(blue_print)

# Creamos la base de Datos, en caso de no existir le paso la conexion para que me la cree
with app.app_context():
    if not database_exists(DB_URL):
        create_database(DB_URL)
    db.create_all()    

if __name__ == "__main__": 
    app.run(host='0.0.0.0',debug=True,port=5000) 