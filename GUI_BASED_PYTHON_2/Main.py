mport PySimpleGUI as sg
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

