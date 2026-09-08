""""
from sklearn.linear_model import LinearRegression

X=[[1],[2],[3],[4],[5]]

Y=[20,30,70,90,110]

model=LinearRegression()
model.fit(X,Y)
p=model.predict([[2]])
#exp=input('enter no of years of expierence')
#print(model.predict([[int(exp)]]))
print("Predicted salary:", p[0])

import pandas as pd

data={
"EmployeeName":["Mohit","Sanmati","Karthik","Ganesh","Rohit","Kanu","Gopi","Raj"],
"Age":[21,22,23,33,33,45,23,33],
"Salary":[1000,2000,3000,4000,5000,6000,7000,8000],
"Location":["Canada","India","India","USA","India","Canada","India","India"]
}
df=pd.DataFrame(data)
#print(df) #full data frame
#print(df.head()) #top 5 rows
#print(df.tail()) #last 5 rows from bottom
#print(df.iloc[0]) # first row
#print(df.iloc[4]) # 5 th row from top

#getting max salary employee data from every location
#print(df)
#print(df.groupby("Location")["Salary"].max())
#print(df.groupby("Location")["Salary"].sum())
#print(df.groupby("Location")["Salary"].nlargest(2))
#print(df)
#print(df.loc[2:])
"""

import pandas as pd
dt={
"Name":["Mohit","Raj","Karthik"],
"Age":[21,22,23],
"Salary":[1000,10000,2000],
"Dept":["A","A","B"] 
}

df=pd.DataFrame(dt)

#print(df.iloc[1])

#print(df.groupby("Dept")["Salary"].max())

import csv
with open("MyPython.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerows(dt)


