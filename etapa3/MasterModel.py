from lib.conexion.conexion import Conexion

class MasterModel:
    def __init__(self):
        self.conexion = Conexion()
    
    def consult(self, query, params=None):
        """
        Executes a SQL query and returns the result.

        Parameters:
        query (str): The SQL query to be executed.
        params (tuple, optional): The parameters to be passed with the SQL query. Defaults to None.

        Returns:
        list: A list of tuples containing the rows returned by the query.
        None: If an error occurs during the execution of the query.
        """
        conn = self.conexion.getConnect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(f"Error in consult: {e}")
            return None
    
    def insert(self, query, params=None):
        """
        Executes an insert query on the database.

        Args:
            query (str): The SQL insert query to be executed.
            params (tuple, optional): The parameters to be used with the SQL query. Defaults to None.

        Returns:
            bool: True if the insert operation was successful, False otherwise.

        Raises:
            Exception: If an error occurs during the execution of the query.
        """
        conn = self.conexion.getConnect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error in insert: {e}")
            conn.rollback()
            return False
