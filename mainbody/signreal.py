from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import messagebox

def register():
    reg_p=Tk()
    reg_p.minsize(900,755)
    reg_p.maxsize(900,755)
    reg_p.title("Jhi:Pasa:")
    reg_p.config(bg="#22A2A2")
    #icon
    photo = PhotoImage(file = "shop.png")
    reg_p.iconphoto(False, photo)
    reg_p.configure(bg="#22A2A2")


    #creating a database table
    
    def form_page(): 
        try:
            log=sqlite3.connect('register.db')
            log1=log.cursor()
            log1.execute("""CREATE TABLE signup(
                f_name text,
                l_name text,
                u_name PRIMARY KEY,
                email varchar,
                pw varrchar
                )
            """)
            log.commit()
            log.close()
        except:
            pass


    def login_page(): 
          reg_p.destroy()
          import loginreal


    #fonts------------------------------------------------
    my_font = Font(
        family = 'Lucida sans',
        size = 11,
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
  

    #frame-1---------------------------------------
    frame_r=Frame(reg_p,bg="#98C1D9",borderwidth=1)
    frame_r.place(x=110,y=100)
    
    space=Label(frame_r,pady=260,padx=330,bg="light yellow")
    space.grid()
    
    #labels and entry-----------------------------------------
    r=Label(frame_r,text="Sign Up",font=my_font2,bg="light yellow",fg="black")
    r.place(x=250,y=30)

    #delete funcs----------------------------------------------
    def del1(event):
        x=f_entry.get()
        if x=='first name':
            f_entry.delete(0,END)
    def del2(event):
        x=l_entry.get()
        if x=='last name':
            l_entry.delete(0,END)
    def del3(event):
        x=u_entry.get()
        if x=='Username':
            u_entry.delete(0,END)
    def del4(event):
        x=email_try.get()
        if x=='email':
            email_try.delete(0,END)
    def del5(event):
        x=pw_entry.get()
        if x=='password':
            pw_entry.delete(0,END)
    def del6(event):
        x=cpw_try.get()
        if x=='re-enter':
            cpw_try.delete(0,END)

    #label and entries---------------------------------------
    email=Label(frame_r,text="Email: ",font=my_font1,bg="light yellow",fg="black")
    email.place(x=355,y=210)
    email_try=Entry(frame_r,font=my_font1,bg="white",fg="black")
    email_try.insert(0,"email")
    email_try.place(x=355,y=250)
    email_try.bind("<FocusIn>",del4)
    
    f_name=Label(frame_r,text="First Name: ",font=my_font1,bg="light yellow",fg="black")
    f_name.place(x=50,y=110)
    f_entry=Entry(frame_r,font=my_font1,bg="white",fg="black")
    f_entry.insert(0,"first name")
    f_entry.place(x=50,y=150)
    f_entry.bind("<FocusIn>",del1)

    l_name=Label(frame_r,text="Last Name: ",font=my_font1,bg="light yellow",fg="black")
    l_name.place(x=355,y=110)
    l_entry=Entry(frame_r,font=my_font1,bg="white",fg="black")
    l_entry.insert(0,"last name")
    l_entry.place(x=355,y=150)
    l_entry.bind("<FocusIn>",del2)

    u_name=Label(frame_r,text="Username: ",font=my_font1,bg="light yellow",fg="black")
    u_name.place(x=50,y=210)
    u_entry=Entry(frame_r,font=my_font1,bg="white",fg="black")
    u_entry.insert(0,"Username")
    u_entry.place(x=50,y=250)
    u_entry.bind("<FocusIn>",del3)

    

    pw=Label(frame_r,text="Password: ",font=my_font1,bg="light yellow",fg="black")
    pw.place(x=50,y=300)

    pw_entry=Entry(frame_r,font=my_font1,bg="white",fg="black",show="*")
    pw_entry.insert(0,"password")
    pw_entry.place(x=50,y=340)
    pw_entry.bind("<FocusIn>",del5) 

    con_pw=Label(frame_r,text="Confirm Password: ",font=my_font1,bg="light yellow",fg="black")
    con_pw.place(x=355,y=300)

    cpw_try=Entry(frame_r,font=my_font1,bg="white",fg="black",show="*")
    cpw_try.insert(0,"re-enter")
    cpw_try.place(x=355,y=340)
    cpw_try.bind("<FocusIn>",del6)
    
    
      #hide and show imgs----------------------------------------------
    a=Image.open('show.png')
    a1=a.resize((20,20))
    show_img=ImageTk.PhotoImage(a1)

    b=Image.open('hide.png')
    b1=b.resize((20,20))
    hide_img=ImageTk.PhotoImage(b1)

    def hide():
       show_btn=Button(frame_r,image=show_img,command=show,bg="white",borderwidth=0,activebackground="white")
       show_btn.place(y=344,x=280)
       pw_entry.config(show="")

    def show():
       hide_btn=Button(frame_r,image=hide_img,command=hide,bg="white",borderwidth=0,activebackground="white")
       hide_btn.place(y=344,x=280)
       pw_entry.config(show="*")
    
    def hide1():
       show_btn=Button(frame_r,image=show_img,command=show1,bg="white",borderwidth=0,activebackground="white")
       show_btn.place(y=344,x=575)
       cpw_try.config(show="")

    def show1():
       hide_btn=Button(frame_r,image=hide_img,command=hide1,bg="white",borderwidth=0,activebackground="white")
       hide_btn.place(y=344,x=575)
       cpw_try.config(show="*")

    show_btn=Button(frame_r,image=show_img,command=show,bg="white",borderwidth=0,activebackground="white")
    show_btn.place(y=344,x=280)
    hide_btn=Button(frame_r,image=hide_img,command=hide,bg="white",borderwidth=0,activebackground="white")
    hide_btn.place(y=344,x=280)

    show_btn1=Button(frame_r,image=show_img,command=show1,bg="white",borderwidth=0,activebackground="white")
    show_btn1.place(y=344,x=575)

    hide_btn1=Button(frame_r,image=hide_img,command=hide1,bg="white",borderwidth=0,activebackground="white")
    hide_btn1.place(y=344,x=575)


    
    #verification function------------------------------------------------- 
    def verify():
        a=f_entry.get()
        b=l_entry.get()
        c=u_entry.get()
        d=email_try.get()
        e=pw_entry.get()
        f=cpw_try.get()
            
        if (a=="" or a=="first name") or (b=="" or b=="last name") or (c=="" or c=="Username") or (d=="" or d=="email@") or (e=="" or e=="password") or (f=="" or f=="re-enter"):
            messagebox.showerror("Signup","Something went wrong.")
        elif "@" and ".com" not in d:
            messagebox.showerror("Signup","Invalid Email")
        elif len(e)<7 or len(e)<7:
            messagebox.showerror("Signup","Password must be more than 7 characters")
        elif f!=e:
            messagebox.showerror("Signup","Passwords not match")
        else:
            form_page()
            submit()

    #sign in and login page button-------------------------------------
    global sign_in
    sign_in=Button(frame_r,text="SIGN IN",font=my_font1,bg="#22A2A2",fg="black",command=verify)
    sign_in.place(x=520,y=444)        
    global log_in
    log_in=Button(frame_r,text="Login",activebackground="#98C1D9",font=my_font,bg="#22A2A2",borderwidth=3,fg="white",command=login_page,highlightbackground="#213A5C",padx=10)
    log_in.place(x=550,y=495)   

    def submit():
        log= sqlite3.connect('register.db')

    #create cursor
        log1= log.cursor() 
    
    #insert into tables
        log1.execute("INSERT INTO signup VALUES(:f_name, :l_name, :u_name, :email, :pw)", {
            'f_name':f_entry.get(),
            'l_name':l_entry.get(),
            'u_name':u_entry.get(),
            'email':email_try.get(),
            'pw':pw_entry.get(),
            
        })
   
        log.commit()
        log.close()

    #clear entries
        f_entry.delete(0,END)
        l_entry.delete(0, END)
        u_entry.delete(0, END)
        email_try.delete(0, END)
        pw_entry.delete(0, END)
        cpw_try.delete(0,END)

        messagebox.showinfo('Registered','You have signed up successfully!')
    
  
    reg_p.mainloop()

register()