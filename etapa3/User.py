
from lib.helpers import Validaciones
from MasterModel import MasterModel
class User:
    def __init__(self):
        self.name = None
        self.id = None
        self.validator = Validaciones()
        
    def enterName(self):
        while True:
            name = input("Ingrese su nombre completo: ")
            if self.validator.validar_nombres(name):
                return name
            else:
                print("Nombre no válido. Intente nuevamente, el nombre solo debe contener letras y espacios.")  
                
    def enterId(self):
        while True:
            id = input("Ingrese su número de identificación: ")
            
            if self.validator.validar_identificacion(id):
                if len(id)<6:
                    print("Identificación no válida. Debe tener mínimo 5 dígitos.")
                elif len(id)>10:
                    print("Identificación no válida. Debe tener máximo 10 dígitos.")
                else:
                    return id
            else:
                print("Identificación no válida. Intente nuevamente, recuerde que el número de identificación debe contener solo números.")
                
           
    def setName(self,name):
        self.name=name
    
    def setId(self, id):
        self.id=id       
    
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def createUser(self):
        self.name = self.enterName()
        self.id = self.enterId()
        user=self.verifyUser(self.id)
        if user:
            print("Usuario ya registrado")
            return
        else:
            query = f"INSERT INTO usuarios (nombre, cedula) VALUES ('{self.name}', '{self.id}')"
            
            newUser=MasterModel().insert(query)
            if newUser:
                print("Usuario registrado con éxito")
            else:
                print("Error al insertar usuario")
        
       

    def verifyUser(self, id):
        query = f"SELECT * FROM usuarios WHERE cedula = {id}"
        try:
            User=MasterModel().consult(query)
            if User:
                return True
            else:
                return False
            
        except Exception:
            print("Error al buscar usuario")
            return None