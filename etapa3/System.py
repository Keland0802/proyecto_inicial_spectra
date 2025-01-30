from RegistroActividad import RegistroActividad
from PlaneacionActividad import PlaneacionActividad
from Report import Report
from lib.helpers import Validaciones
from Views import Views
from User import User

class System:
    def __init__(self):
        self.regist = RegistroActividad()
        self.plan = PlaneacionActividad()
        self.reports = Report()
        self.validador = Validaciones()
        self.views = Views()
        self.user = User()

    def start(self):
            self.init()
            
           
                

   
            
    
    def init(self):
            while True:

                option = self.views.getViewInit()

                if option == "1":
                    self.views.getViewRegistUser()
                    self.user.createUser()
                    
                elif option == "2":
                    while True:
                        self.views.getViewLogin()
                        self.id = self.user.enterId()
                        verifyUser = self.user.verifyUser(self.id)
                        if verifyUser:
                            self.user.setId(self.id)
                            self.options()
                        else:
                            print("Usuario no registrado")
                
                else:
                    print("Opción inválida. Intente nuevamente.")
            
            
    def options(self):
         while True:
        
            option = self.views.getViewMenu()

            if option == "1":
                self.views.getViewRegist()
                self.regist.registerActivity(self.user.getId())
                
            elif option == "2":
                self.views.getViewPlan()
                self.plan.planActivity(self.user.getId())
                
            elif option == "3":
                while True:
                    option_report =self.views.getViewOptReports()

                    if option_report in ["1", "2", "3", "4", "5", "6"]:
                        menu = self.reports.reports(option_report)
                        if menu in ["1", "6"]:
                            break
                        
                    else:
                        print("Por favor ingrese una opción válida")
                        
            elif option == "4":
                print("Saliendo del sistema.")
                self.init()
            else:
                print("Opción inválida. Intente nuevamente.")
