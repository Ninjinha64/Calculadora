#Importação tkinter

from tkinter import *
from tkinter import ttk

#Cores utilizadas

cor1 = "#3b3b3b" #black
cor2 = "white" #white
cor3 = "#baffc0" #Light_Green
cor4 = "#ECEFF1" #Gray
cor5 = "#47d17a" #Green


Windows = Tk()
Windows.title("Calculadora")
Windows.geometry("235x310")
Windows.config(bg=cor1)


# Creating Frames
frame_Display = Frame(Windows, width=235, height=50,bg=cor3)
frame_Display.grid(row=0, column=0)

frame_body = Frame(Windows, width=235, height=260,)
frame_body.grid(row=1, column=0)


# variable all values

all_values = ''



# Creating function
def get_values(event):

    global all_values

    all_values = all_values + str(event)



    #passing value for display

    value_text.set(all_values)

# Function for calculation

def calcular():
    global all_values
    result = eval(all_values)
    
    value_text.set(str(result))


# Function Clean_Screen

def clen_display():
    global all_values
    all_values = ""
    value_text.set("")




# Creating Label

value_text = StringVar()
app_label = Label(frame_Display, textvariable=value_text, width=16, height=2, padx=7, relief=FLAT,anchor="e", justify=RIGHT, font=('Monocraft 16'),bg=cor3,)
app_label.place(x=0,y=0)


#Creating bottom

b_1 = Button(frame_body, command= clen_display, text="C",width=11,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_body, command=lambda:get_values('%'), text="%",width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_body, command=lambda:get_values('/'),text="/",width=5,height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)



b_4 = Button(frame_body, command=lambda:get_values('7'),text="7",width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_body, command=lambda:get_values('8'),text="8",width=5,height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_body, command=lambda:get_values('9'),text="9",width=5,height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_body, command=lambda:get_values('*'),text="*",width=5,height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)


b_8 = Button(frame_body, command=lambda:get_values('4'),text="4",width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_body, command=lambda:get_values('5'),text="5",width=5,height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frame_body, command=lambda:get_values('6'),text="6",width=5,height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frame_body, command=lambda:get_values('-'),text="-",width=5,height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)






b_12 = Button(frame_body, command=lambda:get_values('1'),text="1",width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_body, command=lambda:get_values('2'),text="2",width=5,height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_body, command=lambda:get_values('3'),text="3",width=5,height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_body, command=lambda:get_values('+'),text="+",width=5,height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)


b_16 = Button(frame_body, command=lambda:get_values('0'),text="0",width=11,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_body, command=lambda:get_values('.'),text=".",width=5,height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frame_body, command= calcular,text="=",width=5,height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)













Windows.mainloop()

