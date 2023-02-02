from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import create_access_token
from flask import request
from flask_restful import Resource
from modelos.modelos import db,Publicacion,PublicacionSchema
from datetime import datetime
from validacion.validacion import Validacion
validador=Validacion()
publicacionSchema=PublicacionSchema()
class PublicacionesView(Resource):
    @jwt_required()
    def post(self):
        if(validador.camposRequeridos(paramsR=["plannedStartDate","plannedEndDate","routeId"],request=request.json,numRequired=3)):
            if(validador.validarFechaValidaISO(request.json["plannedStartDate"]) and validador.validarFechaValidaISO(request.json["plannedEndDate"]) ):
        
                plannedStartDate = datetime.strptime(request.json["plannedStartDate"],'%Y-%m-%d')
                plannedEndDate=datetime.strptime(request.json["plannedEndDate"],'%Y-%m-%d')
                if(validador.validarFechasLineales(datetime.now(),plannedStartDate)):
                    return "La fecha de inicio es invalida",412
                if(validador.validarFechasLineales(plannedStartDate,plannedEndDate)):
                    return "Las fechas no son lineales",412 
                post=Publicacion(routeId=2,userId=3,plannedStartDate=plannedStartDate,plannedEndDate=plannedEndDate)
                db.session.add(post)
                db.session.commit()
                return{"id":post.id,"userId":3,"createdAt":post.createdAt.isoformat()}
            else:
                return "Formato de fecha invalido",412
        else:
            return "No se encuentran todos los campos requeridos",400
        
    @jwt_required()
    def get(self):
        when=request.args.get('when')
        route=request.args.get('route')
        date=False
        routeF=False
        query=Publicacion.query
        if when!=None:
            when=datetime.strptime(when,'%Y-%m-%d')
            query=query.filter(Publicacion.plannedEndDate==when)
            print(when)
            
        
        if route!=None:
            if(not route.isnumeric()):
                return "El formato de la ruta no es el correcto",400
            else:
                query=query.filter(Publicacion.routeId==route)
        
        filterq=request.args.get("filter")
        if filterq!=None:
            if(filterq.lower()!="me"):
                 return "Filter invalido",400
            else:
                query.filter(Publicacion.userId==2)
      
   
           
        return [publicacionSchema.dump(i) for i in query.all()]
            

                
      