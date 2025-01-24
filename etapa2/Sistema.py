from etapa2.Registros import RegistrosActividades
from lib.helpers import Validaciones 


class Sistema:
    def __init__(self):
        self.registros = RegistrosActividades()
        self.validador=Validaciones()

    def iniciar(self):
        """
        Inicia el sistema de registro de actividades.
        Este método imprime un mensaje de bienvenida y solicita al usuario que ingrese su nombre e identificación.
        Luego, presenta un menú principal con las siguientes opciones:
        1. Registrar actividad del día anterior
        2. Planear actividad del día
        3. Generar informe
        4. Salir
        Dependiendo de la opción seleccionada, se ejecuta la acción correspondiente:
        - Registrar actividad del día anterior: Llama al método `registrarActividad` de la clase `registros`.
        - Planear actividad del día: Llama al método `planearActividad` de la clase `registros`.
        - Generar informe: Presenta un submenú con opciones para generar diferentes tipos de informes.
        - Salir: Termina la ejecución del sistema.
        Si se selecciona una opción inválida, se muestra un mensaje de error y se solicita una nueva entrada.
        """
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
                while True:
                    print("****************************************************************************************************************************************************************************")
                    print("***********************************************************************************Informes*********************************************************************************")
                    print("****************************************************************************************************************************************************************************")
                    print("1. Informe actividad anterior\n2. Informe del día\n3. Informe combinado\n4. Consultar por número de cédula\n5. Consultar por rango de fecha\n6.Volver al menú principal")
                    opcion_informe = input("Seleccione una opción: ")
                    if opcion_informe in ["1", "2", "3", "4", "5", "6"]:
                        menú=self.registros.generarInformes(opcion_informe)
                        print(menú)
                        if menú in ["1", "6"]:
                            break
                      
                        
                    else:
                        print("Por favor ingrese una opción válida")
            elif opcion == "4":
                print("Saliendo del sistema.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    

    def ingresar_nombre(self):
        """
        Solicita al usuario que ingrese su nombre completo y lo valida.

        Returns:
            str: El nombre completo ingresado por el usuario si es válido.

        Raises:
            None: No se generan excepciones, pero se solicita al usuario que intente nuevamente si el nombre no es válido.
        """
        while True:
            nombre = input("Ingrese su nombre completo: ")
            if self.validador.validar_nombres(nombre):
                return nombre
            print("El nombre ingresado no es válido. Intente nuevamente.")

    def ingresar_identificacion(self):
        """
        Solicita al usuario que ingrese su número de documento y valida que contenga solo números enteros.

        Returns:
            str: El número de documento ingresado por el usuario, validado como un número entero.
        """
        while True:
            identificacion = input("Ingrese su número de documento: ")
            if self.validador.validar_numeros_enteros(identificacion):
                return identificacion
            print("La identificación debe contener solo números.")