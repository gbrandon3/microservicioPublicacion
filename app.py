from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from conectar.conectarBD import ConectarBD
from vistas.publicaciones import PublicacionesView
from vistas.publicacion import PublicacionView
from vistas.healthcheck import HealthCheck
from tokenjwt.token import Tokenjwt
app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True

conectar=ConectarBD()
conectar.conectar(app=app)



cors = CORS(app)

api = Api(app)
api.add_resource(PublicacionesView, "/posts")
api.add_resource(PublicacionView,"/posts/<int:id_post>")
api.add_resource(HealthCheck,"/posts/ping")
api.add_resource(Tokenjwt,"/token")

jwt = JWTManager(app)