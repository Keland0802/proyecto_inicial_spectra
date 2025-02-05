from models.conexion import Conexion

class User:
    def __init__(self):
        self.con=Conexion()
    
    
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
            user = self.con.consult(query)
            if user:
                return user[0]
            else:
                return False
        except Exception:
            print("Error al buscar registros del usuario.")
            return None
        
    
    def createUser(self, name, id):
        
      
            query = f"INSERT INTO usuarios (nombre, cedula) VALUES ('{name}', '{id}')"
            
            newUser = self.con.insert(query)
            if newUser:
                return True
            else:
                return False