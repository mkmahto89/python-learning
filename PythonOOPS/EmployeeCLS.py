class Employee:
    def __init__(self,empid,name,age,salary):
        self.empid=empid
        self.name=name
        self.age=age
        self.salary=salary
        

class EmpDepartment:

    def __init__(self):
        self.EmpCollect={}

    def AddEmp(self,EmpObj):
        self.EmpCollect[EmpObj.empid]=EmpObj

    def RemoveEmp(self,empid):
        del self.EmpCollect[empid]    

    def DisplayEmp(self):
        for v in self.EmpCollect.values():# give emp object like e=Employee() so e.name,e.empid etc...
        #for v in self.EmpCollect.keys(): #give keys like 1,2
            #print(f"EmpID:{self.EmpCollect[v].empid} Name:{self.EmpCollect[v].name} Age:{self.EmpCollect[v].age} Salary:{self.EmpCollect[v].salary}") 
            print(f"EmpID:{v.empid} Name:{v.name} Age:{v.age} Salary:{v.salary}")     

"""
E1=Employee(1,"mohit",21,10000) 
E2=Employee(2,"Raj",22,20000)

EM=EmpDepartment()
EM.AddEmp(E1)
EM.AddEmp(E2)
EM.DisplayEmp()
#EM.RemoveEmp(1)
print("---")
EM.DisplayEmp()
"""
 