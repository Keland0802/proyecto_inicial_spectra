from datetime import datetime
from tabulate import tabulate
import re

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validar_rango_fechas(fecha_inicio, fecha_fin):
    if fecha_inicio > fecha_fin:
        return False
    return True

def validar_numeros_enteros(numero):
    if re.match("^[0-9]+$", numero):
        return True
    return False

def validar_texto(texto):
    if re.match("^[a-zA-Z0-9\s]+$", texto.strip()):
        return True
    return False

def validar_nombres(nombre):
    if nombre.strip() and re.match("^[a-zA-Z\s]+$", nombre.strip()):
        return True
    return False

registro_usu=True
registros = []
planeacion = []



# class gestionTiempo():
#     def __init__(self, nombre, identificacion):
#         self.resgistros = []
#         self.planeacion = []
#         self.nombre = nombre
#         self.identificacion = identificacion
        
#     def planeacionRegistro(self, nombre, identificacion):
#         pass
    
#     def registroActividad(self, nombre, identificacion):
#         self.planeacionRegistro(nombre, identificacion)
#         pass

def planeacionRegistro(nombre, identificacion):
    
    # a=gestionTiempo(nombre, identificacion)
    # planeacion.append(a.planeacionRegistro(nombre, identificacion))
    """
    
    Registra la actividad diaria de un usuario, incluyendo bloqueos y problemas, 
    o detalles de la actividad a realizar.
    Args:
        nombre (str): Nombre del usuario.
        identificacion (str): Identificación del usuario.
    Solicita al usuario que indique si tiene bloqueos o problemas para el desarrollo 
    de la actividad del día. Si los tiene, se le pide una descripción de los mismos 
    y se registra la información. Si no los tiene, se le solicita el tipo de actividad 
    que realizará, una descripción de la actividad, el número del proyecto, las horas 
    dedicadas y la fecha, y se registra la información.
    """
    print("\n")

    print("****************************************************************************************************************************************************************************")
    print("***************************************************************************Indique su actividad del día*********************************************************************")
    print("****************************************************************************************************************************************************************************")
    print("\n")

    while True:
            print("""Bloqueos y/o problemas para el desarrollo de la actividad del día?
            1.Si
            Cualquier otro número para No
            """)
                
            comentario=input("Ingrese una opción: ")
            if validar_numeros_enteros(comentario):
                break
            else:
                print("La opción debe contener solo números.")

                print("\n")

               
    
    
    
    print("\n")

    descripcion="Sin bloqueos y/o problemas"
    if comentario=="1":
        while True:
            descripcion=input("Describa los bloqueos y/o problemas con la actividad: ")

            if validar_texto(descripcion):
                break
            else:
                print("La descripción debe contener solo letras, números y espacios.")

            print("\n")
    
        planeacion.append({
                "nombre": nombre,
                "identificación": identificacion,
                "comentario":descripcion

        })
        print(tabulate(planeacion,headers='keys'))

        print("Registro realizado")
        
        print("\n")
    else:
        while True:
            print("""Tipo de actividad que realizará:
                    1.Soporte
                    2.Backend
                    3.Frontend
                """)
            actividad=input("Ingrese una opción:")
            if validar_numeros_enteros(actividad):
                if actividad in ["1", "2", "3"]:
                    if actividad=="1":
                        tipo_act="Soporte"
                        break

                    elif actividad=="2":
                        tipo_act="Backend"
                        break
                    elif actividad=="3":
                        tipo_act="Frontend"
                        break
                    else:
                        print("Por favor ingrese una opcion válida")
                else:
                    print("\n")

                    print("Por favor ingrese una opción válida.")
                    
                    
            else:
                print("Por favor ingrese una opción válida.")
                print("\n")


        while True:
            descripción_actividad=input("Descripción de la actividad que realizará: ")
            if validar_texto(descripción_actividad):
                        break
            else:
                print("La descripcion ingresada no es válido. Asegúrate de que solo contenga letras y espacios.")
        print("\n")
        
        while True:
            num_proyecto=input("Ingrese número del proyecto: ")
            if validar_numeros_enteros(num_proyecto):
                break
            else:
                print("El número de proyecto debe contener solo números.")

    
        print("\n")
        while True:
            horas=input("Ingrese las horas dedicadas a la actividad: ")
            if validar_numeros_enteros(horas):
                break
            else:
                print("Las horas deben contener solo números.")

        print("\n")
        
        fecha=datetime.now().date()

        planeacion.append({

            "nombre": nombre,
            "identificación": identificacion,
            "tipo de actividad": tipo_act,
            "descripción de actividad": descripción_actividad,
            "numero de proyecto": num_proyecto,
            "horas":horas,
            "fecha":fecha,
            "comentario":descripcion

        })
        print("Registro completado")


while registro_usu:
    print("****************************************************************************************************************************************************************************")
    print("***************************************************************Bienvenido al sistema de registro de actividades*************************************************************")
    print("****************************************************************************************************************************************************************************")
    while True:
        nombre = input("Por favor ingrese su nombre completo: ")
        if validar_nombres(nombre):
            break
        else:
            print("El nombre ingresado no es válido. Asegúrate de que solo contenga letras y espacios.")
            
    while True:
        identificacion = input("Por favor ingrese su número de documento: ")
        if validar_numeros_enteros(identificacion):
            break
        else:
            print("La identificación debe contener solo números.")
    identificado=True
    while identificado:
        print("****************************************************************************************************************************************************************************")
        print("********************************************************************************menú****************************************************************************************")
        print("****************************************************************************************************************************************************************************")
        print("""MENÚ PRINCIPAL:

            1.Registrar actividad del dia anterior\n
            2.Planear actividad del dia\n
            3.Generar informe\n
            4.Salir
            """)
        opcion=input("SELECCIONE UNA OPCIÓN DEL MENÚ: ")
        match opcion:
            case "1":
                print("\n")
                print("****************************************************************************************************************************************************************************")
                print("***************************************************************Registre su actividad realizada el dia de ayer***************************************************************")
                print("****************************************************************************************************************************************************************************")
               
                print("\n")
                while True:
                    print("""Tipo de actividad que realizó:
                            1.Soporte
                            2.Backend
                            3.Frontend
                        """)
                    actividad=input("Ingrese una opción:")
                    if validar_numeros_enteros(actividad):
                        if actividad in ["1", "2", "3"]:
                            if actividad=="1":
                                tipo_act="Soporte"
                                break

                            elif actividad=="2":
                                tipo_act="Backend"
                                break
                            elif actividad=="3":
                                tipo_act="Frontend"
                                break
                            else:
                                print("Por favor ingrese una opcion válida")
                        else:
                            print("\n")

                            print("Por favor ingrese una opción válida.")
                            
                            
                    else:
                        print("Por favor ingrese una opción válida.")
                        print("\n")

                   
                
                     
                while True:
                    descripción_actividad=input("Descripción de la actividad que realizó: ")
                    if validar_texto(descripción_actividad):
                        break
                    else:
                        print("La descripcion ingresada no es válido. Asegúrate de que solo contenga letras y espacios.")
                print("\n")
                
                
                while True:
                    num_proyecto=input("Ingrese número del proyecto: ")
                    if validar_numeros_enteros(num_proyecto):
                        break
                    else:
                        print("El número de proyecto debe contener solo números.")

               
                print("\n")
                
                while True:
                    horas=input("Ingrese las horas dedicadas a la actividad: ")
                    if validar_numeros_enteros(horas):
                        break
                    else:
                        print("Las horas deben contener solo números.")

                print("\n")
                while True:
                    fecha = input("Ingrese la fecha de la actividad en formato aaaa-mm-dd: ")
                    if validar_fecha(fecha):
                        break
                    else:
                        print("La fecha ingresada no es válida. Intente nuevamente.")
                print("\n")
               
               

                while True:
                        
                    print("""Bloqueos y/o problemas para el desarrollo de la actividad?
                            1.Si
                            Cualquier otro número para No
                        """)
                
                    comentario=input("Ingrese una opción: ")
                    if validar_numeros_enteros(comentario):
                        break
                    else:
                        print("La opción debe contener solo números.")

                print("\n")

                descripcion="Sin bloqueos y/o problemas"
                if comentario=="1":
                    while True:
                        descripcion=input("Describa los bloqueos y/o problemas con la actividad: ")

                        if validar_texto(descripcion):
                            break
                        else:
                            print("La descripción debe contener solo letras, números y espacios.")

                        print("\n")



                registros.append({
                    "nombre": nombre,
                    "identificación": identificacion,
                    "tipo de actividad": tipo_act,
                    "descripción de actividad": descripción_actividad,
                    "numero de proyecto": num_proyecto,
                    "horas":horas,
                    "fecha":fecha,
                    "comentario":descripcion
                }) 
                print("Registro completado")




            case "2":
                planeacionRegistro(nombre, identificacion)
                # print("\n")

                # print("****************************************************************************************************************************************************************************")
                # print("***************************************************************************Indique su actividad del día*********************************************************************")
                # print("****************************************************************************************************************************************************************************")
                # print("\n")


                
                # print("""Bloqueos y/o problemas para el desarrollo de la actividad del día?
                #         1.Si
                #         Cualquier otro número para No
                #     """)
                
                # comentario=int(input("Ingrese una opción: "))
                # print("\n")

                # descripcion="Sin bloqueos y/o problemas"
                # if comentario==1:
                #     descripcion=input("Describa los Bloqueos y/o problemas con la actividad: ")
                #     planeacion.append({
                #             "nombre": nombre,
                #             "identificación": identificacion,
                #             "comentario":descripcion

                #     })
                #     print(tabulate(planeacion,headers='keys'))

                #     print("Registro realizado")
                    
                #     print("\n")
                # else:
                #     while True:
                #         print("""Tipo de actividad que realizará:
                #                 1.Soporte
                #                 2.Backend
                #                 3.Frontend
                #             """)
                #         actividad=int(input("Ingrese una opción:"))
                #         print("\n")

                        
                       
                #         if actividad==1:
                #             tipo_act="Soporte"
                #             break

                #         elif actividad==2:
                #             tipo_act="Backend"
                #             break
                #         elif actividad==3:
                #             tipo_act="Frontend"
                #             break
                #         else:
                #             print("Por favor ingrese una opcion válida")


                #     descripción_actividad=input("Descripción de la actividad que realizará: ")
                #     print("\n")

                #     num_proyecto=input("Ingrese número del proyecto: ")
                #     print("\n")
                #     horas=input("Ingrese las horas a dedicar a la actividad: ")
                #     print("\n")
                #     fecha=datetime.now().date()

                #     planeacion.append({
                #         "nombre": nombre,
                #         "identificación": identificacion,
                #         "tipo de actividad": tipo_act,
                #         "descripción de actividad": descripción_actividad,
                #         "numero de proyecto": num_proyecto,
                #         "horas":horas,
                #         "fecha":fecha,
                #         "comentario":descripcion

                #     })
                #     print("Registro completado")


            case "3":
                
                print("\n")
                print("****************************************************************************************************************************************************************************")
                print("***********************************************************************************Informes*********************************************************************************")
                print("****************************************************************************************************************************************************************************")
            
                print("\n")
                while True:

                    print("""Elija una opción:
                            1.Ver registros de actividades dia anterior
                            2.Ver registros de actividad del día
                            3. Ver ambos registros
                            4. Ver registros por numero de cédula
                            5. Ver registros por rango de fecha de actividad
                    
                    """)
                    opcion_informes=input("SELECCIONE UNA OPCIÓN DEL MENÚ: ")

                    match opcion_informes:
                        case "1":
                            print("****************************************************************************Informe actividades día anterior******************************************************************")

                            if len(registros)==0:
                                print("No hay registro de actividades del día anterior en el sistema")
                            print(tabulate(registros,headers='keys'))
                            print("\n")
                            print("""1.Menú principal
                                
                            """)
                            while True:
                                opcion=input("Ingrese una opción:")
                                if validar_numeros_enteros(opcion):
                                    
                                    if opcion=="1":
                                        print("Saliendo al menú...")
                                        break
                                    else:
                                        print("Ingrese una opción válida")
                                else:
                                    print("Ingrese una opción válida")
                            
                        case "2":
                            print("****************************************************************************Informe actividades del día******************************************************************")

                            if len(planeacion)==0:
                                print("No hay registros en el sistema")
                            print(tabulate(planeacion,headers='keys'))
                            print("\n")
                            print("""1.Menú principal
                                
                            """)
                            while True:
                                opcion=input("Ingrese una opción:")
                                if validar_numeros_enteros(opcion):
                                    
                                    if opcion=="1":
                                        print("Saliendo al menú...")
                                        break
                                    else:
                                        print("Ingrese una opción válida")
                                else:
                                    print("Ingrese una opción válida")

                        case "3":
                            print("****************************************************************************Informe actividades día anterior******************************************************************")

                            if len(registros)==0:
                                print("No hay registros de tareas de ayer en el sistema")
                            


                            print(tabulate(registros,headers='keys'))
                            print("\n")
                            print("****************************************************************************Informe actividades del día******************************************************************")
                            
                            if len(planeacion)==0:
                                print("No hay registros de tareas del dia en el sistema")

                            print(tabulate(planeacion,headers='keys'))
                            print("\n")

                            print("""1.Menú principal
                                
                            """)
                            while True:
                                opcion=input("Ingrese una opción:")
                                if validar_numeros_enteros(opcion):
                                    
                                    if opcion=="1":
                                        print("Saliendo ...")
                                        break
                                    else:
                                        print("Ingrese una opción válida")
                                else:
                                    print("Ingrese una opción válida")

                        case "4":
                            resultado=[]
                            print("\n")
                            while True:
                                buscar=input("Ingrese el número de cédula a buscar: ")
                                if validar_numeros_enteros(buscar):
                                    break
                                print("\n")
                                
                            for persona in registros:
                                if buscar in persona["identificación"]:
                                    resultado.append(persona)
                                    
                            for persona in planeacion:
                                if buscar in persona["identificación"]:
                                    resultado.append(persona)
                                    
                            if len(resultado)==0:
                                print("No hay registros en el sistema") 
                                print("\n")
                            
                            print(tabulate(resultado,headers='keys'))
                            print("\n")
                            
                            print("""1.Menú principal
                                
                            """)
                            while True:
                                opcion=input("Ingrese una opción:")
                                if validar_numeros_enteros(opcion):
                                    
                                    if opcion=="1":
                                        print("Saliendo...")
                                        break
                                    else:
                                        print("Ingrese una opción válida")
                                else:
                                    print("Ingrese una opción válida")
                        
                        case "5":
                                resultado = []
                                print("\n")
                                
                                print("****************************************************************************Informe actividades por fecha******************************************************************")
                                
                                while True:
                                    fecha_inicio = input("Ingrese la fecha inicial del rango en formato aaaa-mm-dd: ").strip()
                                    fecha_fin = input("Ingrese la fecha final del rango en formato aaaa-mm-dd: ").strip()
                                    
                                    if validar_fecha(fecha_inicio) and validar_fecha(fecha_fin):
                                        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
                                        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
                                        
                                        if validar_rango_fechas(fecha_inicio, fecha_fin):
                                            break
                                        else:
                                            print("La fecha inicial no puede ser mayor que la fecha final. Intente nuevamente.")
                                    else:
                                        print("Una o ambas fechas no son válidas. Intente nuevamente.")
                                
                                print("\nBuscando registros dentro del rango de fechas...")
                                
                                for persona in registros:
                                    fecha_registro = datetime.strptime(str(persona["fecha"]), "%Y-%m-%d").date()
                                    if fecha_inicio <= fecha_registro <= fecha_fin:
                                        resultado.append(persona)
                                
                                for persona in planeacion:
                                    fecha_registro = datetime.strptime(str(persona["fecha"]), "%Y-%m-%d").date()
                                    if fecha_inicio <= fecha_registro <= fecha_fin:
                                        resultado.append(persona)
                                
                                if len(resultado) == 0:
                                    print("No hay registros dentro del rango de fechas especificado.")
                                else:
                                    print(tabulate(resultado, headers='keys'))
                                
                                print("\n")
                                print("""1.Menú principal
                                    
                                """)
                                while True:
                                    opcion=input("Ingrese una opción:")
                                    if validar_numeros_enteros(opcion):
                                        
                                        if opcion=="1":
                                            print("Saliendo...")
                                            break
                                        else:
                                            print("Ingrese una opción válida")
                                    else:
                                        print("Ingrese una opción válida")           
                        case _:
                            print("\n")
                            print("Ingrese una opción válida...")
                            


            case "4":
                print("Saliendo...")
                identificado=False
                break

            case _:
                print("\n")
                print("Ingrese una opción válida...")



