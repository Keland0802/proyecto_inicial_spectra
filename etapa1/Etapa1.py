from datetime import datetime
from tabulate import tabulate


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


    
    print("""Bloqueos y/o problemas para el desarrollo de la actividad del día?
            1.Si
            Cualquier otro número para No
        """)
    
    comentario=int(input("Ingrese una opción: "))
    print("\n")

    descripcion="Sin bloqueos y/o problemas"
    if comentario==1:
        descripcion=input("Describa los Bloqueos y/o problemas con la actividad: ")
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
            actividad=int(input("Ingrese una opción:"))
            print("\n")
            
            
            if actividad==1:
                tipo_act="Soporte"
                break

            elif actividad==2:
                tipo_act="Backend"
                break
            elif actividad==3:
                tipo_act="Frontend"
                break
            else:
                print("Por favor ingrese una opcion válida")


        descripción_actividad=input("Descripción de la actividad que realizará: ")
        print("\n")

        num_proyecto=input("Ingrese número del proyecto: ")
        
        print("\n")
        horas=input("Ingrese las horas a dedicar a la actividad: ")
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
    nombre=input("Por favor ingrese su nombre completo: ")
    identificacion=input("Por favor ingrese su número de documento: ")
    identificado=True
    while identificado:
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
                    actividad=int(input("Ingrese una opción:"))
                    print("\n")

                   
                    if actividad==1:
                        tipo_act="Soporte"
                        break

                    elif actividad==2:
                        tipo_act="Backend"
                        break
                    elif actividad==3:
                        tipo_act="Frontend"
                        break
                    else:
                        print("Por favor ingrese una opcion válida")
                     
                descripción_actividad=input("Descripción de la actividad que realizó: ")
                print("\n")

                num_proyecto=input("Ingrese número del proyecto: ")
                print("\n")
                horas=input("Ingrese las horas dedicadas a la actividad: ")
                print("\n")
                fecha=input("Ingrese la fecha de la actividad en formato aaaa-mm-dd: ")
                print("\n")

                print("""Bloqueos y/o problemas para el desarrollo de la actividad?
                        1.Si
                        Cualquier otro número para No
                    """)
                
                comentario=int(input("Ingrese una opción: "))
                print("\n")

                descripcion="Sin bloqueos y/o problemas"
                if comentario==1:
                    descripcion=input("Describa los bloqueos y/o problemas con la actividad: ")
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

                print("""Elija una opción:
                        1.Ver registros de actividades dia anterior
                        2.Ver registros de activida del día
                        3. Ver ambos registros
                        4. Ver registros por numero de cédula
                        5. Ver registros por fecha de actividad
                
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
                        opcion=int(input("Ingrese una opción:"))
                        if opcion==1:
                            print("Saliendo al menú...")
                        
                    case "2":
                        print("****************************************************************************Informe actividades del día******************************************************************")

                        if len(planeacion)==0:
                            print("No hay registros en el sistema")
                        print(tabulate(planeacion,headers='keys'))
                        print("\n")
                        print("""1.Menú principal
                            
                        """)
                        opcion=int(input("Ingrese una opción:"))
                        if opcion==1:
                            print("Saliendo al menú...")

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
                        opcion=int(input("Ingrese una opción:"))
                        if opcion==1:
                            print("Saliendo al menú...")

                    case "4":
                        resultado=[]
                        print("\n")
                        buscar=input("Ingrese el número de cédula a buscar: ")
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
                    
                    case "5":
                        resultado=[]
                        print("\n")
                        fecha_inicio=datetime.strptime(input("Ingrese la fecha inicial del rango en formato aaaa-mm-dd: "), "%Y-%m-%d").date()
                        fecha_fin=datetime.strptime(input("Ingrese la fecha final del rango en formato aaaa-mm-dd: "), "%Y-%m-%d").date()
                        print("\n")
                        for persona in registros:
                            fecha_registro=datetime.strptime(str(persona["fecha"]), "%Y-%m-%d").date()
                            if fecha_inicio<=fecha_registro<=fecha_fin:
                                resultado.append(persona)
                            
                        for persona in planeacion:
                            fecha_registro=datetime.strptime(str(persona["fecha"]), "%Y-%m-%d").date()
                            if fecha_inicio<=fecha_registro<=fecha_fin:
                                resultado.append(persona)
                        
                        if len(resultado)==0:
                            print("No hay registros en el sistema") 
                            print("\n")
                        
                        print(tabulate(resultado,headers='keys'))
                        



            case "4":
                print("Saliendo...")
                identificado=False
                break

            case _:
                print("\n")
                print("Ingrese una opción válida...")



