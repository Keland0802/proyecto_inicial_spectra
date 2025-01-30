from datetime import datetime
from tabulate import tabulate
from MasterModel import MasterModel
from lib.helpers import Validaciones

class Report:
    def __init__(self):
        self.model = MasterModel()
        self.validador = Validaciones()
        self.headersPlan = ["id planeación", "número de documento", "actividad que realizará", "descripción de la actividad", "número de proyecto", "horas dedicadas", "fecha de planeación", "comentario o bloqueo"]
        self.headersRegist =  ["id registro", "número de documento", "actividad realizada", "descripción de actividad", "número de proyecto", "horas dedicadas", "fecha de realización", "comentario o bloqueo"]

    def optionExit(self):
        """
        Displays a menu with options to exit to the main menu or the reports menu.
        
        The method continuously prompts the user to enter an option until a valid option is provided.
        Valid options are:
        1. Menú Principal
        2. Menú de Informes
        
        If the user selects option 1, a message indicating exit to the main menu is displayed.
        If the user selects option 2, a message indicating exit to the reports menu is displayed.
        If an invalid option is entered, the user is prompted to enter a valid option.
        
        Returns:
            str: The selected option ("1" or "2").
        """
        while True:
            print("1. Menú Principal\n2. Menú de Informes")
            option = input("Ingrese una opción: ")
            print("\n")
            if self.validador.validar_numeros_enteros(option):
                if option == "1":
                    print("Saliendo al menú principal...")
                    break
                elif option == "2":
                    print("Saliendo al menú de informes...")
                    break
                else:
                    print("Ingrese una opción válida")
            else:
                print("Ingrese una opción válida")
        return option

    def reports(self, option):
        """
        Generates various types of reports based on the provided option.
        Parameters:
        option (str): A string representing the report option to generate. 
                      Valid options are:
                      "1" - Generate a register report.
                      "2" - Generate a plan report.
                      "3" - Generate multiple reports.
                      "4" - Generate a report by ID.
                      "5" - Generate a report by date.
                      "6" - Return the option.
        Returns:
        str: The provided option if it is "6".
        None: If an invalid option is provided or after generating a report.
        """
        if option == "1":
            self.getReportRegister()
        elif option == "2":
            self.getReportPlan()
        elif option == "3":
            self.getReports()
        elif option == "4":
            self.getReportId()
        elif option == "5":
            self.getReportDate()
        elif option == "6":
            return option
        else:
            print("Opción inválida. Intente nuevamente.")
        
        return self.optionExit()

    def getReportRegister(self):
        """
        Generates and prints a report of activities from the previous day.

        This method retrieves data from the 'registro_actividades' table, joins it with the 'tipo_actividades' table to get the activity names, 
        and prints the results in a formatted table.

        The report includes the following columns:
        - id_registro: The ID of the activity record.
        - cedula_usu: The user's ID.
        - actividad: The name of the activity type.
        - descripcion_act: The description of the activity.
        - num_proyecto: The project number.
        - horas: The number of hours spent on the activity.
        - fecha: The date of the activity.
        - comentario: Additional comments about the activity.

        The results are printed using the 'tabulate' library with a grid format.
        """
        print("\n")
        print("****************************************************************************INFORME ACTIVIDADES DÍA ANTERIOR******************************************************************")
        query = """SELECT 
                r.id_registro,
                r.cedula_usu,
                ta.nombre_tipo_actividad AS actividad,
                r.descripcion_act,
                r.num_proyecto,
                r.horas,
                r.fecha,
                r.comentario
            FROM 
                registro_actividades r
            JOIN 
                tipo_actividades ta 
            ON 
                r.actividad = ta.id_tipo_actividad"""
        regist = self.model.consult(query)
        print(tabulate(regist, headers=self.headersRegist, tablefmt="grid"))

    def getReportPlan(self):
        """
        Generates and prints a report of daily activities.

        This method retrieves data from the 'planeación_actividades' table, joins it with the 'tipo_actividades' table to get the activity names, 
        and prints the results in a formatted table.

        The report includes the following columns:
        - id_planeación: The ID of the planning activity.
        - cedula_usu: The user's ID.
        - actividad: The name of the activity type.
        - descripcion_act: The description of the activity.
        - num_proyecto: The project number.
        - horas: The number of hours spent.
        - fecha: The date of the activity.
        - comentario: Any additional comments.

        The results are printed using the 'tabulate' library with a grid format.
        """
        print("\n")
        print("****************************************************************************INFORME DE ACTIVIDADES DEL DÍA******************************************************************")
        query = """SELECT 
                p.id_planeación,
                p.cedula_usu,
                ta.nombre_tipo_actividad AS actividad,
                p.descripcion_act,
                p.num_proyecto,
                p.horas,
                p.fecha,
                p.comentario
            FROM 
                planeación_actividades p
            LEFT JOIN 
                tipo_actividades ta 
            ON 
                p.actividad = ta.id_tipo_actividad"""
        plan = self.model.consult(query)
        print(tabulate(plan, headers=self.headersPlan, tablefmt="grid"))

    def getReports(self):
        """
        Generates and prints the activity report.

        This method prints a formatted header for the activity report and then calls
        two other methods to generate specific sections of the report:
        - getReportRegister: Generates the report register section.
        - getReportPlan: Generates the report plan section.
        """
        print("\n")
        print("****************************************************************************************************************************************************************************")
        print("****************************************************************************INFORME DE ACTIVIDADES**************************************************************************")
        print("****************************************************************************************************************************************************************************")
        self.getReportRegister()
        self.getReportPlan()

    def getReportId(self):
        """
        Retrieves and displays report data based on user input.

        This method prompts the user to input a "cedula" (identification number),
        validates the input, and then retrieves and displays two sets of data:
        - Registered activities associated with the given "cedula".
        - Planned activities associated with the given "cedula".

        The data is fetched from the database and displayed in a tabulated format.

        Returns:
            None
        """
        while True:
            search = input("Ingrese el número de cédula a buscar: ")
            if self.validador.validar_numeros_enteros(search):
                break
            print("\n")
        query = """SELECT 
                    r.id_registro,
                    r.cedula_usu,
                    ta.nombre_tipo_actividad AS actividad,
                    r.descripcion_act,
                    r.num_proyecto,
                    r.horas,
                    r.fecha,
                    r.comentario
                FROM 
                    registro_actividades r
                LEFT JOIN 
                    tipo_actividades ta 
                ON 
                    r.actividad = ta.id_tipo_actividad
                WHERE r.cedula_usu=%s"""
        params = (search,)
        print("\n")
        regist = self.model.consult(query, params)
        print(tabulate(regist, headers=self.headersRegist, tablefmt="grid"))
        print("\n")
        query2 = """SELECT 
                    p.id_planeación,
                    p.cedula_usu,
                    ta.nombre_tipo_actividad AS actividad,
                    p.descripcion_act,
                    p.num_proyecto,
                    p.horas,
                    p.fecha,
                    p.comentario
                FROM 
                    planeación_actividades p
                LEFT JOIN 
                    tipo_actividades ta 
                ON 
                    p.actividad = ta.id_tipo_actividad
                WHERE p.cedula_usu=%s"""
        plan = self.model.consult(query2, params)
        print(tabulate(plan, headers=self.headersPlan, tablefmt="grid"))

    def getReportDate(self):
        """
        Generates a report of activities within a specified date range.

        This method prompts the user to input a start date and an end date in the format 'yyyy-mm-dd'.
        It validates the input dates and ensures the start date is not greater than the end date.
        Once valid dates are provided, it queries the database for records within the specified date range
        and prints the results in a tabulated format.

        The method performs the following steps:
        1. Prompts the user to input the start and end dates.
        2. Validates the input dates.
        3. Ensures the start date is not greater than the end date.
        4. Queries the database for activity records within the specified date range.
        5. Prints the results of the queries in a tabulated format.

        Raises:
            ValueError: If the input dates are not in the correct format or if the start date is greater than the end date.

        Returns:
            None
        """
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
                print("El formato de una o ambas fechas no es válido. Intente nuevamente.")
        print("\nBuscando registros dentro del rango de fechas...")
        query = """SELECT 
                        r.id_registro,
                        r.cedula_usu,
                        ta.nombre_tipo_actividad AS actividad,
                        r.descripcion_act,
                        r.num_proyecto,
                        r.horas,
                        r.fecha,
                        r.comentario
                    FROM 
                        registro_actividades r
                    LEFT JOIN 
                        tipo_actividades ta 
                    ON 
                        r.actividad = ta.id_tipo_actividad
                    WHERE fecha BETWEEN %s AND %s"""
        params = (fecha_inicio, fecha_fin)
        regist = self.model.consult(query, params)
        print(tabulate(regist, headers=self.headersRegist, tablefmt="grid"))
        print("\n")
        query2 = """SELECT 
                        p.id_planeación,
                        p.cedula_usu,
                        ta.nombre_tipo_actividad AS actividad,
                        p.descripcion_act,
                        p.num_proyecto,
                        p.horas,
                        p.fecha,
                        p.comentario
                    FROM 
                        planeación_actividades p
                    LEFT JOIN 
                        tipo_actividades ta 
                    ON 
                        p.actividad = ta.id_tipo_actividad
                    WHERE fecha BETWEEN %s AND %s"""
        plan = self.model.consult(query2, params)
        print(tabulate(plan, headers=self.headersPlan, tablefmt="grid"))
        print("\n")
