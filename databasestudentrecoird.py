# import tkinter as tk
# from tkinter import *
# from tkinter.font import *
#
# class CALCULATOR :
#     def __init__(self):
#         self.window = Tk()
#         self.window.title("taha's projects")
#         self.window.geometry("400x600")
#         self.window_background ='#fbfbfb'
#         self.btn_color_primary = '#f5f5f5'
#         self.btn_color_secondry1  ='#d5e6ff'
#         self.btn_color_secondry2 = 'blue'
#
#         self.window.configure(bg =self.window_background)
#         for i in range (0,4):
#             self.window.columnconfigure(i,weight=1)
#
#         for i in range(0,6):
#             self.window.rowconfigure(i, weight=1)
#
#         self.font_display  =Font(family='consolas',size = 50,weight='bold')
#         self.font_digit    =Font(family="calibri",size=25,weight='bold')
#
#         #label display
#         self.label_display =Label(self.window,text='0',relief=GROOVE, font=self.font_display,anchor='e',bg='white')
#
#         #button display
#         self.btn0 = Button(self.window,text='0',relief=GROOVE,font=self.font_digit,bg=self.btn_color_primary)
#         self.btn1 = Button(self.window, text='1', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btn2 = Button(self.window, text='2', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btn3 = Button(self.window, text='3', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btn4 = Button(self.window, text='4', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btn5 = Button(self.window, text='5', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btn6 = Button(self.window, text='6', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btn7 = Button(self.window, text='7', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btn8 = Button(self.window, text='8', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btn9 = Button(self.window, text='9', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btnA = Button(self.window, text='A', relief=GROOVE, font=self.font_digit, bg=self.btn_color_secondry2)
#         self.btnC = Button(self.window, text='C', relief=GROOVE, font=self.font_digit, bg=self.btn_color_secondry2)
#         self.btnADD = Button(self.window, text='+', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btnSUB = Button(self.window, text='-', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btnMUL = Button(self.window, text='*', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btndiv = Button(self.window, text='/', relief=GROOVE, font=self.font_digit, bg=self.btn_color_primary)
#         self.btnEQ = Button(self.window, text='=', relief=GROOVE, font=self.font_digit, bg=self.btn_color_secondry1)
#         self.btndecimal = Button(self.window, text='.', relief=GROOVE, font=self.font_digit, bg=self.btn_color_secondry1)
#
#         self.label_display.grid(row=0,column=0,columnspan=4,sticky='NSEW',padx=5,pady=15)
#         self.btn0.grid(row = 5,column =0,padx=5,pady = 5,sticky='NSEW',columnspan=2)
#         self.btn1.grid(row=4, column=0, padx=5, pady=5, sticky='NSEW')
#         self.btn2.grid(row=4, column=1, padx=5, pady=5, sticky='NSEW')
#         self.btn3.grid(row=4, column=2, padx=5, pady=5, sticky='NSEW')
#         self.btn4.grid(row=3, column=0, padx=5, pady=5, sticky='NSEW')
#         self.btn5.grid(row=3, column=1, padx=5, pady=5, sticky='NSEW')
#         self.btn6.grid(row=3, column=2, padx=5, pady=5, sticky='NSEW')
#         self.btn7.grid(row=2, column=0, padx=5, pady=5, sticky='NSEW')
#         self.btn8.grid(row=2, column=1, padx=5, pady=5, sticky='NSEW')
#         self.btn9.grid(row=2, column=2, padx=5, pady=5, sticky='NSEW')
#         self.btnA.grid(row=2, column=3, padx=5, pady=5, sticky='NSEW')
#         self.btnC.grid(row=3, column=3, padx=5, pady=5, sticky='NSEW')
#         self.btnADD.grid(row=1, column=0, padx=5, pady=5, sticky='NSEW')
#         self.btnSUB.grid(row=1, column=1, padx=5, pady=5, sticky='NSEW')
#         self.btndiv.grid(row=1, column=2, padx=5, pady=5, sticky='NSEW')
#         self.btnMUL.grid(row=1, column=3, padx=5, pady=5, sticky='NSEW')
#         self.btnEQ.grid(row=4, column=3, padx=5, pady=5, sticky='NSEW',rowspan=2)
#         self.btndecimal.grid(column=2,row=5,sticky='NSEW',padx=5,pady=5)
#
#         self.btn0.bind('<Button-1>',self.on_click)
#         self.btn1.bind('<Button-1>', self.on_click)
#         self.btn2.bind('<Button-1>', self.on_click)
#         self.btn3.bind('<Button-1>', self.on_click)
#         self.btn4.bind('<Button-1>', self.on_click)
#         self.btn5.bind('<Button-1>', self.on_click)
#         self.btn6.bind('<Button-1>', self.on_click)
#         self.btn7.bind('<Button-1>', self.on_click)
#         self.btn8.bind('<Button-1>', self.on_click)
#         self.btn9.bind('<Button-1>', self.on_click)
#         self.btnA.bind('<Button-1>', self.on_click)
#         self.btnC.bind('<Button-1>', self.on_click)
#         self.btnEQ.bind('<Button-1>', self.on_click)
#         self.btnMUL.bind('<Button-1>', self.on_click)
#         self.btndiv.bind('<Button-1>', self.on_click)
#         self.btnADD.bind('<Button-1>', self.on_click)
#         self.btnSUB.bind('<Button-1>', self.on_click)
#         self.btndecimal.bind('<Button-1>', self.on_click)
#
#
#     def on_click(self,event):
#         btn_text = event.widget['text']
#         display_text = self.label_display['text']
#
#         if btn_text in '0123456789':
#             if display_text =='0':
#                 self.label_display['text'] = btn_text
#             else:
#                 self.label_display['text'] = display_text+ btn_text
#
#         if btn_text == '.':
#             if not '.' in display_text:
#                 self.label_display['text'] = display_text + '.'
#
#         if btn_text in ('+', '-', '*', '/'):
#             if display_text[-1].isdigit():
#                 self.label_display['text'] = display_text + btn_text
#         if btn_text == '=':
#             if not display_text[-1].isdigit():
#
#                 self.label_display['text'] = 'ERROR'
#             else:
#                 try:
#                     self.label_display['text'] = str(eval(display_text))
#                 except ZeroDivisionError:
#                     self.label_display['text'] = 'ERROR'
#
#         if btn_text == 'A':
#             self.label_display['text'] = '0'
#
#         if btn_text == 'C':
#             if len(display_text) <= 1 or display_text == 'ERROR':
#                 self.label_display['text'] = '0'
#             else:
#                 self.label_display['text'] = display_text[:-1]
#
#     def run(self):
#         self.window.mainloop()
#
#
# calc1 =CALCULATOR()
# calc2  =CALCULATOR()
# calc1.run()
# calc2.run()
#
#
import sqlite3 as sql
connection = sql.connect('mohammad.db')
connection.execute("""CREATE TABLE  IF NOT EXISTS student_record(
student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,user_name TEXT NOT NULL,
password TEXT NOT NULL
)
""")
#inserting data



connection.execute("INSERT INTO student_record (user_name,password) VALUES ('TAHA','ALI123') ")
connection.execute("INSERT INTO student_record (user_name,password) VALUES ('tayyab','tariq123') ")
connection.execute("INSERT INTO student_record (user_name,password) VALUES ('faseeeh','hyder123') ")

connection.commit()  #  to add the data in the field
connection.close()   # to close the database



#
# connection.execute("""CREATE TABLE payment_record(
# payment_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,payment_type TEXT NOT NULL,
# password TEXT NOT NULL
# )
#
#
#
#
# """)



from tkinter import *
win= Tk()
win.geometry("350x250")
win.title("tahadatabase")

def click():
    uname =user_name.get()
    pasw =password.get()

    if uname =="" or pasw== "":
        message.set("fill the form below")

    else:
        connection = sql.connect('student.db')
        cursor=connection.execute("select *  FROM student_record WHERE user_name  = '%s' and password = '%s' " %(uname,pasw))

    if cursor.fetchone():
        message.set("login succesful")
    else:
        message.set("username or password invalid")

user_name  = StringVar()
password  = StringVar()

message = StringVar()

Label(win,text='username',bg='blue',fg='red', font=("Arial", 12,"bold")).place(x =20,y= 40)
Entry(win,textvariable=user_name,bg='green',fg='yellow',font=("Arial", 12,"bold")).place(x =120,y= 40)

Label(win,text='password',bg='blue',fg='red', font=("Arial", 12,"bold")).place(x =20,y= 80)
Entry(win,textvariable=password,show='*',bg='green',fg='yellow',font=("Arial", 12,"bold")).place(x =120,y= 80)

Button(win,text='login',bg ='red',fg='black',font=("Arial",12,"bold"),command=click ).place(x = 180, y=180)
Label(win,textvariable=message,bg='red',fg='black').place(x =125, y=152)



win.mainloop()