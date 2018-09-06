
#login.py

from userAcc import *
from DBconnection import *
from studentMenu import *
from instructorMenu import *


def login():

    print("Welcome")
    
    while(user_acc.conn is None):
        
        print("Please sign in")

        ID = input("%-10s:"%"ID")
        name = input("%-10s:"%"Name")

        auth(ID,name)
    
    switcher = {
        0 : student_menu,
        1 : instructor_menu
    }

    role_menu = switcher.get(user_acc.role)

    role_menu()



def auth(ID,name):

    #입력 받은 ID, name이 student DB에 존재하는지 확인
    user_connect = connectDB()

        
    #입력 받은 ID, name이 instructor DB에 존재하는지 확인
    
