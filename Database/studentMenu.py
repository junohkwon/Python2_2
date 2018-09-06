
#studentMenu.py

from userAcc import *
from DBconnection import *

def student_menu():
    
    menu_num = -1

    while(menu_num != '0'):
        print("\n\nWelcome %s"%user_acc.name)
        print("select student menu")
        print("1) Student Report")
        print("2) Check Course Qualification")
        print("3) View Time Table")
        print("0) Quit")
        menu_num = input("Enter : ")

        switcher = {
            '0' : quit_menu,
            '1' : print_stud_report,
            '2' : print_course_qual,
            '3' : print_time_table
        }

        selected_func = switcher.get(menu_num, print_wrong)

        selected_func()
    
    return


def print_stud_report():
    
    c = user_acc.conn.cursor()
    c.execute("SELECT * FROM student \
                WHERE ID = \"%s\" and name= \"%s\""%(user_acc.ID, user_acc.name))
    data = c.fetchone()

    print("You are a member of %s"%data[2])
    print("You have taken total %s credits\n"%data[3])
    print("Semester report\n")
		

    #수강한 학기, 연도 정보 모두 가져오기(distinct로 중복계산 방지)
    c.execute(''' FILL THIS QUERY''')

    data = c.fetchall()

    for year, semester in data :
        #year, semester 정보 cursor에서 받아오기


        #course_id, title, dept_name, credit, grade 정보를 cursor에서 받아온 후
        #위 표 모양대로 출력




    #cursor 닫기
    c.close()

    return

  
def print_course_qual():

    c = user_acc.conn.cursor()
    
    while(True):
        print("\nCheck Course Qualification")
        course_info = input("Enter course ID or Title (Enter q to go back) : ")

        if(course_info == "q" or course_info == "Q"):
            break

        #입력 받은 게 course_id인지 title인지 확인해야 한다


    #사용한 cursor 닫기
    c.close()        
    return

def print_time_table():
    c = user_acc.conn.cursor()

    #user가 수강한 최근학기 year, semester 정보 받아오기

    print("\nTime Table\n")
    print("%10s\t%40s\t%15s\t%10s\t%10s"%("course_id","title","day","start_time","end_time"))

    #user가 수강한 year, semester중 가장 최근 year, semester를 이용하여
    #time table 만들기


    #사용한 cursor 닫기
    c.close()
    
    return

def quit_menu():
    
    global user_acc #global 변수 write할 때는 명시 필요
   
    user_acc.conn.close()
    #user가 사용하던 connection 반납
    #return_connect(user_acc.conn)

    #del user_acc

    return

def print_wrong():
    print("\nwrong menu number.")
    return

def gp_to_float(grade):
    return {
        "A+" : 4.3,
        "A " : 4,
        "A-" : 3.7,
        "B+" : 3.3,
        "B " : 3,
        "B-" : 2.7,
        "C+" : 2.3,
        "C " : 2,
        "C-" : 1.7,
        "D+" : 1.3,
        "D " : 1,
        "D-" : 0.7,
        "F" : 0
    }[grade]
