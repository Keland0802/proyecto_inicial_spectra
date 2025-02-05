from models.conexion import Conexion

class Plan:
    def __init__(self):
        self.con=Conexion()

        
    
    def createPlan(self, id, type_act, desc_act, num_proyect, hours,  comment):
            
            query = """INSERT INTO planeacion_actividades (cedula_usu, actividad, descripcion_act, num_proyecto, horas,
           comentario) VALUES (%s, %s, %s, %s, %s, %s)"""
        
            params = (id, type_act, desc_act, num_proyect, hours,  comment)
            
            register = self.con.insert(query, params)
            if register:
                return True
            else:
                return False
            
    def createBlockade(self, id, comment):
        
            query = "INSERT INTO planeacion_actividades (cedula_usu, comentario) VALUES (%s, %s)"
            params = (id, comment)
            register = self.con.insert(query, params)
            if register:
                return True
            else:
                return False