
import os
from modelos.modelos import db  
class ConectarBD:
    def conectar(self,app):
        ISPRUEBAS = os.environ.get('ISPRUEBAS', None)
        
        if ISPRUEBAS is None:
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nombrebd.db'
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            app.config['PROPAGATE_EXCEPTIONS'] = True
            app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
            app_context = app.app_context()
            app_context.push()
            print("Aqui")
            db.init_app(app)
            db.create_all()
        else:
            ISLOCAL = os.environ.get('ISLOCAL', None)

            if os.environ.get('PASSWORD', None) is None:
                os.environ['PASSWORD'] = ''

            if os.environ.get('PUBLIC_IP_ADDRESS', None) is None:
                os.environ['PUBLIC_IP_ADDRESS'] = ''
            
            if os.environ.get('DBNAME', None) is None:
                os.environ['DBNAME'] = ''
            
            if os.environ.get('INSTANCE_NAME', None) is None:
                os.environ['INSTANCE_NAME'] = ''

            if os.environ.get('PROJECT_ID', None) is None:
                os.environ['PROJECT_ID'] = ''
            
            PASSWORD = os.environ.get('PASSWORD', None)
            PUBLIC_IP_ADDRESS = os.environ.get('PUBLIC_IP_ADDRESS', None)
            DBNAME = os.environ.get('DBNAME', None)
            PROJECT_ID = os.environ.get('PROJECT_ID', None)
            INSTANCE_NAME = os.environ.get('INSTANCE_NAME', None)
            
            if ISLOCAL is None:
                app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
            else:
                app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:{}@{}/{}".format(PASSWORD, PUBLIC_IP_ADDRESS, DBNAME)

            app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
            app_context = app.app_context()
            app_context.push()
            db.init_app(app)
            db.create_all()