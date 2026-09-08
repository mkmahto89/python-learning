
from abc import ABC,abstractmethod
class Database(ABC):
    
    @abstractmethod
    def connect(self):
        pass

class SQL(Database):
    def connect(self):
        print("connecting to SQL...")

class MySQL(Database):
    def connect(self):
        print("connecting to MySQL...")

class Oracle(Database):
    def connect(self):
        print("connecting to Oracle...")

class MongoDB(Database):
    def connect(self):
        print("connecting to MongoDB...")

class DBFactory:
    @staticmethod
    def GetFactoryObj(DBObj):
        if DBObj=="SQL":
            return SQL()
        elif DBObj=="MySQL":
            return MySQL()
        elif DBObj=="Oracle":
            return Oracle()
        elif DBObj=="MongoDB":
            return MongoDB()

class ConnectDB:
    def __init__(self,DBobject):
        self.DBObject=DBobject

    def ExecuteMethod(self):
        self.DBObject.connect()    


Obj=DBFactory.GetFactoryObj("SQL")
C=ConnectDB(Obj)
C.ExecuteMethod()





