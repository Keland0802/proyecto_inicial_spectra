from Activity import Activity
from MasterModel import MasterModel

class PlaneacionActividad(Activity):
    def __init__(self):
        super().__init__()
        self.model = MasterModel()

    def planActivity(self, user_id):
        """
        Registers the user's daily activity or any blockades/problems encountered.
        Args:
            user_id (int): The ID of the user.
        Returns:
            None
        Raises:
            Exception: If there is an error while registering the activity.
        The function prompts the user to enter any blockades or problems encountered during the day's activity.
        If there are blockades/problems, it inserts a record with the user's ID and the description of the blockades/problems.
        If there are no blockades/problems, it prompts the user to enter the type of activity, a description of the activity,
        the project number, and the number of hours spent on the activity. It then inserts a record with these details.
        The function prints a success message if the activity is registered successfully, otherwise it prints an error message.
        """
        description = self.enter_blockade("¿Bloqueos y/o problemas para el desarrollo de la actividad del día?\n1. Sí\nCualquier otro número para No", 
                                          "Describa los bloqueos y/o problemas con la actividad: ")
        if description != "Sin bloqueos y/o problemas":
            query = "INSERT INTO planeacion_actividades (cedula_usu, comentario) VALUES (%s, %s)"
            params = (user_id, description)
        else: 
            activity = self.selectTypeAct()
            description_activity = self.enter_description("Descripción de la actividad que realizó: ")
            num_proyect = self.enter_num_proyect()
            hours = self.enter_hours()
            query = """INSERT INTO planeacion_actividades (cedula_usu, actividad, descripcion_act, num_proyecto, horas, comentario) VALUES (%s, %s, %s, %s, %s, %s)"""
            params = (user_id, activity, description_activity, num_proyect, hours, description)
            
        try:
            register = self.model.insert(query, params)
        except Exception as e:
            print("\nError al registrar la actividad: ")
            register = False

        if register:
            print("\nRegistro de actividad exitoso")
        else:
            print("\nError al registrar la actividad")
