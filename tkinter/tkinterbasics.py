# import tkinter as tk
# from tkinter.messagebox import *
# from tkinter.filedialog import *
#
#
#
#
# filename   = None
# window = tk.Tk()
# window.geometry("800x600")
# window.title("untitle - notepad")
#
# def click_new():
#     editor.delete(1.0,tk.END)
#     window.title('untitled _ notepad')
#
# def click_open():
#     global  filename
#
#     filename = askopenfilename(defaultextension= ".txt", filetypes= [("any file name and extension" , "*.*"),("every text document ","*.txt")])
#     if filename != None  and filename != "":
#         window.title(filename + ' - notepad')
#         file = open(filename , "r")
#         text = file.read()
#         editor.delete(1.0 ,tK.END)
#         editor.insert(1.0,text)
#         file.close()
#
#
# def click_save():
#     global  filename
#     if filename == None     and filename == "":
#         filename = asksaveasfilename(initialfile= 'untilted.txt')
#
# def click_saveas():
#     pass
#
# def click_exit():
#     window.destroy()
#
# def click_cut():
#     editor.event_generate('<<cut>>')
#
# def click_copy():
#     editor.event_generate('<<copy>>')
# def click_paste():
#     editor.event_generate('<<paste>>')
#
# def click_cut():
#     pass
#
# def click_about():
#     showinfo
#
# mainmenu = tk.Menu(window)
# filemenu = tk.Menu(mainmenu,tearoff=0)
# editmenu = tk.Menu(mainmenu,tearoff=0)
# helpmenu = tk.Menu(mainmenu,tearoff=0)
#
# filemenu.add_command(label = 'New',command = click_new)
# filemenu.add_separator()
# filemenu.add_command(label='open',command=click_open)
# filemenu.add_command(label='save',command=click_save)
# filemenu.add_command(label='save as',command=click_saveas)
# filemenu.add_separator()
# filemenu.add_command(label='exit',command=click_exit)
#
# editmenu.add_command(label='copy',command=click_copy)
# editmenu.add_command(label='paste',command=click_paste)
# editmenu.add_command(label='cut',command=click_cut)
# helpmenu.add_command(label='about',command=click_about)
#
# mainmenu.add_cascade(label="file",menu=filemenu)
# mainmenu.add_cascade(label="edit",menu=editmenu)
# mainmenu.add_cascade(label="help",menu=helpmenu)
#
#
# window.grid_rowconfigure(0,weight=1)
# window.grid_columnconfigure(0,weight=1)
#
#
# window.configure(menu=mainmenu)
# editor = tk.Text(window).grid(sticky=(tk.S + tk.N + tk.E + tk.W))
#
#
# window.mainloop()
# import tkinter as tk
# from tkinter import *
# from tkinter.font import *
# # from ctypes import windll   # using window files to remove blurness
# # windll.shcore.SetProcessorDpiAwareness(1)
# #tkinter.Tk()
# win = Tk()
# width  = 800
# height  = 600
# X =50
# Y  =200
#win.geometry("800x600")
# win.geometry("{}x{}+{}+{}".format(width,height,x,y))
# win.resizable(False,True)
# win.resizable(False,False)
# win.attributes('-alpha',0.6)   #  use  for transparency  by opaque
# win.attributes('-topmost',True) # THIS USED FOR MAKINMG the window at topmost in stack
# win.geometry('{}x{}'.format(width,height))
# fnt = Font(family='consolas',size=20,weight='bold')

# lbl1.place(x =100 ,y =100)
# lbl1  =Label(win,text='one',font=("arial ", 20) , bg='green', fg= 'black')
# lbl2 = Label(win,text="TWO ",bg= 'red',fg='blue',font =fnt)
# lbl3 = Label(win,text="THREE",bg= 'GREEN',fg='YELLOW',font =fnt)
# lbl4 = Label(win,text="FOUR ",bg= 'ORANGE',fg='RED',font =fnt)
# lbl5 = Label(win,text="FIVE",bg= 'PURPLE',fg='GREEN',font =fnt)
# lbl6 = Label(win,text="SIX ",bg= 'BLUE',fg='RED',font =fnt)
# lbl7 = Label(win,text="seven ",bg= 'grey',fg='black',font =fnt)
# lbl8 = Label(win,text="eight",bg= 'red',fg='GREEN',font =fnt)
# lbl9 = Label(win,text="nine ",bg= 'yellow',fg='RED',font =fnt)




# lbl1.pack(ipadx = 20, ipady=20,fill='both',expand=True)
# lbl2.pack(ipadx = 20, ipady=20 , fill='x')
# lbl3.pack(ipadx = 20, ipady=20 , fill='x')
# lbl4.pack(ipadx = 20, ipady=20 , fill='both',side='left',expand=True)
# lbl5.pack(ipadx = 20, ipady=20 , fill='both',side='left',expand=True)
# lbl6.pack(ipadx = 20, ipady=20 , fill='both',side='right',expand=True)


# win.columnconfigure(0,weight = 1)
# win.columnconfigure(1,weight = 1)
# win.columnconfigure(2,weight = 1)
# win.rowconfigure(0,weight=1)
# win.rowconfigure(1,weight=1)
# win.rowconfigure(2,weight=1)
#
# lbl1.grid(row = 0 ,column= 0 ,sticky=tk.NE + tk.SW)
# lbl2.grid(row = 0 ,column= 1 ,columnspan=2,sticky=tk.NE + tk.SW)
# #lbl3.grid(row = 0 ,column= 2 ,sticky=tk.NE + tk.SW)
# lbl4.grid(row = 1 ,column= 0 ,sticky=tk.NE + tk.SW)
# lbl5.grid(row = 1 ,column= 1 ,columnspan=2,rowspan=2,sticky=tk.NE + tk.SW)
# # lbl6.grid(row = 1 ,column= 2 ,sticky=tk.NE + tk.SW)
# lbl7.grid(row = 2 ,column= 0 ,sticky=tk.NE + tk.SW)
# # lbl8.grid(row = 2 ,column= 1 ,sticky=tk.NE + tk.SW)
# # lbl9.grid(row = 2 ,column= 2 ,sticky=tk.NE + tk.SW)


# APPPLICANT FORM



# lbl_username  =Label(win,text='username', font=fnt)
# lbl_password  = Label(win,text="password", font=fnt)
# btn_login =Button(win,text='login',font= fnt)
#
# win.columnconfigure(0, weight=1)
# win.columnconfigure(1, weight=2)
# win.rowconfigure(0, weight=1)
# win.rowconfigure(1, weight=1)
# win.rowconfigure(2,weight=1)
#
# ent_username = Entry(win, font=fnt)
# ent_password = Entry(win,font=fnt)
#
# lbl_username.grid(row = 0, column= 0,sticky=tk.N)
# lbl_password.grid(row = 1, column= 0)
# ent_username.grid(row = 0, column= 1)
# ent_password.grid(row = 1, column= 1)
# btn_login.grid(row = 2 , column= 1)


# win.mainloop()


# a = 'muet'
# for i in a:
#     print(i.upper())

# dict = {'sindh' : {'software':{'batch' :{'twenty':{'subjects':{'assembly':89}}}}}}
#
# print(dict['sindh']['software']['batch']['twenty']['subjects']['assembly'])

# list=['m','u','e','t']
# i  =0
# # a = []
# # while i > (len(list)):
# #
# #     print(list)
# #     i -=1
# while i < len(list)- 1:
#     print(list[::-1])
#     i-=1


from tkinter import *
import  tkinter as tk

win = Tk()
win.geometry("800x600")
a  = StringVar()
b =5
def cal():

    for i in b:
        i = b+1


l1  =  Label(win,text = "enter any numbers")
b1 = Button(win,text = "preess it",command=cal )


e1 = Entry(win,textvariable=a)
e1.get()

l1.grid(column=0, row =0 )
b1.grid(column=1,row= 1)
e1.grid(column=1,row= 0)



win.mainloop()
