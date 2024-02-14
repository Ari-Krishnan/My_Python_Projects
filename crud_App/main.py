import mysql.connector
from tabulate import tabulate

cont = mysql.connector.connect(
    host = 'localhost:3306',
    user = 'root',
    password = '12345678',
    database = 'crudapp'
)

curs = cont.cursor()

def Insert(name,age,city):
    sql = "insert into Students (name, age, city) values(%s, %s, %s)"
    val = (name, age, city)
    curs.execute(sql, val)
    cont.commit()
    print("Data Inserted Successfully ")

def Update(id, name, age, city):
    sql = "Update students set name = %s, age = %s, city = %s where id = %s"
    val = (name, age, city, id)
    curs.execute(sql, val)
    cont.commit()
    print("Data Updated Successfully ")

def Select():
    sql = "Select id, name, age, city from Students"
    curs.execute(sql)
    res = curs.fetchall()
    print(tabulate(res, headers =["Id", "Name", "Age", "City"]))

def Delete(id):
    sql = "Delete from students where id = %s"
    val = (id,)
    curs.execute(sql, val)
    cont.commit()
    print("Data Deteleted Successfully")

while True:
    print("1.Insert")
    print("2.Update")
    print("3.Select")
    print("4.Delete")
    print("5.Exit")
    choice = int(input("Enter your Choice : "))

    if choice == 1:
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City Name : ")
        Insert(name, age, city)
    elif choice == 2:
        id = input("Enter id : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City Name : ")
        Update(id, name, age, city)
    elif choice == 3:
        Select()
    elif choice == 4:
        id = int(input("Enter id : "))
        Delete(id)
    elif choice == 5:
        break
    else:
        print('Wrong chioce , Please Try again')