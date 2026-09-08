
from EmployeeCLS import Employee,EmpDepartment
from DatabaseConnectCLS import DatabaseObject,ApplicationAccessDB

def main():
    #initialize employee object 
    E1=Employee(1,"mohit",21,10000)
    #initailize dep for operation
    D=EmpDepartment()
    D.AddEmp(E1)
    D.DisplayEmp()

    #connect to MongoDB fo saving data 
    M=DatabaseObject.GetDatabaseObject("MongoDB")
    A=ApplicationAccessDB(M)
    A.Connect(E1)



main()