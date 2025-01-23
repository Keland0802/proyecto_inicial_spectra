import re
from datetime import datetime

class Validaciones:
    def _init(self):  # Cambiado a __init_
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
        if re.match("^[0-9]+$", numero):
            return True
        return False

    @staticmethod
    def validar_texto(texto):
        if re.match("^[a-zA-Z0-9\s]+$", texto.strip()):
            return True
        return False

    @staticmethod
    def validar_nombres(nombre):
        if nombre.strip() and re.match("^[a-zA-Z\s]+$", nombre.strip()):
            return True
        return False