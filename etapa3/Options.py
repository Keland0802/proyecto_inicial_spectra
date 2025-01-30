
class Options:
    def optionInit(self, option):
        if option == "1":
            self.views.getViewRegistUser()
            self.user.createUser()
        elif option == "2":
            self.views.getViewLogin()
            self.name = self.user.setName()
            self.id = self.user.setId()
        