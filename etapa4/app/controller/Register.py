from models.conexion import Conexion

class Register:
    def __init__(self):
        self.con=Conexion()

        
    
    def createRegister(self, id, type_act, desc_act, num_proyect, hours, date, comment):
        
      
           
            
            
            query = """INSERT INTO registro_actividades (cedula_usu, actividad, descripcion_act, num_proyecto, horas,
            fecha, comentario) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        
            params = (id, type_act, desc_act, num_proyect, hours, date, comment)
            
            register = self.con.insert(query, params)
            if register:
                return True
            else:
                return False