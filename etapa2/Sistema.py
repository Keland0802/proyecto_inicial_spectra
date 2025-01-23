from etapa2.Registros import RegistrosActividades
from lib.helpers import Validaciones 


class Sistema:
    def __init__(self):
        self.registros = RegistrosActividades()
        self.validador=Validaciones()

    def iniciar(self):
        print("****************************************************************************************************************************************************************************")
        print("***************************************************************Bienvenido al sistema de registro de actividades*************************************************************")
        print("****************************************************************************************************************************************************************************")
        self.nombre = self.ingresar_nombre()
        self.identificacion = self.ingresar_identificacion()

        while True:
            print("****************************************************************************************************************************************************************************")
            print("********************************************************************************menú****************************************************************************************")
            print("****************************************************************************************************************************************************************************")
            print("\nMenú Principal:")
            print("1. Registrar actividad del día anterior")
            print("2. Planear actividad del día")
            print("3. Generar informe")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registros.registrarActividad(self.nombre, self.identificacion)
            elif opcion == "2":
                self.registros.planearActividad(self.nombre, self.identificacion)
            elif opcion == "3":
                print("****************************************************************************************************************************************************************************")
                print("***********************************************************************************Informes*********************************************************************************")
                print("****************************************************************************************************************************************************************************")
                print("1. Informe día anterior\n2. Informe del día\n3. Informe combinado")
                opcion_informe = int(input("Seleccione: "))
                self.registros.generarInformes(opcion_informe)
            elif opcion == "4":
                print("Saliendo del sistema.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    

    def ingresar_nombre(self):
        while True:
            nombre = input("Ingrese su nombre completo: ")
            if self.validador.validar_nombres(nombre):
                return nombre
            print("El nombre ingresado no es válido. Intente nuevamente.")

    def ingresar_identificacion(self):
        while True:
            identificacion = input("Ingrese su número de documento: ")
            if self.validador.validar_numeros_enteros(identificacion):
                return identificacion
            print("La identificación debe contener solo números.")