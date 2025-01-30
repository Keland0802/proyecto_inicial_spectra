from lib.conexion.conexion import Conexion

class MasterModel:
    def __init__(self):
        self.conexion = Conexion()
    
    def consult(self, query, params=None):
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
