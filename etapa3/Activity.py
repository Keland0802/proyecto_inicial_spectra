from lib.helpers import Validaciones
from MasterModel import MasterModel
class Activity:
    def __init__(self):
        self.validador = Validaciones()
        
    def selectTypeAct(self):
        query = "SELECT id_tipo_actividad, nombre_tipo_actividad FROM tipo_actividades"
        activit = MasterModel().consult(query)
        activities = dict((str(row[0]), row[1]) for row in activit)
        while True:
            for key, value in activities.items():
                print(f"{key}. {value}")
            opcion = input("Ingrese una opción: ")
            if opcion in activities:
                return opcion  # Return the id instead of the name
            print("\n")
            print("Opción inválida. Intente nuevamente.")

    def enter_description(self, message):
         while True:
            print("\n")
            description = input(message)
            if self.validador.validar_texto(description):
                return description
            print("\n")
            print("La descripción ingresada no es válida. Asegúrate de que solo contenga letras y espacios, intente nuevamente.")



    def enter_num_proyect(self):
        while True:
            print("\n")
            print("1. Ingresar número de proyecto\n2. Continuar sin ingresar número de proyecto")
            option=input("Ingrese una opción: ")
            if self.validador.validar_numeros_enteros(option):
                break
            print("\n")
            print(" La opción debe contener solo números.")
        if option == "1":
            while True:
                print("\n")
                num_proyect = input("Ingrese el número de proyecto: ")
                if self.validador.validar_numeros_enteros(num_proyect):
                    return num_proyect
                print("\n")
                print("El número de proyecto debe contener solo números.")
        else: 
            return None

    def enter_hours(self):
        while True:
            print("\n")
            hours = input("Ingrese el número de horas dedicadas a la actividad: ")
            if self.validador.validar_numeros_enteros(hours):
                return hours
            print("\n")
            print("El número de horas debe contener solo números.")
            

    def enter_date(self):
        while True:
            print("\n")
            date = input("Ingrese la fecha de la actividad en formato aaaa-mm-dd: ")

            if self.validador.validar_fecha(date):
                return date
            print("\n")
            print("La fecha ingresada no es válida. Intente nuevamente.")
            
            

    def enter_blockade(self,comment, message_blockade):
        while True:
            print(comment)
            option=input("Ingrese una opción: ")
            if self.validador.validar_numeros_enteros(option):
                break
            print("\n")
            print(" La opción debe contener solo números.")
            
        if option == "1":       
            while True:
                print("\n")
                description = input(message_blockade)
                if self.validador.validar_texto(description):
                    return description
                print("\n")
                print("La descripción ingresada no es válida. Asegúrate de que contenga letras y espacios, intente nuevamente.")
        else:
            return "Sin bloqueos y/o problemas"