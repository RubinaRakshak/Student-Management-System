
import pymysql.cursors
con=pymysql.connect(host="localhost",user="root",database="school")



def addstudent():
    NAME=input("ENTER NAME:")
    CLASS=input("ENTER CLASS:")
    ROLL=input("ENTER ROLL.NO:")
    ADDRESS=input("ENTER ADDRESS:")
    PHONE=input("ENTER PHONE:")
    data=(NAME,CLASS,ROLL,ADDRESS,PHONE)
    sql='insert into student values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("DATA ENTERED SUCCESSFULLY")
    main()
def removestudent():
    CLASS=input("ENTER CLASS:")
    ROLL=input("ENTER ROLL.NO:")
    data=(CLASS,ROLL)
    sql='delete from student where CLASS =%s and ROL=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("DATA UPDATED")
    main()

def addteacher():
    NAME=input("TEACHER NAME:")
    POST=input("POST:")
    SALARY=input("SALARY:")
    ADDRESS=input("ADDRESS:")
    PHONE=input("PHONE:")
    ACCOUNTNUMBER=input("ACCOUNTNUMBER:")
    data=(NAME,POST,SALARY,ADDRESS,PHONE,ACCOUNTNUMBER)
    sql='insert into teacher values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("DATA ENTERED SUCCESSFULLY:")
    main()

def removeteacher():
      NAME=input("TEACHER NAME:")  
      ACCOUNTNUMBER=input("ACCOUNTNUMBER:")
      data=(NAME,ACCOUNTNUMBER)
      sql='delete from teacher where NAME = %s and ACCOUNTNUMBER=%s'
      c=con.cursor()
      c.execute(sql,data)
      con.commit()
      print("DATA UPDATED:")
      main()
def classattendance():
      DATE=input("DATE:")
      CLASS=input("CLASS:")
      ABSENT=input("NAME OF ABSENT STUDENTS:")
      data=(DATE,CLASS,ABSENT)
      sql='insert into classattendance values(%s,%s,%s)'
      c=con.cursor()
      c.execute(sql,data)
      con.commit()
      print("DATA UPDATED:")
      main()

def teacherattendance():
    DATE=input("DATE:")
    ABSENTTEACHER=input("ABSENT TEACHER:")
    PHONE=input("PHONE:")
    data=(DATE,ABSENTTEACHER,PHONE)
    sql='insert into teacherattendance values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    c=con.commit()
    print("DATA UPDATED:")
    main()

def submitfees():
    NAME=input("ENTER NAME:")
    CLASS=input("ENTER CLASS:")
    ROLL=input("ENTER ROLL.NO:")
    FEE=input("FEES:")
    DATE=input("DATE:")
    data=(NAME,CLASS,ROLL,FEE,DATE)
    sql='insert into fees values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("DATA ENTERED SUCCESSFULLY")
    main()

def paysalary():
    NAME=input("TEACHER NAME:")
    MONTH=input("MMONTH:")
    PAID=input("YES/NO:")
    data=(NAME,MONTH,PAID)
    sql='insert into salary values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("DATA ENTERD SUCCESSFULLY:")
    main()
 
    

def displayteacher():
    sql='select * from teacher'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("NAME:",i[0])
        print("POST:",i[1])
        print("SALARY:",i[2])
        print("ADDRESS:",i[3])
        print("PHONE:",i[4])
        print("ACCOUNTNO.:",i[5])
        print("----------------------------------------")
        main()

def main():
    print("""
    1.ADD STUDENT       2.REMOVE STUDENT
    3.ADD TEACHER       4.REMOVE TEACHER
    5.CLASS ATTENDANCE  6.TEACHER ATTENDANCE
    7.SUBMIT FEES       8.PAY SALARY
    9.DISPLAY CLASS     10.DISPLAY TEACHER
    """)

    choice = input("ENTER TASK NO.:")

    if(choice=='1'):
       addstudent()
    elif(choice=='2'):
       removestudent()
    elif(choice=='3'):
       addteacher()
    elif(choice=='4'):
       removeteacher()
    elif(choice=='5'):
       classattendance()
    elif(choice=='6'):
       teacherattendance()
    elif(choice=='7'):
       submitfees()
    elif(choice=='8'):
        paysalary()
    elif(choice=='9'):
        displayclass()
    elif(choice=='10'):
        displayteacher()
    else:
     print("WRONG CHOICE.....")
     
def password():
    p=input("PASSWORD:")
    if p=="rubina":
        main()
    else:
        print("WRONG PASSWORD")
        password()
password()
