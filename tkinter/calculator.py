import tkinter as tk
from tkinter import *
from tkinter.font import *
window  = tk.Tk()
window.geometry("400x600")
window.title("claculator")




# window.columnconfigure(0,weight=1)
# window.columnconfigure(1,weight=1)
# window.columnconfigure(2,weight=1)
# window.columnconfigure(3,weight=1)


for i in range(0,4):
    window.columnconfigure(i, weight=1)


for j in range(0,6):
    window.rowconfigure(j, weight=1)


displayfnt = Font(family='consolas',size=50,weight ='bold')
btdisplay = Font(family='arial black',size=30)
lbldisplay = Label(window,text="0",fg ='blue',bg ='red',font=displayfnt,anchor='e').grid(row=0,column=0,sticky=tk.NE+tk.SW,columnspan=4)
bt0 = Button(window,text="0",font=btdisplay,bg='blue',fg='yellow').grid(row=5,column=0,sticky=tk.NSEW,columnspan=2)
bt1 = Button(window,text="1",font=btdisplay,bg='blue',fg='yellow').grid(row=4,column=0,sticky=tk.NSEW)
bt2 = Button(window,text="2",font=btdisplay,bg='blue',fg='yellow').grid(row=4,column=1,sticky=tk.NSEW)
bt3 = Button(window,text="3",font=btdisplay,bg='blue',fg='yellow').grid(row=4,column=2,sticky=tk.NSEW)
bt4 = Button(window,text="4",font=btdisplay,bg='blue',fg='yellow').grid(row=3,column=0,sticky=tk.NSEW)
bt5 = Button(window,text="5",font=btdisplay,bg='blue',fg='yellow').grid(row=3,column=1,sticky=tk.NSEW)
bt6 = Button(window,text="6",font=btdisplay,bg='blue',fg='yellow').grid(row=3,column=2,sticky=tk.NSEW)
bt7 = Button(window,text="7",font=btdisplay,bg='blue',fg='yellow').grid(row=2,column=0,sticky=tk.NSEW)
bt8 = Button(window,text="8",font=btdisplay,bg='blue',fg='yellow').grid(row=2,column=1,sticky=tk.NSEW)
bt9 = Button(window,text="9",font=btdisplay,bg='blue',fg='yellow').grid(row=2,column=2,sticky=tk.NSEW)
btadd = Button(window,text="+",font=btdisplay,bg ='black',fg='red').grid(row=1,column=0,sticky=tk.NSEW)
btsubtract = Button(window,text="-",font=btdisplay,bg ='black',fg='red').grid(row=1,column=1,sticky=tk.NSEW)
btmul = Button(window,text="x",font=btdisplay,bg ='black',fg='red').grid(row=1,column=3,sticky=tk.NSEW)
btdiv = Button(window,text="/",font=btdisplay,bg ='black',fg='red').grid(row=1,column=2,sticky=tk.NSEW)
bteq = Button(window,text="=",font=btdisplay,bg='purple',fg ='red').grid(row=4,column=3,sticky=tk.NSEW,rowspan=2)
btAC= Button(window,text="AC",font=btdisplay,bg='purple',fg ='red').grid(row=2,column=3,sticky=tk.NSEW)
btCE= Button(window,text="CE",font=btdisplay,bg='purple',fg ='red').grid(row=3,column=3,sticky=tk.NSEW)
btdecimal= Button(window,text=".",font=btdisplay,bg='blue',fg='yellow').grid(row=5,column=2,sticky=tk.NSEW)

















window.mainloop()