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
            print("Conexion exitosa")
        except Exception as e:
            print(f"Conexión fallida: {e}")
    
    def getConnect(self):
        return self.conexion
    
    def close(self):
        self.conexion.close()
        
        
