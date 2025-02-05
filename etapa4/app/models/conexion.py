import os
from dotenv import load_dotenv
from psycopg2 import connect

load_dotenv()

class Conexion:
    def __init__(self):
        self.setConnect()
        self.connection()
    
    def setConnect(self):
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_pass = os.getenv('DB_PASS')
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        
    def connection(self):
        connectionString = "dbname='%s' user='%s' password='%s' host='%s' port='%s'" % (
            self.db_name, self.db_user, self.db_pass, self.db_host, self.db_port)

        try:
            self.conexion = connect(connectionString)
            
        except Exception as e:
            print(f"Conexión fallida: {e}")
    
    def getConnect(self):
        return self.conexion
    
    def close(self):
        self.conexion.close()
        
    
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
        conn = self.getConnect()
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
        conn = self.getConnect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error in insert: {e}")
            conn.rollback()
            return False

        
