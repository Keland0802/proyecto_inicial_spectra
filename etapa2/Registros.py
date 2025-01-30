from datetime import datetime

from tabulate import tabulate
from lib.helpers import Validaciones 


class RegistrosActividades:
    def __init__(self):
          self.registroActividad = []
          self.planeacionActividad = []
          self.validador=Validaciones()
          
    def registrarActividad(self, nombre,cedula):
        """
        Registra una actividad realizada por un usuario.

        Este método solicita al usuario que ingrese detalles sobre una actividad que realizó, 
        incluyendo el tipo de actividad, una descripción, el número de proyecto, horas dedicadas, 
        la fecha y cualquier bloqueo o problema encontrado. La información recopilada se agrega 
        a la lista `registroActividad`.

        Args:
            nombre (str): El nombre del usuario.
            cedula (str): El número de identificación del usuario.

        Returns:
            None
        """
        print("****************************************************************************************************************************************************************************")
        print("***************************************************************Registre su actividad realizada el dia de ayer***************************************************************")
        print("****************************************************************************************************************************************************************************")
        actividad=self.seleccionar_actividad()
        descripcion_actividad=self.ingresar_descripcion("Descripción de la actividad que realizó: ")
        num_proyecto=self.ingresar_num_proyecto()
        horas=self.ingresar_horas()
        fecha=self.ingresar_fecha()
        descripcion=self.ingresar_bloqueo("Bloqueos y/o problemas para el desarrollo de la actividad?\n1.Si\nCualquier otro número para No","Describa los bloqueos y/o problemas con la actividad: ")
        self.registroActividad.append({
                    "nombre": nombre,
                    "identificación": cedula,
                    "tipo de actividad": actividad,
                    "descripción de actividad": descripcion_actividad,
                    "numero de proyecto": num_proyecto,
                    "horas":horas,
                    "fecha":fecha,
                    "comentario":descripcion
                }) 
        print("Registro completado")
        
        
     
    def planearActividad(self, nombre,cedula):
        """
            Planificar y registrar una actividad para el día.
            Este método solicita al usuario que describa cualquier bloqueo o problema que pueda enfrentar durante la actividad del día.
            Si hay bloqueos, registra el nombre del usuario, la identificación y los comentarios sobre los bloqueos.
            Si no hay bloqueos, solicita al usuario que seleccione una actividad, la describa, ingrese el número de proyecto 
            y el número de horas que planea dedicarle. Luego registra toda esta información junto con la fecha actual.
            Args:
                nombre (str): El nombre del usuario.
                cedula (str): El número de identificación del usuario.
            Returns:
                None
        """
        print("\n")
        print("****************************************************************************************************************************************************************************")
        print("***************************************************************************Indique su actividad del día*********************************************************************")
        print("****************************************************************************************************************************************************************************")
        print("\n")
        descripcion=self.ingresar_bloqueo("Bloqueos y/o problemas para el desarrollo de la actividad del día?\n1.Si\nCualquier otro número para No","Describa los bloqueos y/o problemas con la actividad: ")
        if descripcion!="Sin bloqueos y/o problemas":
            self.planeacionActividad.append({
                "nombre": nombre,
                "identificación": cedula,
                "comentario":descripcion

            })
        else:
            actividad=self.seleccionar_actividad()
            descripcion_actividad=self.ingresar_descripcion("Descripción de la actividad que realizará: ")
            num_proyecto=self.ingresar_num_proyecto()
            horas=self.ingresar_horas()
            fecha=datetime.now().date()
            
            self.planeacionActividad.append({
                    "nombre": nombre,
                "identificación": cedula,
                "tipo de actividad": actividad,
                "descripción de actividad": descripcion_actividad,
                "numero de proyecto": num_proyecto,
                "horas":horas,
                "fecha":fecha,
                "comentario":descripcion

            })
            print("Registro completado")

        print("\n")
        
    
    def generarInformes(self,tipo_informe):
        """
        Genera informes basados en el tipo de informe especificado.
        Parámetros:
        tipo_informe (str): El tipo de informe a generar. Puede ser uno de los siguientes valores:
            "1" - Genera el informe de actividad anterior.
            "2" - Genera el informe de actividad del día.
            "3" - Genera otros informes.
            "4" - Genera el informe de cédula.
            "5" - Genera el informe de rango de fechas.
            "6" - Retorna la opción "6".
        Retorna:
        str: La opción "6" si el tipo de informe es "6".
        None: Si el tipo de informe no es válido o si se genera cualquier otro informe.
        """
        if tipo_informe=="1":
            self.informe_actividad_anterior()
        elif tipo_informe=="2":
             self.informe_actividad_dia()
        elif tipo_informe=="3":
             self.informes()
        elif tipo_informe=="4":
             self.informe_cedula()
        elif tipo_informe=="5":
             self.informe_rango_fecha()
        elif tipo_informe=="6":
            opcion="6"
            return opcion
        else:
            print("Por favor ingrese una opción válida")

        return self.opcionSalida()
    
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
            print("\n")
            print("Opción inválida. Intente nuevamente.")
            
            
    
    def ingresar_descripcion(self, mensaje):
        """
        Solicita al usuario que ingrese una descripción y la valida.

        Args:
            mensaje (str): El mensaje que se mostrará al usuario solicitando la descripción.

        Returns:
            str: La descripción ingresada por el usuario que ha sido validada.

        Nota:
            La descripción debe contener solo letras y espacios. Si la descripción no es válida,
            se solicitará al usuario que ingrese una nueva descripción hasta que sea válida.
        """
        while True:
            print("\n")
            descripcion = input(mensaje)
            if self.validador.validar_texto(descripcion):
                return descripcion
            print("\n")
            print("La descripción ingresada no es válida. Asegúrate de que solo contenga letras y espacios, intente nuevamente.")


    def ingresar_num_proyecto(self):
        """
            Solicita al usuario que ingrese un número de proyecto y valida la entrada.

            Este método solicita continuamente al usuario que ingrese un número de proyecto hasta que se proporcione un entero válido.
            Utiliza el método `validar_numeros_enteros` del atributo `validador` para verificar si la entrada es un entero válido.

            Returns:
                str: El número de proyecto válido ingresado por el usuario.
        """
        while True:
            print("\n")
            num_proyecto = input("Ingrese el número de proyecto: ")
            if self.validador.validar_numeros_enteros(num_proyecto):
                return num_proyecto
            print("\n")
            print("El número de proyecto debe contener solo números.")
     
            
    def ingresar_horas(self):
        """
            Solicita al usuario que ingrese el número de horas dedicadas a una actividad.
            
            Este método solicita continuamente al usuario que ingrese un número válido de horas hasta que se proporcione un entero válido.
            Utiliza el método `validador.validar_numeros_enteros` para validar la entrada.
            
            Returns:
                int: El número de horas como un entero.
        """
        while True:
            print("\n")
            horas = input("Ingrese el número de horas dedicadas a la actividad: ")
            if self.validador.validar_numeros_enteros(horas):
                return horas
            print("\n")
            print("El número de horas debe contener solo números.")
            
            
    def ingresar_bloqueo(self, comentario,descrip):
        """
        Solicita al usuario ingresar una opción y una descripción, validando ambos inputs.
        Args:
            comentario (str): Mensaje a mostrar al usuario para solicitar la opción.
            descrip (str): Mensaje a mostrar al usuario para solicitar la descripción.
        Returns:
            str: La descripción ingresada por el usuario si es válida, o "Sin bloqueos y/o problemas" si la opción ingresada no es "1".
        """
        
        while True:
            print("\n")
            print(comentario)
            opcion=input("Ingrese una opción: ")
            if self.validador.validar_numeros_enteros(opcion):
                break
            print("\n")
            print(" La opción debe contener solo números.")
            
        if opcion == "1":       
            while True:
                print("\n")
                descripcion = input(descrip)
                if self.validador.validar_texto(descripcion):
                    return descripcion
                print("\n")
                print("La descripción ingresada no es válida. Asegúrate de que contenga letras y espacios, intente nuevamente.")
        else:
            return "Sin bloqueos y/o problemas"
        
    def ingresar_fecha(self):
        """
            Solicita al usuario que ingrese una fecha en el formato 'aaaa-mm-dd' y la valida.
            Este método solicita continuamente al usuario que ingrese una fecha hasta que se 
            proporcione una fecha válida. La fecha se valida utilizando el método `validar_fecha` 
            del atributo `validador`. Si la fecha es válida, se retorna. De lo contrario, se 
            informa al usuario que la fecha no es válida y se le solicita que intente nuevamente.
            
            Returns:
                str: Una cadena de fecha válida en el formato 'aaaa-mm-dd'.
        """
        while True:
            print("\n")
            fecha = input("Ingrese la fecha de la actividad en formato aaaa-mm-dd: ")

            if self.validador.validar_fecha(fecha):
                return fecha
            print("\n")
            print("La fecha ingresada no es válida. Intente nuevamente.")
            
            
    def informe_actividad_anterior(self):
        """
            Imprime un informe de las actividades del día anterior.

            Este método imprime un informe formateado de las actividades registradas del día anterior.
            Si no hay actividades registradas, notificará al usuario que no hay registros disponibles.

            El informe incluye:
            - Un encabezado que indica el inicio del informe.
            - Un mensaje si no hay actividades registradas.
            - Una lista tabulada de actividades si hay alguna registrada.

            Returns:
                None
        """
        print("\n")
        print("****************************************************************************Informe actividades día anterior******************************************************************")
        print("\n")
        if len(self.registroActividad)==0:
            print("No hay registro de actividades del día anterior en el sistema")
        print(tabulate(self.registroActividad,headers='keys'))
        
        
    def informe_actividad_dia(self):
        """
            Imprime un informe de las actividades del día.

            Este método imprime un informe formateado de las actividades planificadas para el día.
            Si no hay actividades registradas, notifica al usuario que no hay actividades en el sistema.
            Las actividades se muestran en un formato tabulado.

            Returns:
                None
        """
        print("\n")
        print("****************************************************************************Informe actividades del día******************************************************************")
        if len(self.planeacionActividad)==0:
            print("No hay registro de actividades del día en el sistema")
        print(tabulate(self.planeacionActividad,headers='keys'))
        
        
    def informes(self):
        """
        Genera e imprime informes de actividades.
        Este método imprime un encabezado para el informe de actividades y luego llama a dos otros métodos:
        - `informe_actividad_anterior()`: Genera un informe de actividades anteriores.
        - `informe_actividad_dia()`: Genera un informe de actividades del día actual.
        """
        print("\n")
        print("****************************************************************************************************************************************************************************")
        print("****************************************************************************Informe de actividades**************************************************************************")
        print("****************************************************************************************************************************************************************************")

        self.informe_actividad_anterior()
        
        self.informe_actividad_dia()
        
                
    def informe_cedula(self):
        """
        Genera un informe basado en el número de cédula proporcionado.
        Este método solicita al usuario que ingrese un número de cédula y busca registros coincidentes
        en las listas `registroActividad` y `planeacionActividad`. Si se encuentran registros, se muestran
        en un formato tabulado. Si no se encuentran registros, se imprime un mensaje indicando que no hay
        registros con el número de cédula proporcionado.
        Returns:
        None
        """
        resultado=[]
        print("\n")
        while True:
            buscar=input("Ingrese el número de cédula a buscar: ")
            if self.validador.validar_numeros_enteros(buscar):
                break
            print("\n")
            
        for persona in self.registroActividad:
            if buscar in persona["identificación"]:
                resultado.append(persona)
                
        for persona in self.planeacionActividad:
            if buscar in persona["identificación"]:
                resultado.append(persona)
                
        if len(resultado)==0:
            print("No hay registros  con ese número de cédula en el sistema") 
            print("\n")
        
        print(tabulate(resultado,headers='keys'))
        
        
    def informe_rango_fecha(self):
        """
        Genera un informe de actividades dentro de un rango de fechas especificado.
        Este método solicita al usuario que ingrese una fecha de inicio y una fecha de fin en el formato 'aaaa-mm-dd'.
        Valida las fechas ingresadas y asegura que la fecha de inicio no sea mayor que la fecha de fin.
        Luego busca registros de actividades dentro del rango de fechas especificado en las listas `registroActividad` 
        y `planeacionActividad`, y muestra los resultados en un formato tabulado.
        Si no se encuentran registros dentro del rango de fechas especificado, notifica al usuario.
        Returns:
            None
        """
        resultado = []
        print("************************************************************************************************************************************************************************************") 
        print("****************************************************************************Informe actividades por rango de fecha******************************************************************")
        print("************************************************************************************************************************************************************************************")
        
        while True:
            fecha_inicio = input("Ingrese la fecha inicial del rango en formato aaaa-mm-dd: ").strip()
            fecha_fin = input("Ingrese la fecha final del rango en formato aaaa-mm-dd: ").strip()
            
            if self.validador.validar_fecha(fecha_inicio) and self.validador.validar_fecha(fecha_fin):
                fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
                fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
                
                if self.validador.validar_rango_fechas(fecha_inicio, fecha_fin):
                    break
                else:
                    print("La fecha inicial no puede ser mayor que la fecha final. Intente nuevamente.")
            else:
                print("Una o ambas fechas no son válidas. Intente nuevamente.")
        
        print("\nBuscando registros dentro del rango de fechas...")
        
        for persona in self.registroActividad:
            fecha_registro = datetime.strptime(str(persona["fecha"]), "%Y-%m-%d").date()
            if fecha_inicio <= fecha_registro <= fecha_fin:
                resultado.append(persona)
        
        for persona in self.planeacionActividad:
            fecha_registro = datetime.strptime(str(persona["fecha"]), "%Y-%m-%d").date()
            if fecha_inicio <= fecha_registro <= fecha_fin:
                resultado.append(persona)
        
        if len(resultado) == 0:
            print("No hay registros dentro del rango de fechas especificado.")
        else:
            print(tabulate(resultado, headers='keys'))
        
     


    def opcionSalida(self):
        """
        Muestra un menú para que el usuario elija entre el menú principal y el menú de informes.
        El método solicita continuamente al usuario que ingrese una opción hasta que se proporcione una opción válida.
        Las opciones válidas son:
        1. Menú Principal
        2. Menú de Informes
        Si el usuario ingresa "1", el método imprime un mensaje indicando que está saliendo al menú principal y rompe el bucle.
        Si el usuario ingresa "2", el método imprime un mensaje indicando que está saliendo al menú de informes y rompe el bucle.
        Si el usuario ingresa una opción no válida, el método solicita al usuario que ingrese una opción válida.
        Returns:
            str: La opción ingresada por el usuario.
        """
        while True:
            print("1.Menú Principal\n2.Menú de Informes")

            opcion=input("Ingrese una opción:")
            print("\n")
            if self.validador.validar_numeros_enteros(opcion):
                if opcion=="1":
                    print("Saliendo al menú principal...")
                    break
                elif opcion=="2":
                    print("saliendo al menú de informes...")
                    break
                else:
                    print("Ingrese una opción válida")
            else:
                print("Ingrese una opción válida")
        return opcion