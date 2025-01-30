from lib.helpers import Validaciones
from MasterModel import MasterModel

class User:
    def __init__(self):
        self.name = None
        self.id = None
        self.validator = Validaciones()
        
    def enterName(self):
        """
        Prompts the user to enter their full name and validates it.

        Continuously asks the user to input their full name until a valid name is provided.
        A valid name contains only letters and spaces.

        Returns:
            str: The validated full name entered by the user.
        """
        while True:
            name = input("Ingrese su nombre completo: ")
            if self.validator.validar_nombres(name):
                return name
            else:
                print("Nombre no válido. Intente nuevamente, recuerde que el nombre solo debe contener letras y espacios.")  
                
    def enterId(self):
        """
        Prompts the user to enter their identification number and validates it.
        The method continuously prompts the user to enter their identification number until a valid one is provided.
        A valid identification number must:
        - Pass the custom validation defined in `self.validator.validar_identificacion(id)`.
        - Contain only numeric characters.
        - Be at least 6 digits long.
        - Be no more than 10 digits long.
        Returns:
            str: A valid identification number entered by the user.
        """
        while True:
            id = input("Ingrese su número de identificación: ")
            
            if self.validator.validar_identificacion(id):
                if len(id) < 6:
                    print("Identificación no válida. Debe tener mínimo 6 dígitos.")
                elif len(id) > 10:
                    print("Identificación no válida. Debe tener máximo 10 dígitos.")
                else:
                    return id
            else:
                print("Identificación no válida. Intente nuevamente, recuerde que el número de identificación debe contener solo números.")
                
    def setName(self, name):
        self.name = name
    
    def setId(self, id):
        self.id = id       
    
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def createUser(self):
        """
        Creates a new user by prompting for their name and ID, verifying if the user already exists,
        and inserting the new user into the database if they do not already exist.
        If the user already exists, a message is printed prompting the user to log in.
        If the user is successfully registered, a success message is printed.
        If there is an error during the insertion, an error message is printed.
        Returns:
            None
        """
        self.name = self.enterName()
        self.id = self.enterId()
        user = self.verifyUser(self.id)
        if user:
            print("Usuario ya registrado en el sistema, por favor inicie sesión con su número de identificación.")
            return
        else:
            query = f"INSERT INTO usuarios (nombre, cedula) VALUES ('{self.name}', '{self.id}')"
            
            newUser = MasterModel().insert(query)
            if newUser:
                print("Usuario registrado con éxito, por favor inicie sesión con su número de identificación.")
            else:
                print("Error al insertar usuario.")
        
    def verifyUser(self, id):
        """
        Verifies if a user exists in the database by their ID.

        Args:
            id (int): The ID of the user to verify.

        Returns:
            bool: True if the user exists, False if the user does not exist.
            None: If there is an error during the database query.

        Raises:
            Exception: If there is an error during the database query.
        """
        query = f"SELECT * FROM usuarios WHERE cedula = {id}"
        try:
            user = MasterModel().consult(query)
            if user:
                return True
            else:
                return False
        except Exception:
            print("Error al buscar registros del usuario.")
            return None
