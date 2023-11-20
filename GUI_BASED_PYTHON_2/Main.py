import PySimpleGUI as sg
from PIL import ImageTk, Image
import pymysql
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

def open_admin_section(username):
    admin_layout = [
        [sg.Button('ADD BOOK DETAILS', key='-ADD-')],
        [sg.Button('DELETE BOOK', key='-DELETE-')],
        [sg.Button('VIEW BOOK LIST', key='-VIEW-')],
        [sg.Button('ISSUE BOOK TO STUDENT', key='-ISSUE-')],
        [sg.Button('RETURN BOOK', key='-RETURN-')]
    ]

    admin_window = sg.Window(f'Welcome Admin {username}', admin_layout)

    while True:
        event, values = admin_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-ADD-':
            addBook()

        if event == '-DELETE-':
            delete()

        if event == '-VIEW-':
            View()

        if event == '-ISSUE-':
            issueBook()

        if event == '-RETURN-':
            returnBook()

    admin_window.close()

def admin_login():
    admin_layout = [
        [sg.Text('Username'), sg.InputText(key='-USERNAME-')],
        [sg.Text('Password'), sg.InputText(password_char='*', key='-PASSWORD-')],
        [sg.Button('Login')]
    ]

    admin_window = sg.Window('Admin Login', admin_layout)

    while True:
        event, values = admin_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Login':
            username = values['-USERNAME-']
            password = values['-PASSWORD-']
            if username == "ram" and password == "1234":
                print(f"Admin {username} logged in successfully!")
                admin_window.close()
                open_admin_section(username)
            else:
                sg.popup("Invalid credentials")

    admin_window.close()

def teacher_login():
    teacher_layout = [
        [sg.Text('Username'), sg.InputText(key='-USERNAME-')],
        [sg.Text('Password'), sg.InputText(password_char='*', key='-PASSWORD-')],
        [sg.Button('Login')]
    ]

    teacher_window = sg.Window('Teacher Login', teacher_layout)

    while True:
        event, values = teacher_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Login':
            username = values['-USERNAME-']
            password = values['-PASSWORD-']
            if username == "ram" and password == "1234":
                print(f"Teacher {username} logged in successfully!")
                teacher_window.close()
                open_teacher_section(username)
            else:
                sg.popup("Invalid credentials")

    teacher_window.close()

def student_login():
    student_layout = [
        [sg.Text('Username'), sg.InputText(key='-USERNAME-')],
        [sg.Text('Password'), sg.InputText(password_char='*', key='-PASSWORD-')],
        [sg.Button('Login')]
    ]

    student_window = sg.Window('Student Login', student_layout)

    while True:
        event, values = student_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Login':
            username = values['-USERNAME-']
            password = values['-PASSWORD-']
            if username == "ram" and password == "1234":
                print(f"Student {username} logged in successfully!")
                student_window.close()
                open_student_section(username)
            else:
                sg.popup("Invalid credentials")

    student_window.close()

def open_teacher_section(username):
    teacher_layout = [
        [sg.Button('VIEW BOOK LIST', key='-VIEW-')],
        [sg.Button('RETURN BOOK', key='-RETURN-')],
        [sg.Button('VIEW RESEARCH PAPERS', key='-PAPERS-')]
    ]

    teacher_window = sg.Window(f'Welcome Teacher {username}', teacher_layout)

    while True:
        event, values = teacher_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-VIEW-':
            View()

        if event == '-RETURN-':
            returnBook()

        if event == '-PAPERS-':
            # Add code to view research papers here
            pass

    teacher_window.close()

def open_student_section(username):
    student_layout = [
        [sg.Button('VIEW BOOK LIST', key='-VIEW-')],
        [sg.Button('RETURN BOOK', key='-RETURN-')]
    ]

    student_window = sg.Window(f'Welcome {username}', student_layout)

    while True:
        event, values = student_window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-VIEW-':
            View()

        if event == '-RETURN-':
            returnBook()

    student_window.close()

layout = [
    [sg.Image(data='', key='-BG-')],
    [sg.Button('Admin', key='-ADMIN-'), sg.Button('Teacher', key='-TEACHER-'), sg.Button('Student', key='-STUDENT-')]
]

window = sg.Window('User Selection', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-ADMIN-':
        admin_login()

    if event == '-TEACHER-':
        teacher_login()

    if event == '-STUDENT-':
        student_login()

window.close()
