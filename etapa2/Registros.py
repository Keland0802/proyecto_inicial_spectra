from lib.helpers import Validaciones 


class RegistrosActividades:
    def __init__(self):
          self.registroActividad = []
          self.planeacionActividad = []
          self.validador=Validaciones()
          
    def registrarActividad(self, nombre,cedula):
        print("****************************************************************************************************************************************************************************")
        print("***************************************************************Registre su actividad realizada el dia de ayer***************************************************************")
        print("****************************************************************************************************************************************************************************")
        actividad=self.seleccionar_actividad()
        descripcion_actividad=self.ingresar_descripcion("Descripción de la actividad que realizó: ")
     
    def planearActividad(self, nombre,cedula):
        pass
    
    def generarInformes(self,tipo_informe):
        pass

    
    def seleccionar_actividad(self):
        """
        Permite al usuario seleccionar un tipo de actividad de una lista predefinida.

        Presenta un menú con las opciones disponibles y solicita al usuario que ingrese
        una opción. Si la opción ingresada es válida, retorna el nombre de la actividad
        correspondiente. Si la opción es inválida, solicita al usuario que intente nuevamente.

        Returns:
            str: El nombre de la actividad seleccionada.
        """
        actividades = {"1": "Soporte", "2": "Backend", "3": "Frontend"}
        while True:
            print("\nSeleccione el tipo de actividad:")
            print("1. Soporte\n2. Backend\n3. Frontend")
            opcion = input("Ingrese una opción: ")
            if opcion in actividades:
                return actividades[opcion]
            print("Opción inválida. Intente nuevamente.")
            
            
    
    def ingresar_descripcion(self, mensaje):
        while True:
            descripcion = input(mensaje)
            if self.validador.validar_texto(descripcion):
                return descripcion
            print("La descripción ingresada no es válida. Asegúrate de que solo contenga letras y espacios, intente nuevamente.")
