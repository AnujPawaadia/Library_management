from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password="1234", database=mydatabase)
cur = con.cursor()

def admin_click():
    admin_login()

def teacher_click():
    teacher_login()

def student_click():
    student_login()

def open_admin_section(username):
    admin_section = Toplevel(root)
    admin_section.title(f"Welcome Admin {username}")
    admin_section.geometry("800x600")

    # Add a frame with sky blue background
    admin_frame = Frame(admin_section, bg="skyblue")
    admin_frame.place(relwidth=1, relheight=1)

    btn1 = Button(admin_frame, text="ADD BOOK DETAILS", bg='black', fg='white', command=addBook)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(admin_frame, text="DELETE BOOK", bg='black', fg='white', command=delete)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn3 = Button(admin_frame, text="VIEW BOOK LIST", bg='black', fg='white', command=View)
    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    btn4 = Button(admin_frame, text="ISSUE BOOK TO STUDENT", bg='black', fg='white', command=issueBook)
    btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    btn5 = Button(admin_frame, text="RETURN BOOK", bg='black', fg='white', command=returnBook)
    btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

def admin_login():
    login_window = Toplevel(root)
    login_window.title("Admin Login")
    login_window.geometry("300x200")

    Label(login_window, text="Username").pack()
    admin_username = Entry(login_window)
    admin_username.pack()

    Label(login_window, text="Password").pack()
    admin_password = Entry(login_window, show="*")
    admin_password.pack()

    admin_credentials = {
        "ram": "1234",
    }

    def check_credentials():
        username = admin_username.get()
        password = admin_password.get()
        if username in admin_credentials and admin_credentials[username] == password:
            print(f"Admin {username} logged in successfully!")
            login_window.destroy()
            open_admin_section(username)  # Open admin section with username
        else:
            print("Invalid credentials")

    Button(login_window, text="Login", command=check_credentials).pack()

def teacher_login():
    login_window = Toplevel(root)
    login_window.title("Teacher Login")
    login_window.geometry("300x200")

    Label(login_window, text="Username").pack()
    teacher_username = Entry(login_window)
    teacher_username.pack()

    Label(login_window, text="Password").pack()
    teacher_password = Entry(login_window, show="*")
    teacher_password.pack()

    teacher_credentials = {
        "ram": "1234",
        "teacher2": "teacherpass2",
        "teacher3": "teacherpass3",
    }

    def check_credentials():
        username = teacher_username.get()
        password = teacher_password.get()
        if username in teacher_credentials and teacher_credentials[username] == password:
            print(f"Teacher {username} logged in successfully!")
            login_window.destroy()
            open_teacher_section(username)  # Open teacher section with username
        else:
            print("Invalid credentials")

    Button(login_window, text="Login", command=check_credentials).pack()

def student_login():
    login_window = Toplevel(root)
    login_window.title("Student Login")
    login_window.geometry("300x200")

    Label(login_window, text="Username").pack()
    student_username = Entry(login_window)
    student_username.pack()

    Label(login_window, text="Password").pack()
    student_password = Entry(login_window, show="*")
    student_password.pack()

    student_credentials = {
        "ram": "1234",
        "shyam": "123",
        "student3": "studentpass3"
    }

    def check_credentials():
        username = student_username.get()
        password = student_password.get()
        if username in student_credentials and student_credentials[username] == password:
            print(f"Student {username} logged in successfully!")
            login_window.destroy()
            open_student_section(username)  # Open student section with username
        else:
            print("Invalid credentials")

    Button(login_window, text="Login", command=check_credentials).pack()
