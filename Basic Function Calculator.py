#This is a program that calculates a users inputed numbers using either addition, subtraction, division, or multiplication
from tkinter import *
#These are functions tthat realte to the individual buttons to perform the operation 
def addition():
    add=eval(firstNum.get())+eval(secondNum.get())
    results.set(add)
def subtraction():
    sub=eval(firstNum.get())-eval(secondNum.get())
    results.set(sub)
def multiplication():
    mul=eval(firstNum.get())*eval(secondNum.get())
    results.set(mul)
def division():
     div=eval(firstNum.get())/eval(secondNum.get())
     results.set(div)

window=Tk()
window.title('Basic Function Calculator')
title=Label(window, text='Basic Function Calculator',font=('Verdana',15))
title.grid(row=0,column=1,padx=1,sticky=N)

#This makes the results a string and allows it to be defined  
results=StringVar()

#This creates the entry box and label for the first  number
contentsFirst=StringVar()
firstNum=Entry(bg='white',textvariable=contentsFirst)
firstNum.grid(row=2, column=1,pady=15, sticky=W)
firstNumlbl=Label(window,text='First Number:')
firstNumlbl.grid(row=2,column=0, sticky=E,padx=5, pady=15)

#This creates the entry box and label for the second number 
contentsSecond=StringVar()
secondNum=Entry(bg='white',textvariable=contentsSecond)
secondNum.grid(row=3,column=1,pady=5,sticky=W)
secondNumlbl=Label(window,text='Second Number:')
secondNumlbl.grid(row=3,column=0, sticky=E,padx=5,pady=5)


#This creates the addition button and relates it to the add function
addBtn=Button(window,text='+',font=('courier',18),command=addition)
addBtn.grid(row=4,column=0,padx=20,pady=30,sticky=W)
addBtn.config(width=2)

#This creates the subtraction button and relates it to the add function
subBtn=Button(window,text='-',font=('courier',18),command=subtraction)
subBtn.grid(row=4,column=1,padx=20,pady=30,sticky=W )
subBtn.config(width=2)

#This creates the multiplaction button and relates it to the add function
mulBtn=Button(window,text='x',font=('courier',18),command=multiplication)
mulBtn.grid(row=4,column=1,padx=125,pady=30,sticky=W)
mulBtn.config(width=2)

#This creates the divide button and relates it to the add functionn
divBtn=Button(window,text='/',font=('courier',18),command=division)
divBtn.grid(row=4,column=1,padx=235,pady=30,sticky=W)
divBtn.config(width=2)

#This creates the results label and displays it within the entry box, users cannot enter anything into it
resultsLbl=Label(window,text='Your Answer is:',font=('Courier',18))
resultsLbl.grid(row=5,column=1,padx=75,pady=75,sticky=W)
resultsEnt=Entry(window,font=('Courier',18),state='readonly',textvariable=results,fg='green')
resultsEnt.grid(row=5,column=1,padx=50,pady=25,sticky=SW)

window.mainloop()


        
    
