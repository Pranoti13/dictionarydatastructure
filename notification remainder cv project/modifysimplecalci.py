from tkinter import *
import math

win = Tk()  # This is to create a basic window
win.geometry("312x324")  # this is for the size of the window
#win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("My Calculator")


###################Starting with functions ####################
# 'btn_click' function :
# This Function continuously updates the input field whenever you enters a number

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# 'bt_clear' function :This is used to clear
# the input field

def bt_clear():
    global expression
    expression = ""
    input_text.set("")


# 'bt_equal':This method calculates the expression
# present in input field

def bt_equal():

    global expression
    result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""


expression = ""

# 'StringVar()' :It is used to get the instance of input field

input_text = StringVar()

# Let us creating a frame for the input field
# frame is nothing but container widget(control)
#bd is border
input_frame = Frame(win, width=312, height=50, bd=0, bg='black', highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)

input_frame.pack(side=TOP)

# Let us create a input field inside the 'Frame'

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)
# 'ipady' is internal padding to increase the height of input field

# Let us creating another 'Frame' for the button below the 'input_frame'

btns_frame = Frame(win, width=312, height=272.5, bg="red")

btns_frame.pack()

# first row

clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_clear()).grid(row=0, column=0, columnspan=1, padx=1, pady=1)

degree = Button(btns_frame, text="deg", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_degree()).grid(row=0, column=1,padx=1, pady=1)

modular = Button(btns_frame, text="MOD", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_MOD()).grid(row=0, column=2,padx=1, pady=1)

delete = Button(btns_frame, text="DEL", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_DEL()).grid(row=0, column=3,padx=1, pady=1)

'''2nd = Button(btns_frame, text="2nd", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click("2nd")).grid(row=0, column=4,padx=1, pady=1)'''

#second row

fact=Button(btns_frame, text="x!", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_click("!")).grid(row=1, column=0, columnspan=1, padx=1, pady=1)

permucombo= Button(btns_frame, text="nCr", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_click("nCr")).grid(row=1, column=1, columnspan=1, padx=1, pady=1)

random= Button(btns_frame, text="Ran#", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_click("Ran")).grid(row=1, column=2, columnspan=1, padx=1, pady=1)

log10= Button(btns_frame, text="log", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_click("log")).grid(row=1, column=3, columnspan=1, padx=1, pady=1)

loge= Button(btns_frame, text="ln", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_click("lnx")).grid(row=1, column=4, columnspan=1, padx=1, pady=1)




#third row


root = Button(btns_frame, text="√", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("√")).grid(row=2, column=0, padx=1, pady=1)

power = Button(btns_frame, text='x'+get_super('y'), fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("pow")).grid(row=2, column=1, padx=1, pady=1)

reciprocal = Button(btns_frame, text='x'+get_super('-1'), fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("r")).grid(row=2, column=2, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("/")).grid(row=2, column=3, padx=1, pady=1)

sin = Button(btns_frame, text="sin", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("sin")).grid(row=2, column=4, padx=1, pady=1)



# fourth row

seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=3, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=3, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=3, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=3, column=3, padx=1, pady=1)

cos = Button(btns_frame, text="cos", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("cos")).grid(row=3, column=4, padx=1, pady=1)

# fifth row

four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=4, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=4, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=4, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click("-")).grid(row=4, column=3, padx=1, pady=1)

tan = Button(btns_frame, text="tan", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click("tan")).grid(row=4, column=4, padx=1, pady=1)

# sixth row

one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=5, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=5, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=5, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=5, column=3, padx=1, pady=1)

pi = Button(btns_frame, text="π", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: btn_click("π")).grid(row=5, column=4, padx=1, pady=1)




# seventh row

zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=6, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=6, column=1, padx=1, pady=1)

ce= Button(btns_frame, text="CE", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click()).grid(row=6, column=2, padx=1, pady=1)


equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: bt_equal()).grid(row=6, column=3, padx=1, pady=1)

e = Button(btns_frame, text="e", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("e")).grid(row=6, column=4, padx=1, pady=1)

win.mainloop()