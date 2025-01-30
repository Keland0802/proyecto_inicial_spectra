import re
from datetime import datetime

class Validaciones:
    def __init__(self): 
        pass

    @staticmethod
    def validar_fecha(fecha):
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def validar_rango_fechas(fecha_inicio, fecha_fin):
        if fecha_inicio > fecha_fin:
            return False
        return True

    @staticmethod
    def validar_numeros_enteros(numero):
        if re.match("^[0-9]*$", numero):
            return True
        return False

    @staticmethod
    def validar_texto(texto):
        if re.match("^[a-zA-Z0-9\sáéíóúÁÉÍÓÚ]+$", texto.strip()):
            return True
        return False

    @staticmethod
    def validar_nombres(nombre):
        if nombre.strip() and re.match("^[a-zA-Z\sáéíóúÁÉÍÓÚ'-]+$", nombre.strip()):
            return True
        return False
    
    @staticmethod
    def validar_identificacion(id):
        if isinstance(id, str) and re.match("^[0-9]+$", id):
            return True
        return False