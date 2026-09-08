
from abc import ABC,abstractmethod

class ConnectDB(ABC):
    @abstractmethod
    def DatabaseConnectivity(self,EmpDBValues):
        pass   

class SQL(ConnectDB):

    def DatabaseConnectivity(self,EmpDBValues):
        print("connecting to SQL...")
        print(f"empid:{EmpDBValues.empid} name:{EmpDBValues.name} age:{EmpDBValues.age} salary:{EmpDBValues.salary} saved in SQL Database")

class MySQL(ConnectDB):

    def DatabaseConnectivity(self,EmpDBValues):
        print("connecting to MySQL")
        print(f"empid:{EmpDBValues.empid} name:{EmpDBValues.name} age:{EmpDBValues.age} salary:{EmpDBValues.salary} saved in MySQL Database")

class MongoDB(ConnectDB):

    def DatabaseConnectivity(self,EmpDBValues):
        print("connecting to MongoDB...")
        print(f"empid:{EmpDBValues.empid} name:{EmpDBValues.name} age:{EmpDBValues.age} salary:{EmpDBValues.salary}  saved in MongoDB Database")

class Oracle(ConnectDB):

    def DatabaseConnectivity(self,EmpDBValues):
        print("Connecting to Oracle...")
        print(f"empid:{EmpDBValues.empid} name:{EmpDBValues.name} age:{EmpDBValues.age} salary:{EmpDBValues.salary}  saved in Oracle Database")

class DatabaseCollection:
    DBs={
        "SQL":SQL,
        "MySQL":MySQL,
        "MongoDB":MongoDB,
        "Oracle":Oracle
    }

class DatabaseObject:
    @staticmethod
    def GetDatabaseObject(DBObj):
        return DatabaseCollection.DBs[DBObj]()     

class ApplicationAccessDB:
    def __init__(self,DObj):
        self.DObj=DObj
    def Connect(self,EmpDBValues):
        self.DObj.DatabaseConnectivity(EmpDBValues)

"""
M=DatabaseObject.GetDatabaseObject("MongoDB")
A=ApplicationAccessDB(M)
A.Connect()
"""






