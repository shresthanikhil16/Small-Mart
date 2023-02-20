from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import messagebox
import sqlite3

def registration():
       root.destroy()
       import signreal
def login():
       root.destroy()
       import main





def check():
    a=user_entry.get()
    b=pw_entry.get()
    try:
        log=sqlite3.connect("register.db")
        log1=log.cursor()

        log1.execute("SELECT * from signup")
        global records
        records=log1.fetchall()
        global i
        i=len(records)-1
        while i>=0:
            if records[i][2]!=a or records[i][4]!=b:
                i=i-1
                if i==-1:
                    messagebox.showerror("Login","Invalid Credentials")
                    break
            else:    
                log.commit()
                messagebox.showinfo("Login","Logged in Successfully")
                login()
                break     
        log.commit()
        log.close()
    except:
        messagebox.showerror("Login","Sign Up First")




root=Tk()
root.minsize(1000,655)
root.maxsize(1000,655)
root.title("JHI : PASA :")
#icon
photo = PhotoImage(file = "shop.png")
root.iconphoto(False, photo)
root.configure(bg="#22A2A2")

root.config(bg="#22A2A2")
#fonst------------------------------------------------
my_font0 = Font(
    family = 'Lucida sans',
    size = 11,
    weight='bold',
    slant = 'roman',
    overstrike = 0)
my_font = Font(
    family = 'Lucida sans',
    size = 13,
    weight='bold',
    slant = 'roman',
    overstrike = 0)
my_font1 = Font(
        family = 'Lucida sans',
        size = 16,
        weight='bold',
        slant = 'roman',
        overstrike = 0)
my_font2 = Font(
        family = 'Lucida sans',
        size = 28,
        weight='bold',
        slant = 'roman',
        overstrike = 0)


#logo------------------------------------------
img=Image.open('shop.png')
img1=img.resize((400,320))
logo=ImageTk.PhotoImage(img1)
logo_p=Label(root,image=logo,bg="#4A78A9")
logo_p.place(x=550,y=150)

#login frame------------------------------------
logon=Frame(root,bg="white",borderwidth=1)
logon.place(x=50,y=95)
log_ttle=Label(logon,bg="light yellow",font=my_font2,padx=240,pady=200)
log_ttle.grid()

#event-entries--------------------------------
def del1(event):
    a=user_entry.get()
    if a=='' or a=='Username':
       user_entry.delete(0,END)
def del2(e):
    b=pw_entry.get()
    if b=='' or b=='Password':
       pw_entry.delete(0,END)
       
#labels and entry---------------------------------------------------------------
login_lb=Label(logon,text="LOGIN",font=my_font2,bg="light yellow",fg="black")
login_lb.place(x=180,y=25)

user=Label(logon,text="Username:",font=my_font1,bg="light yellow",fg="black")
user.place(x=92,y=105)

user_entry=Entry(logon,bg="white",font=my_font1,fg="#2B2828",width=20,borderwidth=2,relief=GROOVE)
user_entry.insert(0,"Username")
user_entry.place(x=120,y=138)
user_entry.bind("<FocusIn>",del1)

#passworddd----------------------------------------
pw=Label(logon,text="Password:",font=my_font1,bg="light yellow",fg="black")
pw.place(x=90,y=190)

pw_entry=Entry(logon,bg="white",font=my_font1,fg="#2B2828",width=20,borderwidth=2,relief=GROOVE,show="*")
pw_entry.insert(0,"Password")
pw_entry.place(x=120,y=225)
pw_entry.bind("<FocusIn>",del2)

#verify function-------------------------------------
def verify():
    a=user_entry.get()
    b=pw_entry.get()
    if (a=="" or a=="Username:") or (b=="" or b=="Password"):
        messagebox.showerror("Login","Error.")
    else:
        check()  

a=Image.open('show.png')
a1=a.resize((20,20))
show_img=ImageTk.PhotoImage(a1)

b=Image.open('hide.png')
b1=b.resize((20,20))
hide_img=ImageTk.PhotoImage(b1)
            


    #hide/show functions 
def hide():
       show_btn=Button(logon,image=show_img,command=show,bg="white",borderwidth=0,activebackground="#CBD8ED")
       show_btn.place(y=228,x=325)
       pw_entry.config(show="")

def show():
       hide_btn=Button(logon,image=hide_img,command=hide,bg="white",borderwidth=0,activebackground="#CBD8ED")
       hide_btn.place(y=228,x=325)
       pw_entry.config(show="*")

show_btn=Button(logon,image=show_img,command=show,bg="white",borderwidth=0,activebackground="#CBD8ED")
show_btn.place(y=228,x=325)
hide_btn=Button(logon,image=hide_img,command=hide,bg="white",borderwidth=0,activebackground="#CBD8ED")
hide_btn.place(y=228,x=325)


#loging button---------------------------------------------
log_btn=Button(logon,bg="#22A2A2",fg='white',text="LOGIN",padx=92,font=my_font,command=verify)
log_btn.place(x=120,y=275)

new=Label(logon,bg="light yellow",text="Don't have a account?",fg="#2B2828",font=my_font0)
new.place(x=150,y=325)

register_btn=Button(logon,bg="#22A2A2",fg='white',text="Sign Up",font=my_font0,command=registration,padx=10)
register_btn.place(x=200,y=355)





root.mainloop()