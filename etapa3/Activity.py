from lib.helpers import Validaciones
from MasterModel import MasterModel

class Activity:
    def __init__(self):
        self.validador = Validaciones()
        
    def selectTypeAct(self):
        """
        Prompts the user to select an activity type from a list of available types.

        This method retrieves activity types from the database, displays them to the user,
        and prompts the user to select one by entering the corresponding number. If the user
        enters an invalid option, they are prompted to try again.

        Returns:
            str: The ID of the selected activity type.
        """
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
        """
        Prompts the user to enter a description and validates the input.

        This method repeatedly prompts the user to enter a description until a valid input is provided.
        A valid description contains only letters and spaces.

        Args:
            message (str): The message to display when prompting the user for input.

        Returns:
            str: The valid description entered by the user.
        """
        while True:
            print("\n")
            description = input(message)
            if self.validador.validar_texto(description):
                return description
            print("\n")
            print("La descripción ingresada no es válida. Asegúrate de que solo contenga letras y espacios, intente nuevamente.")

    def enter_num_proyect(self):
        """
        Prompts the user to enter a project number or continue without entering one.

        The method displays a menu with two options:
        1. Enter a project number.
        2. Continue without entering a project number.

        If the user chooses to enter a project number, they are prompted to input the number.
        The input is validated to ensure it contains only numbers. If the input is valid, the
        project number is returned. Otherwise, the user is prompted to enter the number again.

        If the user chooses to continue without entering a project number, the method returns None.

        Returns:
            str or None: The project number entered by the user, or None if the user chooses to
            continue without entering a project number.
        """
        while True:
            print("\n")
            print("1. Ingresar número de proyecto\n2. Continuar sin ingresar número de proyecto")
            option = input("Ingrese una opción: ")
            if self.validador.validar_numeros_enteros(option):
                break
            print("\n")
            print("La opción debe contener solo números.")
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
        """
        Prompts the user to enter the number of hours dedicated to an activity.
        
        Continuously asks the user for input until a valid integer is provided.
        Uses the `validador.validar_numeros_enteros` method to validate the input.
        
        Returns:
            int: The number of hours entered by the user.
        """
        while True:
            print("\n")
            hours = input("Ingrese el número de horas dedicadas a la actividad: ")
            if self.validador.validar_numeros_enteros(hours):
                return hours
            print("\n")
            print("El número de horas debe contener solo números.")
            
    def enter_date(self):
        """
        Prompts the user to enter a date in the format 'aaaa-mm-dd' and validates it.

        This method continuously prompts the user to enter a date until a valid date
        is provided. The date is validated using the `validador.validar_fecha` method.

        Returns:
            str: A valid date string in the format 'aaaa-mm-dd'.
        """
        while True:
            print("\n")
            date = input("Ingrese la fecha de la actividad en formato aaaa-mm-dd: ")
            if self.validador.validar_fecha(date):
                return date
            print("\n")
            print("El formato de fecha ingresado no es válido. Intente nuevamente.")
            
    def enter_blockade(self, comment, message_blockade):
        """
        Handles the process of entering a blockade description based on user input.
        Args:
            comment (str): The comment to be printed before asking for an option.
            message_blockade (str): The message to be printed when asking for a blockade description.
        Returns:
            str: The description of the blockade if valid, or "Sin bloqueos y/o problemas" if the option is not "1".
        """
        while True:
            print(comment)
            option = input("Ingrese una opción: ")
            if self.validador.validar_numeros_enteros(option):
                break
            print("\n")
            print("La opción debe contener solo números.")
            
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
