from Activity import Activity
from MasterModel import MasterModel

class PlaneacionActividad(Activity):
    def __init__(self):
        super().__init__()
        self.model=MasterModel()

    def planActivity(self, user_id):
       
        description = self.enter_blockade("Bloqueos y/o problemas para el desarrollo de la actividad del día?\n1.Si\nCualquier otro número para No", 
                                          """Describa los bloqueos y/o problemas con la actividad: """)
        if description!="Sin bloqueos y/o problemas":
            query="INSERT INTO planeacion_actividades (cedula_usu,comentario) VALUES (%s, %s)"
            params = (user_id, description)

        else: 
            activity = self.selectTypeAct()
            description_activity = self.enter_description("Descripción de la actividad que realizó: ")
            num_proyect = self.enter_num_proyect()
            hours = self.enter_hours()
            query="""INSERT INTO planeacion_actividades (cedula_usu, actividad, descripcion_act, num_proyecto, horas, comentario) VALUES (%s, %s, %s, %s, %s, %s)"""
            params = (user_id, activity, description_activity, num_proyect, hours, description)
            
        try:
            register = self.model.insert(query, params)
        except Exception as e:
            print(f"\nError al registrar la actividad: {e}")
            register = False

        if register:
            print("\nRegistro de actividad exitoso")
        else:
            print("\nError al registrar la actividad")
