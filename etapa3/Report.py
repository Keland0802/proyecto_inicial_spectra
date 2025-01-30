from datetime import datetime
from tabulate import tabulate
from MasterModel import MasterModel
from lib.helpers import Validaciones

class Report:
    def __init__(self):
        self.model = MasterModel()
        self.validador = Validaciones()
        self.headersPlan = ["id planeacion", "número de documento", "actividad que realizará", "descripción de la actividad", "número de proyecto", "horas dedicadas", "fecha de planeación", "comentario o bloqueo"]
        self.headersRegist =  ["id registro", "número de documento", "actividad realizada", "descripcion de actividad", "número de proyecto", "horas dedicadas", "fecha de realización", "comentario o bloqueo"]



    def optionExit(self):
          
            while True:
                print("1.Menú Principal\n2.Menú de Informes")

                option=input("Ingrese una opción:")
                print("\n")
                if self.validador.validar_numeros_enteros(option):
                    if option=="1":
                        print("Saliendo al menú principal...")
                        break
                    elif option=="2":
                        print("saliendo al menú de informes...")
                        break
                    else:
                        print("Ingrese una opción válida")
                else:
                    print("Ingrese una opción válida")
            return option
        
        
    def reports(self, option):
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
            print ("Opción inválida. Intente nuevamente.")
        
        return self.optionExit()
   
        
    def getReportRegister(self):
        
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
                
        regist=self.model.consult(query)
        print(tabulate(regist,headers=self.headersRegist, tablefmt="grid"))
        
        
    def getReportPlan(self):
        print("\n")
        print("****************************************************************************INFORME DE ACTIVIDADES DEL DIA******************************************************************")
        query = """SELECT 
                p.id_planeacion,
                p.cedula_usu,
                ta.nombre_tipo_actividad AS actividad,
                p.descripcion_act,
                p.num_proyecto,
                p.horas,
                p.fecha,
                p.comentario
                
            FROM 
                planeacion_actividades p
            LEFT JOIN 
                tipo_actividades ta 
            ON 
                p.actividad = ta.id_tipo_actividad"""
            
        plan=self.model.consult(query)
        print(tabulate(plan,headers=self.headersPlan,tablefmt="grid"))

    
    def getReports(self):
        print("\n")
        print("****************************************************************************************************************************************************************************")
        print("****************************************************************************INFORME DE ACTIVIDADES**************************************************************************")
        print("****************************************************************************************************************************************************************************")

        self.getReportRegister()
        
        self.getReportPlan()

        
    def getReportId(self):
        while True:
            search=input("Ingrese el número de cédula a buscar: ")
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

        print(tabulate(regist,headers=self.headersRegist, tablefmt="grid"))

        print("\n")
        query2 = """SELECT 
                    p.id_planeacion,
                    p.cedula_usu,
                    ta.nombre_tipo_actividad AS actividad,
                    p.descripcion_act,
                    p.num_proyecto,
                    p.horas,
                    p.fecha,
                    p.comentario
                    
                FROM 
                    planeacion_actividades p
                LEFT JOIN 
                    tipo_actividades ta 
                ON 
                    p.actividad = ta.id_tipo_actividad
                WHERE p.cedula_usu=%s"""
        plan = self.model.consult(query2, params)
        print(tabulate(plan,headers=self.headersPlan,tablefmt="grid"))
    
        

        
    def getReportDate(self):
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
                print("Una o ambas fechas no son válidas. Intente nuevamente.")
        
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
        print(tabulate(regist,headers=self.headersRegist, tablefmt="grid"))
        print("\n")
        
        query2 = """SELECT 
                        p.id_planeacion,
                        p.cedula_usu,
                        ta.nombre_tipo_actividad AS actividad,
                        p.descripcion_act,
                        p.num_proyecto,
                        p.horas,
                        p.fecha,
                        p.comentario
                        
                    FROM 
                        planeacion_actividades p
                    LEFT JOIN 
                        tipo_actividades ta 
                    ON 
                        p.actividad = ta.id_tipo_actividad
                    WHERE fecha BETWEEN %s AND %s"""
        plan = self.model.consult(query2, params)
        print(tabulate(plan,headers=self.headersPlan,tablefmt="grid"))
        print("\n")
        

       
        