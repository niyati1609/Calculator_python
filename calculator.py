from tkinter import *
import pyttsx3 as py
import os
import sqlite3
import time
import math
import parser
from tkinter import filedialog
from PIL import ImageTk,Image
root = Tk()
root.geometry('310x400')
root.title('Calculator')

operator=""
t1=StringVar()
root.config(bg = 'lavender blush')
def clickbut(number):   #lambda:clickbut(1)
     global operator
     operator=operator+str(number)
     t1.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     t1.set(add)
     operator=''
def equlbut():
     global operator
     sub=str(eval(operator))
     t1.set(sub)
     operator=''     
def equlbut():
     global operator
     mul=str(eval(operator))
     t1.set(mul)
     operator=''
def equlbut():
     global operator
     div=str(eval(operator))
     t1.set(div)
     operator=''    

def clrbut():
     t1.set('')

e1= Entry(root,font=('cyan',17,'bold'),textvariable=t1,bd=15,bg='misty rose',fg='black')
e1.place(x=10,y=10)
b1= Button(root,text='+',command=lambda:clickbut("+"),font=('times',17,'bold'),bd=5,height=1,width=2,bg='pink',fg='white')
b1.place(x=30,y=90)
b2= Button(root,text='-',command=lambda:clickbut("-"),font=('times',17,'bold'),bd=5,height=1,width=2,bg='pink',fg='white')
b2.place(x=90,y=90)
b3= Button(root,text='x',command=lambda:clickbut("*"),font=('times',17,'bold','bold'),bd=5,height=1,width=2,bg='pink',fg='white')
b3.place(x=150,y=90)
b4= Button(root,text='/',command=lambda:clickbut("/"),bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b4.place(x=210,y=90)
b5= Button(root,text='1',bd=5,command=lambda:clickbut(1),font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b5.place(x=30,y=150)
b6= Button(root,text='2',command=lambda:clickbut(2),bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b6.place(x=90,y=150)
b7= Button(root,text='3',command=lambda:clickbut(3),bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b7.place(x=150,y=150)
b14= Button(root,text='=',bd=5,font=('times',17,'bold'),command=equlbut,height=1,width=2,bg='pink',fg='white')
b14.place(x=210,y=150)
b8= Button(root,text='4',command=lambda:clickbut(4),bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b8.place(x=30,y=210)
b9= Button(root,text='5',command=lambda:clickbut(5),bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b9.place(x=90,y=210)
b10= Button(root,text='6',command=lambda:clickbut(6),bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b10.place(x=150,y=210)
b15= Button(root,text='log',bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b15.place(x=210,y=210)
b11= Button(root,text='7',command=lambda:clickbut(7),bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b11.place(x=30,y=270)
b12= Button(root,text='8',bd=5,font=('times',17,'bold'),command=lambda:clickbut(8),height=1,width=2,bg='pink',fg='white')
b12.place(x=90,y=270)
b13= Button(root,text='9',bd=5,font=('times',17,'bold'),command=lambda:clickbut(9),height=1,width=2,bg='pink',fg='white')
b13.place(x=150,y=270)
b16= Button(root,text='( )',bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b16.place(x=210,y=270)
b17= Button(root,text='Sq',bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',fg='white')
b17.place(x=30,y=330)
b18= Button(root,text='0',bd=5,font=('times',17,'bold'),height=1,width=2,bg='pink',command=lambda:clickbut(0),fg='white')
b18.place(x=90,y=330)
b19= Button(root,text='.',bd=5,font=('times',17,'bold'),command=lambda:clickbut("."),height=1,width=2,bg='pink',fg='white')
b19.place(x=150,y=330)
b20= Button(root,text='C',bd=5,font=('times',17,'bold'),command=clrbut,height=1,width=2,bg='pink',fg='white')
b20.place(x=210,y=330)
root.mainloop()


