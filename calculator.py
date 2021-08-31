from tkinter import *
from tkinter import ttk
import threading
import time
root=Tk()
def TIME():
    L['text']=time.ctime()
    L.after(1000,TIME)
def clear():
    global s1
    s1=s1[:-1:]
    s.set(s1)
def display(t):
    global s1
    s1=s.get()+t
    s.set(s1)
def c():
     s.set('')
def result():
    global s1
    s1=s.get()
    s1=str(eval(s1))
    s.set(s1)
s1=''

s=StringVar()
root.title("Calculator")
fe=Frame(root)
f1=Frame(root)
f2=Frame(root)
f3=Frame(root)
f4=Frame(root)
f5=Frame(root)
e1=ttk.Entry(fe,textvariable=s,justify=RIGHT)
e1.pack(fill=BOTH,expand=YES,padx=5,pady=5)
for i in '789/':
    b=ttk.Button(f1,text=i,command=lambda x=i:display(x))
    b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
for i in '456*':
    b=ttk.Button(f2,text=i,command=lambda x=i:display(x))
    b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
for i in '123-':
    b=ttk.Button(f3,text=i,command=lambda x=i:display(x))
    b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
for i in '0.+':
    b=ttk.Button(f4,text=i,command=lambda x=i:display(x))
    b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
b=ttk.Button(f4,text='=',command=result)
b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
fe.pack(fill=BOTH,expand=YES,padx=5,pady=5)
f1.pack(fill=BOTH,expand=YES,padx=5,pady=5)
f2.pack(fill=BOTH,expand=YES,padx=5,pady=5)
f3.pack(fill=BOTH,expand=YES,padx=5,pady=5)
f4.pack(fill=BOTH,expand=YES,padx=5,pady=5)
b=ttk.Button(f5,text='<-',command=clear)
b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

b=ttk.Button(f5,text='CE',command=c)
b.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)
f5.pack(fill=BOTH,expand=YES,padx=5,pady=5)
L=ttk.Label(root,font='bold')
L.pack(fill=BOTH,expand=YES,padx=5,pady=5)
TIME()

root.mainloop()
