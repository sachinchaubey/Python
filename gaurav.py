from tkinter import *
import random
import time

root = Tk()
root.geometry('1400x700+0+0')
root.title('Resaurant Management Systems')

text_Input = StringVar()
operator=''

Tops = Frame(root, width = 1400,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 700,height=600,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 200,height=600,relief=SUNKEN)
f2.pack(side=RIGHT)

#------------------------------------TIME----------------------------------------

localtime=time.asctime(time.localtime(time.time()))


#--------------------------------INFORMATION------------------------------------

lblInfo = Label(Tops,font=('arial',50,'bold'),text='Resaurant Management Systems',fg='Red',bd=5,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops,font=('arial',20,'bold'),text=localtime,fg='blue',bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

#---------------------------------CALCULATOR-------------------------------------
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ''
    text_Input.set('')

def btnEqualInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ''

def Ref():
    x = random.randint(12908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF=float(Fries.get())
    CoD=float(Drinks.get())
    CoFilet=float(Filet.get())
    CoBurger=float(Burger.get())
    CoPanBurger=float(Panner_Burger.get())
    CoCheese_Burger=float(Cheese_Burger.get())

    CostofFires = CoF * 0.99
    CostofDrinks = CoD * 1.00
    CostofFilet = CoFilet * 2.99
    CostofBruger = CoBurger * 2.87
    CostofPanner_Burger = CoPanBurger * 3.10
    CostofCheese_Burger = CoCheese_Burger * 3.40

    CostofMeal = '$',str('%.2f' % (CostofFires + CostofDrinks + CostofFilet + CostofBruger + CostofPanner_Burger + CostofCheese_Burger))
    PayTax = ((CostofFires + CostofDrinks + CostofFilet + CostofBruger + CostofPanner_Burger + CostofCheese_Burger) * 0.2)
    TotalCost = (CostofFires + CostofDrinks + CostofFilet + CostofBruger + CostofPanner_Burger + CostofCheese_Burger)
    Ser_Charge = ((CostofFires + CostofDrinks + CostofFilet + CostofBruger + CostofPanner_Burger + CostofCheese_Burger)/99)

    Service = '$',str('%.2f' % Ser_Charge)
    OverAllCost = '$',str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = '$',str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Sub_Total.set(CostofMeal)
    Total.set(OverAllCost)
    
    
    
     
def qExit():
    root.destroy()

def Reset():
    rand.set('')
    Fries.set('')
    Burger.set('')
    Filet.set('')
    Drinks.set('')
    Panner_Burger.set('')
    Cheese_Burger.set('')
    Tax.set('')
    Cost.set('')
    Service_Charge.set('')
    Sub_Total.set('')
    Total.set('')

    
txtDisplay = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg='white',justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='7',bg='orange',command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='8',bg='orange',command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='9',bg='orange',command=lambda:btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='+',bg='yellow',command=lambda:btnClick('+')).grid(row=2,column=3)

#------------------------------------------------------------------------------------------------------------------------------------------------

btn4=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='4',bg='orange',command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='5',bg='orange',command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='6',bg='orange',command=lambda:btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='-',bg='yellow',command=lambda:btnClick('-')).grid(row=3,column=3)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='1',bg='orange',command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='2',bg='orange',command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='3',bg='orange',command=lambda:btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='x',bg='yellow',command=lambda:btnClick('x')).grid(row=4,column=3) 

#--------------------------------------------------------------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='0',bg='orange',command=lambda:btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='C',bg='orange',command=btnClearDisplay).grid(row=5,column=1)

btnEqual=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='=',bg='orange',command=btnEqualInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='/',bg='yellow',command=lambda:btnClick('/')).grid(row=5,column=3)

#----------------------------------------------------------------------------------------------------------------------------------------------------

point=Button(f2,padx=16,pady=16,bd=8, fg='black',font=('arial',15,'bold'),text='.',bg='orange',command=lambda:btnClick('.')).grid(row=6,column=1)

#--------------------------------------------------Restaurant Info : 1------------------------------------------------------------------------
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
Drinks = StringVar()
Panner_Burger = StringVar()
Cheese_Burger = StringVar()
Tax = StringVar()
Cost = StringVar()
Service_Charge = StringVar()
Sub_Total = StringVar()
Total = StringVar()

lblReference = Label(f1,font=('arial',16,'bold'),text='Reference',bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=2,bg='white',justify = 'right')
txtReference.grid(row=0,column=1)

lblFries = Label(f1,font=('arial',16,'bold'),text='Large Fries',bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg='white',justify = 'right')
txtFries.grid(row=1,column=1)

lblBurger = Label(f1,font=('arial',16,'bold'),text='Burger',bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg='white',justify = 'right')
txtBurger.grid(row=2,column=1)

lblFilet = Label(f1,font=('arial',16,'bold'),text='Filet',bd=16,anchor='w')
lblFilet.grid(row=3,column=0)
txtFilet=Entry(f1,font=('arial',16,'bold'),textvariable=Filet,bd=10,insertwidth=4,bg='white',justify = 'right')
txtFilet.grid(row=3,column=1)

lblDrinks = Label(f1,font=('arial',16,'bold'),text='Drinks',bd=16,anchor='w')
lblDrinks.grid(row=4,column=0)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg='white',justify = 'right')
txtDrinks.grid(row=4,column=1)

lblBurger = Label(f1,font=('arial',16,'bold'),text='Panner Burger',bd=16,anchor='w')
lblBurger.grid(row=5,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Panner_Burger,bd=10,insertwidth=4,bg='white',justify = 'right')
txtBurger.grid(row=5,column=1)
#--------------------------------------------------Restaurant Info : 2----------------------------------------------------------------
lblBurger = Label(f1,font=('arial',16,'bold'),text='Cheese Burger',bd=16,anchor='w')
lblBurger.grid(row=0,column=2)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Cheese_Burger,bd=10,insertwidth=4,bg='white',justify = 'right')
txtBurger.grid(row=0,column=3)

lblCost = Label(f1,font=('arial',16,'bold'),text='Cost of Meal',bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg='white',justify = 'right')
txtCost.grid(row=1,column=3)

lblCharge = Label(f1,font=('arial',16,'bold'),text='Service Charge',bd=16,anchor='w')
lblCharge.grid(row=2,column=2)
txtCharge=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg='white',justify = 'right')
txtCharge.grid(row=2,column=3)

lblTax  = Label(f1,font=('arial',16,'bold'),text='State Tax',bd=16,anchor='w')
lblTax .grid(row=3,column=2)
txtTax =Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg='white',justify = 'right')
txtTax .grid(row=3,column=3)

lblTotal = Label(f1,font=('arial',16,'bold'),text='Sub Total',bd=16,anchor='w')
lblTotal.grid(row=4,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Sub_Total,bd=10,insertwidth=4,bg='white',justify = 'right')
txtTotal.grid(row=4,column=3)

lblTotal = Label(f1,font=('arial',16,'bold'),text='Total Cost',bd=16,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg='white',justify = 'right')
txtTotal.grid(row=5,column=3)
#--------------------------------------------------Buttons-------------------------------------------------------
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,text='Total',bg='sky blue',command = Ref).grid(row=7,column=1)

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,text='Exit',bg='sky blue',command = qExit).grid(row=7,column=3)

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg='black',font=('arial',16,'bold'),width=10,text='Reset',bg='sky blue',command = Reset).grid(row=7,column=2)

#------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
