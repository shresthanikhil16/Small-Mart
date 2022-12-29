from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import messagebox
#Title Sizw
mart=Tk()
mart.title("K Mart")
mart.geometry('925x500+300+200')
mart.resizable(False,False)
mart.configure(bg="#fff")
#user sign in and password
def signin():
    username=user.get()
    password=code.get()
    if username=='kirtan1232'and password=='nepal123':
        screen=Toplevel(mart)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        Label(screen,text="Welcome to our Mart",bg="#fff",font=("Calibri(Body",50,"bold")).pack(expand=True)
        screen.mainloop()
    elif username!="kirtan1232"and password!="nepal123":
        messagebox.showerror("Invalid",'invalid username and password')
    elif password!="nepal123":
        messagebox.showerror("Invalid","invalid password")
    elif username!="kirtan1232":
        messagebox.showerror("Invalid","invalid username and password")

#icon
photo = PhotoImage(file = "Kmart.png")
mart.iconphoto(False, photo)
mart.configure(bg="white")
#Login page
img=PhotoImage(file="grocery.png")
Label(mart,image=img,bg='white').place(x=50,y=50)
frame=Frame(mart,width=350,height=350,bg="white")
frame.place(x=480,y=70)
heading=Label(frame,text="Sign In",fg="#57a148",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)
####--------UserID -----------###
def on_enter(e):
    user.delete(0,"end")
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0 ,"UserName") 
user=Entry(frame,width=25,fg="black",border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,"UserName")
user.bind("<FocusIn>",on_enter)
user.bind("FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
###-------------Password-----------###
def on_enter(e):
    code.delete(0,"end")
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0 ,"Password") 
code=Entry(frame,width=25,fg="black",border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
##---------Button------------##
Button(frame,width=39,pady=8,text="Sign In",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have a account?",fg="black",bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg="#57a1f8")
sign_up.place(x=215,y=270)

# k=Label(mart,text="UserName",bg="light green",fg="blue").place(x=30,y=50)
# k=Label(mart,text="Password",bg="light green",fg="blue").place(x=30,y=90)
# login=Button(mart,text="Login").place(x=100,y=120)
# register=Button(mart,text="Register",state=DISABLED).place(x=150,y=120)
# password=StringVar()
#login and password write place
# e1=Entry(mart).place(x=100,y=50)
# e2=Entry(mart,textvariable=password,show='*').place(x=100,y=90)


mart.mainloop()
