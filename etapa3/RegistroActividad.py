from Activity import Activity
from MasterModel import MasterModel

class RegistroActividad(Activity):
    def __init__(self):
        super().__init__()
        self.model = MasterModel()

    def registerActivity(self, user_id):
        activity = self.selectTypeAct()
        description_activity = self.enter_description("Descripción de la actividad que realizó: ")
        num_proyect = self.enter_num_proyect()
        hours = self.enter_hours()
        date = self.enter_date()
        description = self.enter_blockade("Bloqueos y/o problemas para el desarrollo de la actividad?\n1.Si\nCualquier otro número para No", "Describa los bloqueos y/o problemas con la actividad: ")

        query = """INSERT INTO registro_actividades (cedula_usu, actividad, descripcion_act, num_proyecto, horas,
        fecha, comentario) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        
        params = (user_id, activity, description_activity, num_proyect, hours, date, description)
        
        register = self.model.insert(query, params)
        if register:
            print("\nRegistro de actividad exitoso")
        else:
            print("\nError al registrar la actividad")