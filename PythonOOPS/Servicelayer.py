class ServiceLayer:
    def __init__(self,userrepo):
        self.userrepo=userrepo


    def create(self,user):
        if len(user)<0:
            return
        return self.userpo.create(user)        

            