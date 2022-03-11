from tkinter import*
root=Tk()
root.title("Smart Calculator")
def button_response(event):              #creating fun for button

    b=event.widget
    text=b['text']
    if text=="=":
        try:
            the_value=entry.get()
            answer=eval(the_value)
            entry.delete(0,END)
            entry.insert(0,answer)
        except SyntaxError:
            Serror="Syntax Error"
            entry.delete(0,END)
            entry.insert(0,Serror)
        except ZeroDivisionError:
            Zerror="Undefined"
            entry.delete(0,END)
            entry.insert(0,Zerror)
        return
    entry.insert(END,text)

def clear():
    entry.delete(1)

root.resizable()
root['bg']=['#42f593']
value=DoubleVar()
entry=Entry(root,width=10,justify="right",bg="black",fg="#39f500",border=8,font=("Verdana",20),textvariable= value)
entry.grid(column=0,row=0,pady=10)
frame1=LabelFrame(root,bg="#97b4f7")
frame1.grid(column=0,row=1)
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(frame1,text=str(temp),font=("Disco revival",20,"bold"),bg="#cad9db",activebackground='magenta')
        btn.grid(column=j,row=i)
        temp=temp+1
        btn.bind('<Button-1>',button_response)
C=Button(frame1,text="C",font=("Disco revival",20,"bold"),bg="#cad9db",activebackground='magenta',command=clear)
C.grid(column=4,row=0)
sign1=Button(frame1,text="+",font=("Disco revival",20,"bold"),bg="#cad9db",activebackground='magenta')
sign1.grid(column=4,row=1)
sign2=Button(frame1,text="-",font=("Disco revival",20,"bold"),width=int(2.5),bg="#cad9db",activebackground='magenta')
sign2.grid(column=4,row=2)
sign3=Button(frame1,text="=",font=("Disco revival",20,"bold"),bg="#cad9db",activebackground='magenta')
sign3.grid(column=4,row=3)
sign4=Button(frame1,text="*",font=("Disco revival",20,"bold"),width=int(2.5),bg="#cad9db",activebackground='magenta')
sign4.grid(column=1,row=3)
sign5=Button(frame1,text="/",font=("Disco revival",20,"bold"),width=int(2.5),bg="#cad9db",activebackground='magenta')
sign5.grid(column=0,row=3)
btn0=Button(frame1,text="0",font=("Disco revival",20,"bold"),bg="#cad9db",activebackground='magenta')
btn0.grid(column=2,row=3)

for child in frame1.winfo_children():
    child.grid_configure(padx=5,pady=5)
sign1.bind('<Button-1>',button_response)
sign2.bind('<Button-1>',button_response)
sign3.bind('<Button-1>',button_response)
sign4.bind('<Button-1>',button_response)
sign5.bind('<Button-1>',button_response)
btn0.bind('<Button-1>',button_response)
root.mainloop()