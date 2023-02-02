class Validacion:
    def camposRequeridos(self,paramsR,request,numRequired):
        if(numRequired==len(paramsR)):
            for paramR in paramsR:
               try:
                request[paramR]
               except:
                return False 
        else:
            return True
    def validarFechasLineales(self,fechaInicial,fechaFinal):
        if(fechaFinal>fechaInicial):
            return True
        else:
            return False