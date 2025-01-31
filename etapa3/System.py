from RegistroActividad import RegistroActividad
from PlaneacionActividad import PlaneacionActividad
from Report import Report
from lib.helpers import Validaciones
from Views import Views
from User import User

class System:
    def __init__(self):
        self.registro = RegistroActividad()
        self.plan = PlaneacionActividad()
        self.reportes = Report()
        self.validador = Validaciones()
        self.vistas = Views()
        self.usuario = User()

    def start(self):
        self.init()
            
    def init(self):
        """
        Initializes the system and provides the main menu for user interaction.
        This method runs an infinite loop that presents the user with options to either
        register a new user or log in with an existing user ID. Depending on the user's
        choice, it either initiates the user registration process or the login process.
        - If the user chooses to register, it calls the methods to display the registration
          view and create a new user.
        - If the user chooses to log in, it enters a nested loop where it prompts the user
          to log in with an existing ID. If the ID is verified, it sets the user ID and
          calls the options method. If the ID is not verified, it prompts the user to try
          again or register.
        The loop continues until a valid option is selected.
        Returns:
            None
        """
        while True:
            opcion = self.vistas.getViewInit()

            if opcion == "1":
                self.vistas.getViewRegistUser()
                self.usuario.createUser()
                    
            elif opcion == "2":
                while True:
                    self.vistas.getViewLogin()
                    self.id = self.usuario.enterId()
                    verificarUsuario = self.usuario.verifyUser(self.id)
                    if verificarUsuario:
                        self.usuario.setId(self.id)
                        self.options()
                    else:
                        print("Usuario no registrado. Por favor regístrese o intente nuevamente.")
                        break
                
            else:
                print("Opción inválida. Intente nuevamente.")
            
    def options(self):
        """
        Displays a menu of options to the user and performs actions based on the selected option.
        Options:
            1. Register an activity.
            2. Plan an activity.
            3. Generate reports.
                - Sub-options for reports:
                    1. Report type 1
                    2. Report type 2
                    3. Report type 3
                    4. Report type 4
                    5. Report type 5
                    6. Exit report menu
            4. Exit the system and reinitialize.
        The method will continue to prompt the user for input until a valid option is selected.
        """
        while True:
            opcion = self.vistas.getViewMenu()

            if opcion == "1":
                self.vistas.getViewRegist()
                self.registro.registerActivity(self.usuario.getId())
                
            elif opcion == "2":
                self.vistas.getViewPlan()
                self.plan.planActivity(self.usuario.getId())
                
            elif opcion == "3":
                while True:
                    opcion_reporte = self.vistas.getViewOptReports()

                    if opcion_reporte in ["1", "2", "3", "4", "5", "6"]:
                        menu = self.reportes.reports(opcion_reporte)
                        if menu in ["1", "6"]:
                            break
                        
                    else:
                        print("Por favor ingrese una opción válida")
                        
            elif opcion == "4":
                print("Saliendo del sistema.")
                self.init()
            else:
                print("Opción inválida. Intente nuevamente.")
