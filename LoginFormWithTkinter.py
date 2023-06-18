
import sqlite3 as sql
conn = sql.connect('apple.db') #connect sql with database

#Create a Table
conn.execute(""" CREATE TABLE IF NOT EXISTS student_record(
student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL
)
""")

#INSERT DATA

conn.execute("INSERT INTO student_record (username,password) VALUES ('Saqib', 'admin123')")
conn.execute("INSERT INTO student_record (username,password) VALUES ('Taha', 'admin123')")
conn.execute("INSERT INTO student_record (username,password) VALUES ('Moon', 'admin123')")
conn.execute("INSERT INTO student_record (username,password) VALUES ('Love Kumar', 'admin123')")

#To add data in the fields
conn.commit()
#To close the database
conn.close()



from tkinter import *
win = Tk()
win.title("Login Form")
win.geometry('400x400')

def click():
    uname = username.get()
    pwd = password.get()

    if uname == "" or pwd == "":
        message.set("Fields should be filled")

    else:
        #to connect with database
        conn = sql.connect('student.db')
        curosr = conn.execute("SELECT * FROM student_record WHERE username = '%s' and password = '%s'"%(uname, pwd))

    if curosr.fetchone():
        message.set("Login Successful")
    else:
        message.set("Username or Password is incorrect")
username = StringVar()
password = StringVar()
message = StringVar()


Label(win, text="Username", bg="#32a864", fg="white", font=("Arial", 12, "bold")).place(x=20,y =40)
Entry(win, textvariable=username, bg="#32a864", fg="white", font=("Arial", 12, "bold")).place(x=120,y =40)

Label(win, text="Password", bg="#32a864", fg="white", font=("Arial", 12, "bold")).place(x=20,y =80)
Entry(win, textvariable=password,show="*", bg="#32a864", fg="white", font=("Arial", 12, "bold")).place(x=120,y =80)

Button(win, text="Login", bg='#bf3075', fg="white", font=("Arial",16, "bold"),command=click).place(x=125, y=180)
Label(win, textvariable=message, bg="#32a864", fg="white", font=("Arial", 12, "bold")).place(x=80,y =120)
win.mainloop()
