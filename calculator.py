from math import pow, sqrt
from tkinter import *


class cuch:
    def getandreplace(self):
        self.expression=self.txt.get()
        self.newtext=self.expression.replace('x','*')
    def equals(self):
        self.getandreplace()
        try:
            self.value=eval(self.newtext)
        except NameError:
            self.txt.delete(0,END)
            self.txt.insert(0,'invalid input')
        except SyntaxError:
            self.txt.delete(0,END)
            self.txt.insert(0,'syntax error')
        else:
            self.txt.delete(0,END)
            
            self.txt.insert(0,self.value)
    def squareroot(self):
        self.getandreplace()
        try:
            self.value=eval(self.newtext)
        except NameError:
            self.txt.delete(0,END)
            self.txt.insert(0,'invalid input')
        except SyntaxError:
            self.txt.delete(0,END)
            self.txt.insert(0,'syntax error.')
        else:
            self.sqrtval=sqrt(int(self.newtext))
            self.txt.delete(0,END)
            self.txt.insert(0,self.sqrtval)
    def square(self):
        self.getandreplace()
        try:
            self.value=eval(self.newtext)
        except NameError:
            self.txt.delete(0,END)
            self.txt.insert(0,'invalid input')
        except SyntaxError:
            self.txt.delete(0,END)
            self.txt.insert(0,'syntax error')
        else:
            self.sqrtval=pow(int(self.newtext))
            self.txt.delete(0,END)
            self.txt.insert(0,self.sqrtval)
    def put(self,argi):
        self.i+=1
        self.txt.insert(self.i,argi)
    def clearall(self):
        self.txt.delete(0,END)
    def clear1(self):
        self.less=self.txt.get()[:-1]
        self.txt.delete(0,END)
        self.txt.insert(0,self.less)
       
    def __init__(self,master):
        master.title('calculator')
        master.geometry()
        self.txt=Entry(master)
        self.txt.grid(row=0,column=0,columnspan=6,pady=3)
        self.txt.focus_set()
        self.i=0
        s=[[('7',7,3,0),('8',8,3,1),('9',9,3,2),('/','/',3,3)],
       [('4',4,2,0),('5',5,2,1),('6',6,2,2),('x','x',2,3),('(','(',2,4),(')',')',2,5)],
       [('1',1,1,0),('2',2,1,1),('3',3,1,2),('-','-',1,3)],
       [('.','.',4,0),('0',0,4,1),('%','%',4,2),('+','+',4,3)],
       [('AC',self.clearall,1,4),('DEL',self.clear1,1,5),
       ('sqrt',self.squareroot,3,4),('x2',self.square,3,5),('=',self.equals,4,4)]
      ]   
        
        for i,c,m,n in s[2]:
            Button(master,text=i,width=3,command=lambda a=c:self.put(a)).grid(row=m,column=n)
        for i,c,m,n in s[1]:
            Button(master,text=i,width=3,command=lambda a=c:self.put(a)).grid(row=m,column=n)
        for i,c,m,n in s[0]:
            Button(master,text=i,width=3,command=lambda a=c:self.put(a)).grid(row=m,column=n)
        for i,c,m,n in s[3]:
            Button(master,text=i,width=3,command=lambda a=c:self.put(a)).grid(row=m,column=n)
        for i,c,m,n in s[4]:
            Button(master,text=i,width=3,command=lambda a=c:a()).grid(row=m,column=n)
root=Tk()
non=cuch(root)   
root.mainloop()
