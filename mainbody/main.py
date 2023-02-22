from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from datetime import datetime
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
root = Tk()
root.title("JHI: PASA:")
root.geometry("1920x1080")

# Frame of Heading

Heading = LabelFrame(root,border=2,relief="groove",bg="cadet blue")
Heading.place(x=0,y=0,width=1920,height=55)

# Image on Heading

im = PhotoImage(file="head.png")
Label(Heading,image=im,border=0,bg="white").place(x=5,y=0)

# Name of Shop

name = Label(Heading,bg="white",fg="black",text="The Mini Mart",font=("arail italic",20,"bold"))
name.place(x=120,y=10)

# Tagline of shop

tagline = Label(Heading,bg="white",fg="black",text="Hamro Pasal Ramro Pasal",font=("arail italic",20,"bold"))
tagline.place(x=620,y=10)

# Frame for the option

frame = LabelFrame(root,border=2,relief="groove",text="Product",font=("arial",16,"bold"))
frame.place(x=180,y=140,width=1215,height=620)

# Image on Option Frame

logo = Image.open("shop.png")
image = ImageTk.PhotoImage(logo)
Label(frame,image=image).place(x=300,y=50)

# Text on Option Frame

label_enjoy = Label(frame,text="Enjoy Shopping",bg="light yellow",fg="cadet blue",font=("castellar",20,"bold"))
label_enjoy.place(x=450,y=5)

# Frame for the BUtton

Button_frame = LabelFrame(root,border=2,relief="groove",bg='cadetblue')
Button_frame.place(x=2,y=70,width=1920,height=55)


# Function to hide all frame

def HideAllFrames():
    for widget in frame.winfo_children():
        widget.destroy()

# Function of Space

def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s

# variables of Electronic

clicked_ele1 = StringVar()
clicked_ele1.set("Aurora Blue")

clicked_ele2 = StringVar()
clicked_ele2.set("Aquamarine Green")

clicked_ele3 = StringVar()
clicked_ele3.set("Black")

clicked_ele4 = StringVar()
clicked_ele4.set("black")

clicked_ele5 = StringVar()
clicked_ele5.set("Charcoal Grey")

clicked_ele6 = StringVar()
clicked_ele6.set("Shadow Black")

clicked_ele7 = StringVar()
clicked_ele7.set("Black")

clicked_ele8 = StringVar()
clicked_ele8.set("Black")

clicked_ele9 = StringVar()
clicked_ele9.set("Jet Black")

clicked_ele10 = StringVar()
clicked_ele10.set("Blue nd White")

elec_list=[]


# Image of the electronics

el_1 = Image.open("Electronics_1.jpeg")
sam = ImageTk.PhotoImage(el_1)

el_2 = Image.open("Electronics_2.jpeg")
oplus = ImageTk.PhotoImage(el_2)

el_3 = Image.open("Electronics_3.jpeg")
ear = ImageTk.PhotoImage(el_3)

el_4 = Image.open("Electronics_4.jpeg")
head = ImageTk.PhotoImage(el_4)

el_5 = Image.open("Electronics_5.jpeg")
mouse = ImageTk.PhotoImage(el_5)

el_6 = Image.open("Electronics_6.jpeg")
laptop = ImageTk.PhotoImage(el_6)

el_7 = Image.open("Electronics_7.jpeg")
acer = ImageTk.PhotoImage(el_7)

el_8 = Image.open("Electronics_8.jpeg")
slimTv = ImageTk.PhotoImage(el_8)

el_9 = Image.open("Electronics_9.jpeg")
watch = ImageTk.PhotoImage(el_9)

el_10 = Image.open("Electronics_10.jpeg")
printer = ImageTk.PhotoImage(el_10)

# Function of the electronic

def elecCall():
    HideAllFrames()

    electro_lbl = Label(frame,text="Electronics",bg="gray",fg="black",font=("times",15,"bold")).grid(row=0,column=0,padx=10)

    lf_el1 = LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_el1.place(x=120,y=10,width=200,height=280)
    el_1 = Label(lf_el1,image=sam,border=2,justify="center").place(x=60,y=0)
    nam = Label(lf_el1,text="SAMSUNG F12",font=("arial",9),justify="center").place(x=60,y=190)
    label_color1 = Label(lf_el1,text="Colour:",border=1,font=("arial",9),justify="left").place(x=0,y=215)
    price_elec1 = Label(lf_el1,text="Price:Rs.20,000",font=("arial",9,"bold")).place(x=0,y=245)
    # add_elec1 = Button(lf_el1,text="Add Items",bg="green",fg="white",font=("arial",9,"bold")).place(x=100,y=245)
    opt_el1 = ["Aurora  blue","Interstellar Black"]

    lf_el2 = LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_el2.place(x=345,y=10,width=200,height=280)
    el_2 = Label(lf_el2,image=oplus,border=2,justify="center").place(x=60,y=0)
    nam = Label(lf_el2,text="OnePLus Nord",font=("arial",9),justify="center").place(x=60,y=190)
    label_color2 = Label(lf_el2,text="Colour:",border=1,font=("arial",9),justify="left").place(x=0,y=215)
    price_elec2 = Label(lf_el2,text="Price:Rs.40,000",font=("arial",9,"bold")).place(x=0,y=245)
    # add_elec2 = Button(lf_el2,text="Add Items",bg="green",fg="white",font=("arial",9,"bold")).place(x=100,y=245)
    opt_el2 = ["Aquiamarine Green","Lunar Silver"]

    lf_el3 = LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_el3.place(x=570,y=10,width=200,height=280)
    el_3 = Label(lf_el3,image=ear,border=2,justify="center").place(x=40,y=0)
    nam = Label(lf_el3,text="Power x200",font=("arial",9),justify="center").place(x=60,y=190)
    label_color3 = Label(lf_el3,text="Colour:",border=1,font=("arial",9),justify="left").place(x=0,y=215)
    price_elec3 = Label(lf_el3,text="Price:Rs.2,000",font=("arial",9,"bold")).place(x=0,y=245)
    # add_elec3 = Button(lf_el3,text="Add Items",bg="green",fg="white",font=("arial",9,"bold")).place(x=100,y=245)
    opt_el3 = ["Black","Forest Green","Molten Orange"]

    lf_el4 = LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_el4.place(x=795,y=10,width=200,height=280)
    el_4 = Label(lf_el4,image=head,border=2,justify="center").place(x=40,y=0)
    nam = Label(lf_el4,text="JBL P234",font=("arial",9),justify="center").place(x=60,y=190)
    label_color4 = Label(lf_el4,text="Colour:",border=1,font=("arial",9),justify="left").place(x=0,y=215)
    price_elec4 = Label(lf_el4,text="Price:Rs.5000",font=("arial",9,"bold")).place(x=0,y=245)
    # add_elec4 = Button(lf_el4,text="Add Items",bg="green",fg="white",font=("arial",9,"bold")).place(x=100,y=245)
    opt_el4 = ["Black","Blue","White"]

    lf_el5 = LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_el5.place(x=1010,y=10,width=200,height=280)
    el_5 = Label(lf_el5,image=mouse,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_el5,text="Fantech F12",font=("arial",9),justify="center").place(x=60,y=190)
    label_color5 = Label(lf_el5,text="Colour:",border=1,font=("arial",9),justify="left").place(x=0,y=215)
    price_elec5 = Label(lf_el5,text="Price:Rs.2,500",font=("arial",9,"bold")).place(x=0,y=245)
    # add_elec5 = Button(lf_el5,text="Add Items",bg="green",fg="white",font=("arial",9,"bold")).place(x=100,y=245)
    opt_el5 = ["Charcoal Grey","Red","Blue"]

    lf_el6 = LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_el6.place(x=120,y=305,width=200,height=280)
    el_6 = Label(lf_el6,image=laptop,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_el6,text="Acer Nitro 5",font=("arial",9),justify="center").place(x=60,y=130)
    label_color6 = Label(lf_el6,text="Colour:",border=1,font=("arial",9),justify="left").place(x=0,y=190)
    price_elec6 = Label(lf_el6,text="Price:Rs.130,000",font=("arial",9,"bold")).place(x=0,y=160)
    # add_elec6 = Button(lf_el6,text="Add Items",bg="green",fg="white",font=("arial",9,"bold")).place(x=100,y=220)
    opt_el6 = ["Shadow Black","Fiery Red"]

    lf_el7 = LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_el7.place(x=345,y=305,width=200,height=280)
    el_7 = Label(lf_el7,image=acer,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_el7,text="Acer Swift",font=("arial",9),justify="center").place(x=60,y=130)
    label_color7 = Label(lf_el7,text="Colour:",border=1,font=("arial",9),justify="left").place(x=0,y=190)
    price_elec7 = Label(lf_el7,text="Price:Rs.70,000",font=("arial",9,"bold")).place(x=0,y=160)
    # add_elec7 = Button(lf_el7,text="Add Items",bg="green",fg="white",font=("arial",9,"bold")).place(x=100,y=220)
    opt_el7 = ["Black"]

    lf_el8 = LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_el8.place(x=570,y=305,width=200,height=280)
    el_8 = Label(lf_el8,image=slimTv,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_el8,text="Yasuda x100",font=("arial",9),justify="center").place(x=60,y=130)
    label_color8 = Label(lf_el8,text="Colour:",border=1,font=("arial",9),justify="left").place(x=0,y=190)
    price_elec8 = Label(lf_el8,text="Price:Rs.80,000",font=("arial",9,"bold")).place(x=0,y=160)
    # add_elec8 = Button(lf_el8,text="Add Items",bg="green",fg="white",font=("arial",9,"bold")).place(x=100,y=220)
    opt_el8 = ["Black"]

    lf_el9 = LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_el9.place(x=795,y=305,width=200,height=280)
    el_9 = Label(lf_el9,image=watch,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_el9,text="SO Watch",font=("arial",9),justify="center").place(x=130,y=180)
    label_color9 = Label(lf_el9,text="Colour:",border=1,font=("arial",9),justify="left").place(x=0,y=215)
    price_elec9 = Label(lf_el9,text="Price:Rs.2,000",font=("arial",9,"bold")).place(x=0,y=245)
    # add_elec9 = Button(lf_el9,text="Add Items",bg="green",fg="white",font=("arial",9,"bold")).place(x=100,y=245)
    opt_el9 = ["Jet Black","Cherry Red","Mist Grey"]

    lf_el10 = LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_el10.place(x=1010,y=305,width=200,height=280)
    el_10 = Label(lf_el10,image=printer,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_el10,text="HP Printer",font=("arial",9),justify="center").place(x=60,y=130)
    label_color10 = Label(lf_el10,text="Colour:",border=1,font=("arial",9),justify="left").place(x=0,y=190)
    price_elec10 = Label(lf_el10,text="Price:Rs.1,20,000",font=("arial",9,"bold")).place(x=0,y=160)
    # add_elec10 = Button(lf_el10,text="Add Items",bg="green",fg="white",font=("arial",9,"bold")).place(x=100,y=220)
    opt_el10 = ["blue and White"]

    global clicked_ele1,clicked_ele2,clicked_ele3,clicked_ele4,clicked_ele5,elec_list
    global clicked_ele6,clicked_ele7,clicked_ele8,clicked_ele9,clicked_ele10

    drop_elec1 = OptionMenu(lf_el1,clicked_ele1,*opt_el1).place(x=50,y=210)
    drop_elec2 = OptionMenu(lf_el2,clicked_ele2,*opt_el2).place(x=50,y=210)
    drop_elec3 = OptionMenu(lf_el3,clicked_ele3,*opt_el3).place(x=50,y=210)
    drop_elec4 = OptionMenu(lf_el4,clicked_ele4,*opt_el4).place(x=50,y=210)
    drop_elec5 = OptionMenu(lf_el5,clicked_ele5,*opt_el5).place(x=50,y=210)
    drop_elec6 = OptionMenu(lf_el6,clicked_ele6,*opt_el6).place(x=50,y=190)
    drop_elec7 = OptionMenu(lf_el7,clicked_ele7,*opt_el7).place(x=50,y=190)
    drop_elec8 = OptionMenu(lf_el8,clicked_ele8,*opt_el8).place(x=50,y=190)
    drop_elec9 = OptionMenu(lf_el9,clicked_ele9,*opt_el9).place(x=50,y=210)
    drop_elec10 = OptionMenu(lf_el10,clicked_ele10,*opt_el10).place(x=50,y=190)

    # Function for the Add items

    def AddS1():
        global elec_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            elec_list.append(["Samsung F12",20000,"20,000",clicked_ele1.get(),Spaces(40-len("Samsung F12"))])
            messagebox.showinfo("Product Status","Samsung F12 ("+clicked_ele1.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Samsung F12 ("+clicked_ele1.get()+") is not added to the cart.")

    def AddS2():
        global elec_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            elec_list.append(["OnePLus Nord",40000,"40,000",clicked_ele2.get(),Spaces(40-len("OnePLus Nord"))])
            messagebox.showinfo("Product Status","OnePlus Nord ("+clicked_ele2.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Oneplus Nord ("+clicked_ele2.get()+") is not added to the cart.")

    def AddS3():
        global elec_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            elec_list.append(["Power x200",2000,"2,000",clicked_ele3.get(),Spaces(40-len("Power x200"))])
            messagebox.showinfo("Product Status","Power x100 ("+clicked_ele3.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Power x100 ("+clicked_ele3.get()+") is not added to the cart.")

    def AddS4():
        global elec_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            elec_list.append(["JBL R234",5000,"5,000",clicked_ele4.get(),Spaces(40-len("JBL R234"))])
            messagebox.showinfo("Product Status","JBL R234 ("+clicked_ele4.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","JBL R234 ("+clicked_ele4.get()+") is not added to the cart.")

    def AddS5():
        global elec_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            elec_list.append(["Fantech F12",2500,"2,500",clicked_ele5.get(),Spaces(40-len("Fantech F12"))])
            messagebox.showinfo("Product Status","Fantech F12 ("+clicked_ele5.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Fantech F12 ("+clicked_ele5.get()+") is not added to the cart.")

    def AddS6():
        global elec_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            elec_list.append(["Acer Nitro 5",130000,"1,30,000",clicked_ele6.get(),Spaces(40-len("Acer Nitro 5"))])
            messagebox.showinfo("Product Status","Acer Nitro 5 ("+clicked_ele7.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Acer Nitro 5 ("+clicked_ele6.get()+") is not added to the cart.")

    def AddS7():
        global elec_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            elec_list.append(["Acer Swift",70000,"70,000",clicked_ele7.get(),Spaces(40-len("Acer Swift"))])
            messagebox.showinfo("Product Status","Acer Swift ("+clicked_ele7.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Acer Swift ("+clicked_ele7.get()+") is not added to the cart.")

    def AddS8():
        global elec_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            elec_list.append(["Yasuda x100",80000,"80,000",clicked_ele8.get(),Spaces(40-len("Yasuda x100"))])
            messagebox.showinfo("Product Status","Yasuda x100 ("+clicked_ele9.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Yasuda x100 ("+clicked_ele8.get()+") is not added to the cart.")

    def AddS9():
        global elec_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            elec_list.append(["So Watch",2000,"2,000",clicked_ele9.get(),Spaces(40-len("So Watch"))])
            messagebox.showinfo("Product Status","So Watch ("+clicked_ele9.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","So Watch ("+clicked_ele9.get()+") is not added to the cart.")

    def AddS10():
        global elec_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            elec_list.append(["HP Printer",120000,"1,20,000",clicked_ele10.get(),Spaces(40-len("HP Printer"))])
            messagebox.showinfo("Product Status","HP Printer ("+clicked_ele10.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","HP Printer ("+clicked_ele10.get()+") is not added to the cart.")



    # Button for the Add items
    add_elec1 = Button(lf_el1,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddS1).place(x=100,y=245)
    add_elec2 = Button(lf_el2,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddS2).place(x=100,y=245)
    add_elec3 = Button(lf_el3,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddS3).place(x=100,y=245)
    add_elec4 = Button(lf_el4,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddS4).place(x=100,y=245)
    add_elec5 = Button(lf_el5,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddS5).place(x=100,y=245)
    add_elec6 = Button(lf_el6,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddS6).place(x=60,y=225)
    add_elec7 = Button(lf_el7,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddS7).place(x=60,y=225)
    add_elec8 = Button(lf_el8,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddS8).place(x=60,y=225)
    add_elec9 = Button(lf_el9,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddS9).place(x=100,y=245)
    add_elec10 = Button(lf_el10,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddS10).place(x=60,y=225)

    
#Button of Electronic
elec_btn = Button(Button_frame,bg="light yellow",fg="black",border=2,text="Electronic",font=("times",19,"bold"),activebackground="light blue",command=elecCall)
elec_btn.place(x=0,y=0,width=305)


# Variables of Grocery

clicked_gro1 = StringVar()
clicked_gro1.set("250g-Rs.100")

clicked_gro2 = StringVar()
clicked_gro2.set("5Kg-Rs.500")

clicked_gro3 = StringVar()
clicked_gro3.set("1kg-Rs.30")

clicked_gro4 = StringVar()
clicked_gro4.set("1L-Rs.180")

clicked_gro5 = StringVar()
clicked_gro5.set("500g-Rs.170")

clicked_gro6 = StringVar()
clicked_gro6.set("120g-Rs.50")

clicked_gro7 = StringVar()
clicked_gro7.set("200g-Rs.250")

clicked_gro8 = StringVar()
clicked_gro8.set("500g-Rs.200")

clicked_gro9 = StringVar()
clicked_gro9.set("70g-Rs.50")

clicked_gro10 = StringVar()
clicked_gro10.set("70g-Rs.50")

grocery_list = []


# Image of grocery


gr_1 = Image.open("Grocery_1.jpg")
corn = ImageTk.PhotoImage(gr_1)

gr_2 = Image.open("Grocery_2.jpeg")
atta = ImageTk.PhotoImage(gr_2)

gr_3 = Image.open("Grocery_3.jpeg")
rice = ImageTk.PhotoImage(gr_3)

gr_4 = Image.open("Grocery_4.jpeg")
oil = ImageTk.PhotoImage(gr_4)

gr_5 = Image.open("Grocery_5.jpeg")
dal = ImageTk.PhotoImage(gr_5)

gr_6 = Image.open("Grocery_6.jpeg")
noodle = ImageTk.PhotoImage(gr_6)

gr_7 = Image.open("Grocery_7.jpeg")
jam = ImageTk.PhotoImage(gr_7)

gr_8 = Image.open("Grocery_8.jpeg")
pick = ImageTk.PhotoImage(gr_8)

gr_9 = Image.open("Grocery_9.jpg")
chip = ImageTk.PhotoImage(gr_9)

gr_9 = Image.open("Grocery_10.jpg")
kur = ImageTk.PhotoImage(gr_9)

# Function for the Grocery


def groceryCall():
    HideAllFrames()

    go_lbl = Label(frame,text="Grocery",bg="gray",fg="black",font=("times",15,"bold")).grid(row=0,column=0,padx=10)

    lf_gc1= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_gc1.place(x=120,y=10,width=200,height=280)
    el_1 = Label(lf_gc1,image=corn,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_gc1,text="Corn Flakes",font=("arial",9),justify="center").place(x=60,y=190)
    label_color1 = Label(lf_gc1,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=230)
    opt_ge1 = ["250g - Rs.100","475g - Rs.345"]

    lf_gc2= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_gc2.place(x=345,y=10,width=200,height=280)
    el_2 = Label(lf_gc2,image=atta,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_gc2,text="Aashirwad Atta",font=("arial",9),justify="center").place(x=60,y=190)
    label_color2 = Label(lf_gc2,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=230)
    opt_ge2 = ["5kg - Rs.500","10Kg - Rs.1200"]

    lf_gc3= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_gc3.place(x=570,y=10,width=200,height=280)
    el_3 = Label(lf_gc3,image=rice,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_gc3,text="Tata Salt",font=("arial",9),justify="center").place(x=60,y=190)
    label_color3 = Label(lf_gc3,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=230)
    opt_ge3 = ["1Kg - Rs.30"]

    lf_gc4= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_gc4.place(x=795,y=10,width=200,height=280)
    el_4 = Label(lf_gc4,image=oil,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_gc4,text="Groundnut Oil",font=("arial",9),justify="center").place(x=60,y=190)
    label_color4 = Label(lf_gc4,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=230)
    opt_ge4 = ["1L - Rs.180"]

    lf_gc5= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_gc5.place(x=1010,y=10,width=200,height=280)
    el_5 = Label(lf_gc5,image=dal,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_gc5,text="Toor Dal",font=("arial",9),justify="center").place(x=60,y=190)
    label_color5 = Label(lf_gc5,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=230)
    opt_ge5 = ["500g - Rs.170"]

    lf_gc6= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_gc6.place(x=120,y=305,width=200,height=280)
    el_6 = Label(lf_gc6,image=noodle,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_gc6,text="Yippee Noodles",font=("arial",9),justify="center").place(x=60,y=190)
    label_color6 = Label(lf_gc6,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=230)
    opt_ge6 = ["120g - Rs.50","250g - Rs.120"]

    lf_gc7= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_gc7.place(x=345,y=305,width=200,height=280)
    el_7 = Label(lf_gc7,image=jam,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_gc7,text="Kissan Mixed Jam",font=("arial",9),justify="center").place(x=60,y=190)
    label_color7 = Label(lf_gc7,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=230)
    opt_ge7 = ["200g - Rs.250","500g - Rs.450"]

    lf_gc8= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_gc8.place(x=570,y=305,width=200,height=280)
    el_8 = Label(lf_gc8,image=pick,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_gc8,text="Mother Recipe pickel",font=("arial",9),justify="center").place(x=60,y=190)
    label_color8 = Label(lf_gc8,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=230)
    opt_ge8 = ["500g - Rs.200","1Kg - Rs.450"]

    lf_gc9= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_gc9.place(x=795,y=305,width=200,height=280)
    el_9 = Label(lf_gc9,image=chip,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_gc9,text="Cream & Onion Chips",font=("arial",9),justify="center").place(x=60,y=190)
    label_color9 = Label(lf_gc9,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=230)
    opt_ge9 = ["250g - Rs.50","150g - Rs.110"]

    lf_gc10= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_gc10.place(x=1010,y=305,width=200,height=280)
    el_10 = Label(lf_gc10,image=kur,border=2,bg='white',justify="center").place(x=30,y=0)
    nam = Label(lf_gc10,text="KurKure",font=("arial",9),justify="center").place(x=60,y=190)
    label_color10 = Label(lf_gc10,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=220)
    opt_ge10 = ["250g - Rs.50","150g - Rs.110"]

    global clicked_gro1,clicked_gro2,clicked_gro3,clicked_gro4,clicked_gro5,grocery_list
    global clicked_gro6,clicked_gro7,clicked_gro8,clicked_gro9,clicked_gro10


    drop_gy1 = OptionMenu(lf_gc1,clicked_gro1,*opt_ge1).place(x=40,y=220)
    drop_gy2 = OptionMenu(lf_gc2,clicked_gro2,*opt_ge2).place(x=40,y=220)
    drop_gy3 = OptionMenu(lf_gc3,clicked_gro3,*opt_ge3).place(x=40,y=220)
    drop_gy4 = OptionMenu(lf_gc4,clicked_gro4,*opt_ge4).place(x=40,y=220)
    drop_gy5 = OptionMenu(lf_gc5,clicked_gro5,*opt_ge5).place(x=40,y=220)
    drop_gy6 = OptionMenu(lf_gc6,clicked_gro6,*opt_ge6).place(x=40,y=220)
    drop_gy7 = OptionMenu(lf_gc7,clicked_gro7,*opt_ge7).place(x=40,y=220)
    drop_gy8 = OptionMenu(lf_gc8,clicked_gro8,*opt_ge8).place(x=40,y=220)
    drop_gy9 = OptionMenu(lf_gc9,clicked_gro9,*opt_ge9).place(x=40,y=220)
    drop_gy10 = OptionMenu(lf_gc10,clicked_gro10,*opt_ge10).place(x=40,y=220)
    
# Function of the Grocery price

    def GroceryPrice(s):
        s1 = ""
        for i in range(len(s)-1,0,-1):
            if s[i]!=".":
                s1 = s1+s[i]
            else:
                break
        return int(s1[::-1])

# Funtion of the Grocery Qty

    def GroceryQty(s):
        s1 = "" 
        for i in range(len(s)):
            s1 = s1+s[i]
            if s[i]=="g" or s[i]=="L":
                break
        return s1          

# Function To Add the item on grocery

    def AddG1():
        global grocery_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Corn Flakes",GroceryPrice(clicked_gro1.get()),GroceryQty(clicked_gro1.get()),Spaces(40-len("Corn Flakes"))])
            messagebox.showinfo("Product Status","Corn Flakes ("+clicked_gro1.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Corn Flakes ("+clicked_gro1.get()+") is not added to the cart.")


    def AddG2():
        global grocery_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Aashirwad Atta",GroceryPrice(clicked_gro2.get()),GroceryQty(clicked_gro2.get()),Spaces(40-len("Aashirwad Atta"))])
            messagebox.showinfo("Product Status","Aashirwad Atta ("+clicked_gro2.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Aashirwad Atta ("+clicked_gro2.get()+") is not added to the cart.")


    def AddG3():
        global grocery_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Tata Salt",GroceryPrice(clicked_gro3.get()),GroceryQty(clicked_gro3.get()),Spaces(40-len("Tata Salt"))])
            messagebox.showinfo("Product Status","Tata Salt ("+clicked_gro3.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Tata Salt ("+clicked_gro3.get()+") is not added to the cart.")


    def AddG4():
        global grocery_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Groundnut Oil",GroceryPrice(clicked_gro4.get()),GroceryQty(clicked_gro4.get()),Spaces(40-len("Groundnut Oil"))])
            messagebox.showinfo("Product Status","Groundnut Oil ("+clicked_gro4.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Groundnut Oil("+clicked_gro4.get()+") is not added to the cart.")

    def AddG5():
        global grocery_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Toor Dal",GroceryPrice(clicked_gro5.get()),GroceryQty(clicked_gro5.get()),Spaces(40-len("Toor Dal"))])
            messagebox.showinfo("Product Status","Toor Dal ("+clicked_gro5.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Toor Dal ("+clicked_gro5.get()+") is not added to the cart.")


    def AddG6():
        global grocery_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Yippee Noodles",GroceryPrice(clicked_gro6.get()),GroceryQty(clicked_gro6.get()),Spaces(40-len("Yippee Noodles"))])
            messagebox.showinfo("Product Status","Yippee Noodles ("+clicked_gro6.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Yippee Noodles ("+clicked_gro6.get()+") is not added to the cart.")



    def AddG7():
        global grocery_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Mixed Jam",GroceryPrice(clicked_gro7.get()),GroceryQty(clicked_gro7.get()),Spaces(40-len("Mixed Jam"))])
            messagebox.showinfo("Product Status","Mixed Jam ("+clicked_gro7.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Mixed Jam ("+clicked_gro7.get()+") is not added to the cart.")


    def AddG8():
        global grocery_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Mother Repice Pickle",GroceryPrice(clicked_gro8.get()),GroceryQty(clicked_gro8.get()),Spaces(40-len("Mother Repice Pickle"))])
            messagebox.showinfo("Product Status","Mother Repice Pickle ("+clicked_gro8.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Mother Repice Pickle ("+clicked_gro8.get()+") is not added to the cart.")


    def AddG9():
        global grocery_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["Cream & Onion Chips",GroceryPrice(clicked_gro9.get()),GroceryQty(clicked_gro9.get()),Spaces(40-len("Cream & Onion Chips"))])
            messagebox.showinfo("Product Status","Cream & Onion Chips ("+clicked_gro9.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Cream & Onion Chips ("+clicked_gro9.get()+") is not added to the cart.")   

    def AddG10():
        global grocery_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            grocery_list.append(["KurKure",GroceryPrice(clicked_gro10.get()),GroceryQty(clicked_gro10.get()),Spaces(40-len("Kurkure"))])
            messagebox.showinfo("Product Status","Kurkure ("+clicked_gro10.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Kurkure ("+clicked_gro10.get()+") is not added to the cart.")   

 # Button to Add the items of Grocery

    add_goc1 = Button(lf_gc1,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddG1).place(x=125,y=250)
    add_goc2 = Button(lf_gc2,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddG2).place(x=125,y=250)
    add_goc3 = Button(lf_gc3,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddG3).place(x=125,y=250)
    add_goc4 = Button(lf_gc4,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddG4).place(x=125,y=250)
    add_goc5 = Button(lf_gc5,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddG5).place(x=125,y=250)
    add_goc6 = Button(lf_gc6,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddG6).place(x=125,y=250)
    add_goc7 = Button(lf_gc7,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddG7).place(x=125,y=250)
    add_goc8 = Button(lf_gc8,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddG8).place(x=125,y=250)
    add_goc9 = Button(lf_gc9,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddG9).place(x=125,y=250)
    add_goc10 = Button(lf_gc10,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddG10).place(x=125,y=250)

# Button of the Grocery Frame

Gro_btn = Button(Button_frame,bg="light yellow",fg="black",border=2,text="Grocery",font=("times",19,"bold"),activebackground="light blue",command=groceryCall)
Gro_btn.place(x=305,y=0,width=305)

# Variable of Sports and Gym

sportsgym_list = []

# Image for the Sport and Gym

sg_1 = Image.open("SportsGym_1.jpg")
bat = ImageTk.PhotoImage(sg_1)

sg_2 = Image.open("SportsGym_2.jpg")
ball = ImageTk.PhotoImage(sg_2)

sg_3 = Image.open("SportsGym_3.jpg")
coc = ImageTk.PhotoImage(sg_3)

sg_4 = Image.open("SportsGym_4.jpg")
feat = ImageTk.PhotoImage(sg_4)

sg_5 = Image.open("SportsGym_5.jpg")
tt = ImageTk.PhotoImage(sg_5)

sg_6 = Image.open("SportsGym_6.jpg")
mill = ImageTk.PhotoImage(sg_6)

sg_7 = Image.open("SportsGym_7.jpg")
dum = ImageTk.PhotoImage(sg_7)

sg_8 = Image.open("SportsGym_8.jpg")
bp = ImageTk.PhotoImage(sg_8)

sg_9 = Image.open("SportsGym_9.jpg")
cycle = ImageTk.PhotoImage(sg_9)

sg_10 = Image.open("SportsGym_10.jpg")
punch = ImageTk.PhotoImage(sg_10)

# Function of the Sport and Gym

def SportGymcall():
    HideAllFrames()

    sp_lbl = Label(frame,text="Sports & Gym",bg="gray",fg="black",font=("times",15,"bold")).grid(row=0,column=0,padx=10)

    lf_so1= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_so1.place(x=140,y=10,width=200,height=280)
    el_1 = Label(lf_so1,image=bat,border=2,justify="center").place(x=40,y=0)
    nam = Label(lf_so1,text="GM Cricket Bat",font=("arial",9),justify="center").place(x=60,y=200)
    label_color1 = Label(lf_so1,text="Price : Rs.8,000",border=1,font=("arial",9),justify="left").place(x=0,y=230)
   

    lf_so2= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_so2.place(x=360,y=10,width=200,height=280)
    el_2 = Label(lf_so2,image=ball,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_so2,text="Cricket Ball",font=("arial",9),justify="center").place(x=60,y=190)
    label_color2 = Label(lf_so2,text="Price : Rs.800",border=1,font=("arial",9),justify="left").place(x=5,y=220)
   
    lf_so3= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_so3.place(x=575,y=10,width=200,height=280)
    el_3 = Label(lf_so3,image=coc,border=2,justify="center").place(x=30,y=0)
    nam = Label(lf_so3,text="Badminton",font=("arial",9),justify="center").place(x=60,y=200)
    label_color3 = Label(lf_so3,text="Price : Rs.5,000",border=1,font=("arial",9),justify="left").place(x=0,y=230)
   
    lf_so4= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_so4.place(x=795,y=10,width=200,height=280)
    el_4 = Label(lf_so4,image=feat,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_so4,text="Badminton cock",font=("arial",9),justify="center").place(x=50,y=200)
    label_color4 = Label(lf_so4,text="Price : Rs.100",border=1,font=("arial",9),justify="left").place(x=0,y=230)
   
    lf_so5= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_so5.place(x=1010,y=10,width=200,height=280)
    el_5 = Label(lf_so5,image=tt,border=2,justify="center").place(x=40,y=0)
    nam = Label(lf_so5,text="T-tennis Bat",font=("arial",9),justify="center").place(x=60,y=200)
    label_color5 = Label(lf_so5,text="Price : Rs.2000",border=1,font=("arial",9),justify="left").place(x=0,y=230)
   
    lf_so6= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_so6.place(x=140,y=305,width=200,height=280)
    el_6 = Label(lf_so6,image=mill,border=2,justify="center").place(x=10,y=10)
    nam = Label(lf_so6,text="Treadmill",font=("arial",9),justify="center").place(x=60,y=170)
    label_color6 = Label(lf_so6,text="Price : Rs.80,000",border=1,font=("arial",9),justify="left").place(x=0,y=200)
   
    lf_so7= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_so7.place(x=360,y=305,width=200,height=280)
    el_7 = Label(lf_so7,image=dum,border=2,justify="center").place(x=10,y=20)
    nam = Label(lf_so7,text="Dumb Bell",font=("arial",9),justify="center").place(x=60,y=150)
    label_color7 = Label(lf_so7,text="Price : Rs.10,000",border=1,font=("arial",9),justify="left").place(x=0,y=180)
   
    lf_so8= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_so8.place(x=575,y=305,width=200,height=280)
    el_8 = Label(lf_so8,image=bp,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_so8,text="Bench Press",font=("arial",9),justify="center").place(x=60,y=170)
    label_color8 = Label(lf_so8,text="Price : Rs.18,000",border=1,font=("arial",9),justify="left").place(x=0,y=220)
   
    lf_so9= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_so9.place(x=795,y=305,width=200,height=280)
    el_9 = Label(lf_so9,image=cycle,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_so9,text="Exercise Cycle",font=("arial",9),justify="center").place(x=60,y=200)
    label_color9 = Label(lf_so9,text="Price : Rs.50,000",border=1,font=("arial",9),justify="left").place(x=0,y=230)
   
    lf_so10= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_so10.place(x=1010,y=305,width=200,height=280)
    el_10 = Label(lf_so10,image=punch,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_so10,text="Punching Bag",font=("arial",9),justify="center").place(x=60,y=200)
    label_color10 = Label(lf_so10,text="Price : Rs.12,000",border=1,font=("arial",9),justify="left").place(x=0,y=230)
   
# Function to Add items of Sport and Gym in Cart

    def AddY1():
        global sportsgym_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["GM Cricket Bat",8000,"8,000",Spaces(40-len("GM Cricket Bat"))])
            messagebox.showinfo("Product Status","GM Purist Kw 202 is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","GM Purist kw 202 is not added to the cart.")

    def AddY2():
        global sportsgym_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["GM Cricket Ball",800,"800",Spaces(40-len("GM Cricket Ball"))])
            messagebox.showinfo("Product Status","GM Circket Ball 2 is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","GM Circket Ball 2 is not added to the cart.")

    def AddY3():
        global sportsgym_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Badminton",5000,"5,000",Spaces(40-len("Badminton"))])
            messagebox.showinfo("Product Status","badminton is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","badminton is not added to the cart.")

    def AddY4():
        global sportsgym_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Badminton cock",100,"100",Spaces(40-len("Badminton cock"))])
            messagebox.showinfo("Product Status","Badminton is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Badminton is not added to the cart.")

    def AddY5():
        global sportsgym_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Table tennis",2000,"2,000",Spaces(40-len("Table Tennis"))])
            messagebox.showinfo("Product Status","Table Tennis is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Table Tennis is not added to the cart.")

    def AddY6():
        global sportsgym_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Treadmill",80000,"80,000",Spaces(40-len("Treadmill"))])
            messagebox.showinfo("Product Status","Treadmill is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Treadmill is not added to the cart.")

    def AddY7():
        global sportsgym_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Dumb bell",10000,"10,000",Spaces(40-len("Dumb bell"))])
            messagebox.showinfo("Product Status","Dumb bell is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Dumb bell is not added to the cart.")

    def AddY8():
        global sportsgym_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Bench Press",18000,"18,000",Spaces(40-len("Bench Press"))])
            messagebox.showinfo("Product Status","Bench Press is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Bench Press is not added to the cart.")


    def AddY9():
        global sportsgym_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Exercise Cycle",50000,"50,000",Spaces(40-len("Exercise Cycle"))])
            messagebox.showinfo("Product Status","Exercise Cycle is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Exercise Cycle is not added to the cart.")

    def AddY10():
        global sportsgym_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            sportsgym_list.append(["Punching Bag",12000,"12,000",Spaces(40-len("Punching Bag"))])
            messagebox.showinfo("Product Status","Punching Bag is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Punching Bag is not added to the cart.")


# Button for the Add Items on Sports and Gym

    add_sm1 = Button(lf_so1,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddY1).place(x=110,y=230)
    add_sm2 = Button(lf_so2,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddY2).place(x=110,y=230)
    add_sm3 = Button(lf_so3,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddY3).place(x=110,y=230)
    add_sm4 = Button(lf_so4,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddY4).place(x=110,y=230)
    add_sm5 = Button(lf_so5,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddY5).place(x=110,y=230)
    add_sm6 = Button(lf_so6,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddY6).place(x=110,y=230)
    add_sm7 = Button(lf_so7,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddY7).place(x=110,y=230)
    add_sm8 = Button(lf_so8,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddY8).place(x=110,y=230)
    add_sm9 = Button(lf_so9,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddY9).place(x=110,y=230)
    add_sm10 = Button(lf_so10,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddY10).place(x=110,y=230)

# Button for the Sport and Gym in Button Frame

Spg_btn = Button(Button_frame,bg="light yellow",fg="black",border=2,text="Sports & Gym",font=("times",19,"bold"),activebackground="light blue",command=SportGymcall)
Spg_btn.place(x=610,y=0,width=305)


# Variables of Furniture

Furni_list = []

# Image of the Furniture in Frame 

fu_1 = Image.open("Furniture_1.jpeg")
cup = ImageTk.PhotoImage(fu_1)

fu_2 = Image.open("Furniture_2.jpg")
door = ImageTk.PhotoImage(fu_2)

fu_3 = Image.open("Furniture_3.jpeg")
board = ImageTk.PhotoImage(fu_3)

fu_4 = Image.open("Furniture_4.jpeg")
bed = ImageTk.PhotoImage(fu_4)

fu_5 = Image.open("Furniture_5.jpeg")
largeb = ImageTk.PhotoImage(fu_5)

fu_6 = Image.open("Furniture_6.jpg")
Ttable = ImageTk.PhotoImage(fu_6)

fu_7 = Image.open("Furniture_7.jpg")
lagret = ImageTk.PhotoImage(fu_7)

fu_8 = Image.open("Furniture_8.jpeg")
sofa = ImageTk.PhotoImage(fu_8)

fu_9 = Image.open("Furniture_9.jpg")
coach = ImageTk.PhotoImage(fu_9)

fu_10 = Image.open("Furniture_10.jpg")
dinning = ImageTk.PhotoImage(fu_10)

# Function for the Furniture

def FurniCall():
    HideAllFrames()

    Fu_lbl = Label(frame,text="Furniture",bg="gray",fg="black",font=("times",15,"bold")).grid(row=0,column=0,padx=10)

    lf_fr1= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_fr1.place(x=120,y=10,width=200,height=280)
    el_1 = Label(lf_fr1,image=cup,border=2,justify="center").place(x=40,y=0)
    nam = Label(lf_fr1,text="Julian Wood 2 Door",font=("arial",9),justify="center").place(x=60,y=200)
    label_color1 = Label(lf_fr1,text="Price : Rs.18,000",border=1,font=("arial",9),justify="left").place(x=0,y=230) 

    lf_fr2= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_fr2.place(x=345,y=10,width=200,height=280)
    el_2 = Label(lf_fr2,image=door,border=2,justify="center").place(x=40,y=0)
    nam = Label(lf_fr2,text="Shoes Closet",font=("arial",9),justify="center").place(x=60,y=200)
    label_color2 = Label(lf_fr2,text="Price : Rs.2,500",border=1,font=("arial",9),justify="left").place(x=0,y=230) 

    lf_fr3= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_fr3.place(x=570,y=10,width=200,height=280)
    el_3 = Label(lf_fr3,image=board,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_fr3,text="Tv - Stand",font=("arial",9),justify="center").place(x=60,y=150)
    label_color3 = Label(lf_fr3,text="Price : Rs.70,000",border=1,font=("arial",9),justify="left").place(x=0,y=190) 

    lf_fr4= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_fr4.place(x=795,y=10,width=200,height=280)
    el_4 = Label(lf_fr4,image=bed,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_fr4,text="Modren Coach",font=("arial",9),justify="center").place(x=60,y=150)
    label_color4 = Label(lf_fr4,text="Price : Rs.1,40,000",border=1,font=("arial",9),justify="left").place(x=0,y=190) 

    lf_fr5= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_fr5.place(x=1010,y=10,width=200,height=280)
    el_5 = Label(lf_fr5,image=largeb,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_fr5,text="Wooden Kitchen Dinning",font=("arial",9),justify="center").place(x=30,y=150)
    label_color5 = Label(lf_fr5,text="Price : Rs.55,000",border=1,font=("arial",9),justify="left").place(x=0,y=190) 

    lf_fr6= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_fr6.place(x=120,y=305,width=200,height=280)
    el_6 = Label(lf_fr6,image=Ttable,border=2,justify="center").place(x=40,y=0)
    nam = Label(lf_fr6,text="Reading Table",font=("arial",9),justify="center").place(x=45,y=200)
    label_color6 = Label(lf_fr6,text="Price : Rs.25,000",border=1,font=("arial",9),justify="left").place(x=0,y=230) 

    lf_fr7= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_fr7.place(x=345,y=305,width=200,height=280)
    el_7 = Label(lf_fr7,image=lagret,border=2,justify="center").place(x=40,y=0)
    nam = Label(lf_fr7,text="Bed mattress",font=("arial",9),justify="center").place(x=50,y=200)
    label_color7 = Label(lf_fr7,text="Price : Rs.12,000",border=1,font=("arial",9),justify="left").place(x=0,y=230) 

    lf_fr8= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_fr8.place(x=570,y=305,width=200,height=280)
    el_8 = Label(lf_fr8,image=sofa,border=2,justify="center").place(x=10,y=10)
    nam = Label(lf_fr8,text="Wooden Modern Bed",font=("arial",9),justify="center").place(x=30,y=150)
    label_color8 = Label(lf_fr8,text="Price : Rs.60,000",border=1,font=("arial",9),justify="left").place(x=0,y=180) 

    lf_fr9= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_fr9.place(x=795,y=305,width=200,height=280)
    el_9 = Label(lf_fr9,image=coach,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_fr9,text="Clothes Hanger",font=("arial",9),justify="center").place(x=60,y=200)
    label_color9 = Label(lf_fr9,text="Price : Rs.16,000",border=1,font=("arial",9),justify="left").place(x=0,y=230) 

    lf_fr10= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_fr10.place(x=1010,y=305,width=200,height=280)
    el_10 = Label(lf_fr10,image=dinning,border=2,justify="center").place(x=40,y=0)
    nam = Label(lf_fr10,text="Simple Chair",font=("arial",9),justify="center").place(x=50,y=200)
    label_color10 = Label(lf_fr10,text="Price : Rs.5,000",border=1,font=("arial",9),justify="left").place(x=0,y=230) 

# Function for the Add items in Furniture in Cart

    def AddF1():
        global Furni_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Furni_list.append(["Julian wood 2 Door",18000,"18,000",Spaces(40-len("JUlian wood 2 Door"))])
            messagebox.showinfo("Product Status","Julian wood 2 Door is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Julian wood 2 Door is not added to the cart.")



    def AddF2():
        global Furni_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Furni_list.append(["Shoes Closet",2500,"2,500",Spaces(40-len("Shoes closet"))])
            messagebox.showinfo("Product Status","Shoes Closet is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Shoes Closet is not added to the cart.")


    def AddF3():
        global Furni_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Furni_list.append(["Tv - Stand",70000,"70,000",Spaces(40-len("Tv - Stand"))])
            messagebox.showinfo("Product Status","Tv - Stand is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Tv - Stand is not added to the cart.")

    def AddF4():
        global Furni_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Furni_list.append(["Modern Coach",140000,"1,40,000",Spaces(40-len("Modern Coach"))])
            messagebox.showinfo("Product Status","Modern Coach is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Modern Coach is not added to the cart.")

    def AddF5():
        global Furni_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Furni_list.append(["Modern kitchen Dinning",50000,"50,000",Spaces(40-len("Modern Kitchen Dinning"))])
            messagebox.showinfo("Product Status","Modern kitchen Dinning is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Modern kitchen Dinning is not added to the cart.")

    def AddF6():
        global Furni_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Furni_list.append(["Reading Table",25000,"25,000",Spaces(40-len("Reading Table"))])
            messagebox.showinfo("Product Status","Reading Table is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Reading Table is not added to the cart.")

    def AddF7():
        global Furni_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Furni_list.append(["Bed Mattress",12000,"12,000",Spaces(40-len("Bed Mattress"))])
            messagebox.showinfo("Product Status","Bed Mattress is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Bed Mattress is not added to the cart.")

    def AddF8():
        global Furni_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Furni_list.append(["Wooden Modern Bed ",60000,"60,000",Spaces(40-len("JWooden Modern Bed"))])
            messagebox.showinfo("Product Status","Wooden Modern Bed is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Wooden Modern Bed is not added to the cart.")

    def AddF9():
        global Furni_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Furni_list.append(["Clothes Hanger",16000,"16,000",Spaces(40-len("Clothes Hanger"))])
            messagebox.showinfo("Product Status","Clothes Hanger is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Clothes Hanger is not added to the cart.")

    def AddF10():
        global Furni_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Furni_list.append(["Simple Chair",5000,"5,000",Spaces(40-len("Simple Chair"))])
            messagebox.showinfo("Product Status","Simple Chair is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Simple Chair is not added to the cart.")

    
# Button to add the item on Cart

    add_fn1 = Button(lf_fr1,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddF1).place(x=110,y=230)
    add_fn2 = Button(lf_fr2,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddF2).place(x=110,y=230)
    add_fn3 = Button(lf_fr3,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddF3).place(x=60,y=230)
    add_fn4 = Button(lf_fr4,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddF4).place(x=60,y=230)
    add_fn5 = Button(lf_fr5,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddF5).place(x=60,y=230)
    add_fn6 = Button(lf_fr6,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddF6).place(x=110,y=230)
    add_fn7 = Button(lf_fr7,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddF7).place(x=110,y=230)
    add_fn8 = Button(lf_fr8,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddF8).place(x=60,y=230)
    add_fn9 = Button(lf_fr9,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddF9).place(x=110,y=230)
    add_fn10 = Button(lf_fr10,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddF10).place(x=110,y=230)
    

# Button of Furniture on Button Frame

Furn_btn = Button(Button_frame,bg="light yellow",fg="black",border=2,text="Furniture",font=("times",19,"bold"),activebackground="light blue",command=FurniCall)
Furn_btn.place(x=915,y=0,width=305)

# Variables of Fruit and Vegetables

clicked_FV1 = StringVar()
clicked_FV1.set("1Kg-Rs.240")

clicked_FV2 = StringVar()
clicked_FV2.set("1 Dozen-Rs.190")

clicked_FV3 = StringVar()
clicked_FV3.set("1kg-Rs.400")

clicked_FV4 = StringVar()
clicked_FV4.set("1Kg-Rs.220")

clicked_FV5 = StringVar()
clicked_FV5.set("1Kg-Rs.400")

clicked_FV6 = StringVar()
clicked_FV6.set("1 Piece -Rs.30")

clicked_FV7 = StringVar()
clicked_FV7.set("1Kg-Rs.200")

clicked_FV8 = StringVar()
clicked_FV8.set("1g-Rs.250")

clicked_FV9 = StringVar()
clicked_FV9.set("1Kg-Rs.150")

clicked_FV10 = StringVar()
clicked_FV10.set("1Kg-Rs.50")

FruV_list = []

# Image of Vegetables and Fruits for the Frame

VF_1 = Image.open("fruits_1.jpg")
apple = ImageTk.PhotoImage(VF_1)

VF_2 = Image.open("fruits_2.jpg")
ban = ImageTk.PhotoImage(VF_2)

VF_3 = Image.open("fruits_3.jpg")
gra = ImageTk.PhotoImage(VF_3)

VF_4 = Image.open("fruits_4.jpg")
oran = ImageTk.PhotoImage(VF_4)

VF_5 = Image.open("fruits_5.jpg")
pom = ImageTk.PhotoImage(VF_5)

VF_6 = Image.open("vegetables_1.png")
spa = ImageTk.PhotoImage(VF_6)

VF_7 = Image.open("vegetables_2.png")
Oni = ImageTk.PhotoImage(VF_7)

VF_8 = Image.open("vegetables_3.jpg")
car = ImageTk.PhotoImage(VF_8)

VF_9 = Image.open("vegetables_4.jpg")
cuc = ImageTk.PhotoImage(VF_9)

VF_10 = Image.open("vegetables_5.jpg")
zero = ImageTk.PhotoImage(VF_10)

# Function of the Fruits and Vegetables in Product Frame

def VegeFruCall():
    HideAllFrames()

    Ve_lbl = Label(frame,text="Fruits & Vegetables",bg="gray",fg="black",font=("times",15,"bold")).grid(row=0,column=0,padx=10)

    lf_vf1= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_vf1.place(x=120,y=30,width=200,height=250)
    el_1 = Label(lf_vf1,image=apple,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_vf1,text="Mustang apple",font=("arial",9),justify="center").place(x=60,y=130)
    label_color1 = Label(lf_vf1,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=160)
    opt_ve1 = ["1Kg - Rs.240","2.5Kg - Rs.600"]

    lf_vf2= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_vf2.place(x=345,y=10,width=200,height=280)
    el_2 = Label(lf_vf2,image=ban,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_vf2,text="Indian Banana",font=("arial",9),justify="center").place(x=60,y=130)
    label_color1 = Label(lf_vf2,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=160)
    opt_ve2 = ["1 Dozen - Rs.190","1 gharr - Rs.1200"]

    lf_vf3= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_vf3.place(x=570,y=10,width=200,height=280)
    el_3 = Label(lf_vf3,image=gra,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_vf3,text="Nepali Grapes",font=("arial",9),justify="center").place(x=60,y=130)
    label_color3 = Label(lf_vf3,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=160)
    opt_ve3 = ["1Kg - Rs.400","5Kg - Rs.2000"]

    lf_vf4= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_vf4.place(x=795,y=10,width=200,height=280)
    el_4 = Label(lf_vf4,image=oran,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_vf4,text="Gorkha Orange",font=("arial",9),justify="center").place(x=60,y=130)
    label_color4 = Label(lf_vf4,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=160)
    opt_ve4 = ["1Kg - Rs.200","2.5Kg - Rs.100"]

    lf_vf5= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_vf5.place(x=1010,y=10,width=200,height=280)
    el_5 = Label(lf_vf5,image=pom,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_vf5,text="Chinese Pomegranate",font=("arial",9),justify="center").place(x=40,y=130)
    label_color5 = Label(lf_vf5,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=160)
    opt_ve5 = ["1Kg - Rs.400","5Kg - Rs.2000"]

    lf_vf6= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_vf6.place(x=120,y=305,width=200,height=280)
    el_6 = Label(lf_vf6,image=spa,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_vf6,text="Green Spanish",font=("arial",9),justify="center").place(x=60,y=130)
    label_color6 = Label(lf_vf6,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=160)
    opt_ve6 = ["1 Piece - Rs.30","5 pieces - Rs.145"]

    lf_vf7= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_vf7.place(x=345,y=305,width=200,height=280)
    el_7 = Label(lf_vf7,image=Oni,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_vf7,text="Chinese Onion",font=("arial",9),justify="center").place(x=60,y=130)
    label_color7 = Label(lf_vf7,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=160)
    opt_ve7 = ["1Kg - Rs.200","2.5Kg - Rs.450"]

    lf_vf8= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_vf8.place(x=570,y=305,width=200,height=280)
    el_8 = Label(lf_vf8,image=car,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_vf8,text="Local Carrot",font=("arial",9),justify="center").place(x=60,y=130)
    label_color8 = Label(lf_vf8,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=160)
    opt_ve8 = ["1Kg - Rs.240","2.5Kg - Rs.480"]

    lf_vf9= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_vf9.place(x=795,y=305,width=200,height=280)
    el_9 = Label(lf_vf9,image=cuc,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_vf9,text="Local Cucumber",font=("arial",9),justify="center").place(x=60,y=130)
    label_color9 = Label(lf_vf9,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=160)
    opt_ve9 = ["1Kg - Rs.150","5Kg - Rs.750"]

    lf_vf10= LabelFrame(frame,border=2,relief="groove",bg="white",fg="black")
    lf_vf10.place(x=1010,y=305,width=200,height=280)
    el_10 = Label(lf_vf10,image=zero,border=2,justify="center").place(x=10,y=0)
    nam = Label(lf_vf10,text="Potato",font=("arial",9),justify="center").place(x=60,y=130)
    label_color10 = Label(lf_vf10,text="Qty:",border=1,font=("arial",9),justify="left").place(x=5,y=160)
    opt_ve10 = ["1Kg - Rs.50","2.5Kg - Rs.250"]

    global clicked_FV1,clicked_FV2,clicked_FV3,clicked_FV4,clicked_FV5,FruV_list
    global clicked_FV6,clicked_FV7,clicked_FV8,clicked_FV9,clicked_FV10

    drop_fe1 = OptionMenu(lf_vf1,clicked_FV1,*opt_ve1).place(x=40,y=160)
    drop_fe2 = OptionMenu(lf_vf2,clicked_FV2,*opt_ve2).place(x=40,y=160)
    drop_fe3 = OptionMenu(lf_vf3,clicked_FV3,*opt_ve3).place(x=40,y=160)
    drop_fe4 = OptionMenu(lf_vf4,clicked_FV4,*opt_ve4).place(x=40,y=160)
    drop_fe5 = OptionMenu(lf_vf5,clicked_FV5,*opt_ve5).place(x=40,y=160)
    drop_fe6 = OptionMenu(lf_vf6,clicked_FV6,*opt_ve6).place(x=40,y=160)
    drop_fe7 = OptionMenu(lf_vf7,clicked_FV7,*opt_ve7).place(x=40,y=160)
    drop_fe8 = OptionMenu(lf_vf8,clicked_FV8,*opt_ve8).place(x=40,y=160)
    drop_fe9 = OptionMenu(lf_vf9,clicked_FV9,*opt_ve9).place(x=40,y=160)
    drop_fe10 = OptionMenu(lf_vf10,clicked_FV10,*opt_ve10).place(x=40,y=160)

# Function of Vegetable and fruits
    def vegfruPrice(s):
        s1 = ""
        for i in range(len(s)-1,0,-1):
            if s[i]!=".":
                s1 = s1+s[i]
            else:
                break
        return int(s1[::-1])

# FUnction of Vegetable and Fruits (Quantity)

    def vegefruQty(s):
        s1 = "" 
        for i in range(len(s)):
            s1 = s1+s[i]
            if s[i]=="g" or s[i]=="L":
                break
        return s1     

# Function to add the items in cart

    def AddV1():
        global FruV_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            FruV_list.append(["Mustang Apple",vegfruPrice(clicked_FV1.get()),vegefruQty(clicked_FV1.get()),Spaces(40-len("Mustang Apple"))])
            messagebox.showinfo("Product Status","Mustang Apple ("+clicked_FV1.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Mustang Apple ("+clicked_FV1.get()+") is not added to the cart.")   

    def AddV2():
        global FruV_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            FruV_list.append(["Indian Banana",vegfruPrice(clicked_FV2.get()),vegefruQty(clicked_FV2.get()),Spaces(40-len("Indian Banana"))])
            messagebox.showinfo("Product Status","Indian Banana ("+clicked_FV2.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Indian Banana ("+clicked_FV2.get()+") is not added to the cart.")   

    def AddV3():
        global FruV_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            FruV_list.append(["Nepali Grapes",vegfruPrice(clicked_FV3.get()),vegefruQty(clicked_FV3.get()),Spaces(40-len("CNepali Grapes"))])
            messagebox.showinfo("Product Status","Nepali Grapes ("+clicked_FV3.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Nepali Grapes("+clicked_FV3.get()+") is not added to the cart.")   

    def AddV4():
        global FruV_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            FruV_list.append(["Gorkha Orange",vegfruPrice(clicked_FV4.get()),vegefruQty(clicked_FV4.get()),Spaces(40-len("Gorkha Orange"))])
            messagebox.showinfo("Product Status","Gorkha Orange ("+clicked_FV4.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Gorkha Orange ("+clicked_FV4.get()+") is not added to the cart.")   

    def AddV5():
        global FruV_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            FruV_list.append(["Chinese Pomegranate",vegfruPrice(clicked_FV5.get()),vegefruQty(clicked_FV5.get()),Spaces(40-len("Chinese Pomegranate"))])
            messagebox.showinfo("Product Status","Chinese Pomegrante ("+clicked_FV5.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Chinese Pomegrante ("+clicked_FV5.get()+") is not added to the cart.")   

    def AddV6():
        global FruV_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            FruV_list.append(["Green Spanish",vegfruPrice(clicked_FV6.get()),vegefruQty(clicked_FV6.get()),Spaces(40-len("Green Spanish"))])
            messagebox.showinfo("Product Status","Green Spanish ("+clicked_FV6.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Green Spanish("+clicked_FV6.get()+") is not added to the cart.")  
    
    def AddV7():
        global FruV_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            FruV_list.append(["Chinese Onion",vegfruPrice(clicked_FV7.get()),vegefruQty(clicked_FV7.get()),Spaces(40-len("Chinese Onion"))])
            messagebox.showinfo("Product Status","Chinese Onion ("+clicked_FV7.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Chinese Onion ("+clicked_FV7.get()+") is not added to the cart.")  

    def AddV8():
        global FruV_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            FruV_list.append(["Local Carrot",vegfruPrice(clicked_FV8.get()),vegefruQty(clicked_FV8.get()),Spaces(40-len("Local Carrot"))])
            messagebox.showinfo("Product Status","Local Carrot ("+clicked_FV8.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Local Carrot ("+clicked_FV8.get()+") is not added to the cart.")  

    def AddV9():
        global FruV_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            FruV_list.append(["Local Cucumber",vegfruPrice(clicked_FV9.get()),vegefruQty(clicked_FV9.get()),Spaces(40-len("Local Cucumber"))])
            messagebox.showinfo("Product Status","Local Cucumber ("+clicked_FV9.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Local Cucumber ("+clicked_FV9.get()+") is not added to the cart.")  

    def AddV10():
        global FruV_list
        op = messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            FruV_list.append(["Potato",vegfruPrice(clicked_FV10.get()),vegefruQty(clicked_FV10.get()),Spaces(40-len("Potato"))])
            messagebox.showinfo("Product Status","Potato ("+clicked_FV10.get()+") is successfully added to the cart.")

        else:
            messagebox.showinfo("Product Status","Potato ("+clicked_FV10.get()+") is not added to the cart.")  

    
# Button to Add the items in cart

    add_vg1 = Button(lf_vf1,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddV1).place(x=60,y=200)
    add_vg2 = Button(lf_vf2,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddV2).place(x=60,y=200)
    add_vg3 = Button(lf_vf3,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddV3).place(x=60,y=200)
    add_vg4 = Button(lf_vf4,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddV4).place(x=60,y=200)
    add_vg5 = Button(lf_vf5,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddV5).place(x=60,y=200)
    add_vg6 = Button(lf_vf6,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddV6).place(x=60,y=200)
    add_vg7 = Button(lf_vf7,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddV7).place(x=60,y=200)
    add_vg8 = Button(lf_vf8,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddV8).place(x=60,y=200)
    add_vg9 = Button(lf_vf9,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddV9).place(x=60,y=200)
    add_vg10 = Button(lf_vf10,text="Add Items",bg="green",fg="white",font=("arial",9,"bold"),command=AddV10).place(x=60,y=200)


# Button of the Fruits and VegeTables in Button Frame

Fruit_btn = Button(Button_frame,bg="light yellow",fg="black",border=2,text="Fruit & Vegetables",font=("times",19,"bold"),activebackground="light blue",command=VegeFruCall)
Fruit_btn.place(x=1220,y=0,width=302)

# Function of Bill 

def bill():
    op = messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or remove during bill generation. Are you sure that you have Finished shopping?")
    if op:
        frame.destroy()
        Button_frame.destroy()
        bill_gen_button.destroy()

        grocery_price = 0
        electronic_price = 0
        SportGym_price = 0
        Furniture_price = 0
        FruitsVegetable_price = 0

        for i in range(len(elec_list)):
            electronic_price+=elec_list[i][1]
        
        for i in range(len(grocery_list)):
            grocery_price+=grocery_list[i][1]

        for i in range(len(sportsgym_list)):
            SportGym_price+=sportsgym_list[i][1]

        for i in range(len(Furni_list)):
            Furniture_price+=Furni_list[i][1]

        for i in range(len(FruV_list)):
            FruitsVegetable_price+=FruV_list[i][1]

        total_price = grocery_price+electronic_price+SportGym_price+Furniture_price+FruitsVegetable_price
        discount = [0,0,0]

        if 0.15*total_price<500:
            discount[0] = 0.15*total_price
        else:
            discount[0] = 500
        
        if 0.1*total_price<570:
            discount[1] = 0.1*total_price
        else:
            discount[1] = 750

        if 0.05*total_price<1000:
            discount[2] = 0.05*total_price
        else:
            discount[2] = 1000

        max_discount = max(discount)

        if max_discount == discount[0]:
            suggest = Label(root,text="Suggested : 15% Off Upto Rs.500",font=("times",12),fg="blue").place(x=545,y=480)
        elif max_discount == discount[1]:
            suggest = Label(root,text="Suggested : 10% Off Upto Rs.750",font=("times",12),fg="blue").place(x=545,y=480)
        else:
            suggest = Label(root,text="Suggested : 5% Off Upto Rs.1000",font=("times",12),fg="blue").place(x=545,y=480)

        def GenBill(d,choice):
            def save_Invoice():
                text = bill_txt_area.get("1.0", "end-1c")
                file_path = filedialog.asksaveasfilename(defaultextension=".txt")
                if file_path:
                    with open(file_path, "w") as f:
                        f.write(text)
            global bill_txt_area
            bill_area = LabelFrame(root)
            bill_area.pack(fill=BOTH,expand=True)            
            bill_title = Label(bill_area,text="INVOICE",font=("arial",15,"bold"),border=4,relief="groove").pack(fill=X)
            scroll_y = Scrollbar(bill_area,orient=VERTICAL)
            scroll_x = Scrollbar(bill_area,orient=VERTICAL)

            bill_txt_area = Text(bill_area,yscrollcommand=scroll_y.set) 
            scroll_y.pack(side=RIGHT,fill=X)
            scroll_y.config(command=bill_txt_area.yview)
            bill_txt_area.pack(fill=BOTH,expand=1)
            bill_txt_area.insert(END,Spaces(40)+"JHI: PASA:\n"+Spaces(90,'*')+"\n") 
            # bill_txt_area.place(relx=500, rely=500, anchor=CENTER)

            if len(grocery_list)>0:
                bill_txt_area.insert(END,"Grocery Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
                for i in grocery_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Grocery Price : Rs."+str(grocery_price)+"\n"+Spaces(90,"*")+"\n")
            
            if len(elec_list)>0:
                bill_txt_area.insert(END,"Electronics Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Colour\n")
                for i in elec_list:
                    bill_txt_area.insert(END,i[0]+i[4]+"Rs."+i[2]+Spaces(27-len(i[2]))+i[3]+"\n")
                bill_txt_area.insert(END,"\nTotal Electronics Price : Rs."+str(electronic_price)+"\n"+Spaces(90,'*')+"\n")

            if len(sportsgym_list)>0:
                bill_txt_area.insert(END,"Sports nd Gym Equipment(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in sportsgym_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Sports nd Gym Equipment Price : Rs."+str(SportGym_price)+"\n"+Spaces(90,'*')+"\n")
            
            if len(Furni_list)>0:
                bill_txt_area.insert(END,"Furniture Product(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in Furni_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Furniture Price : Rs."+str(Furniture_price)+"\n"+Spaces(90,'*')+"\n")
        
            if len(FruV_list)>0:
                bill_txt_area.insert(END,"Fruits nd vegetables Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Quantity\n")
                for i in FruV_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Fruits nd Vegetables Price : Rs."+str(FruitsVegetable_price)+"\n"+Spaces(90,'*')+"\n")

            if choice == 1:
                bill_txt_area.insert(END,"\nCoupon Appiled : 15% Off Upto Rs.500")
            elif choice == 2:
                bill_txt_area.insert(END,"\nCoupon Applied : 10% Off Upto Rs.750")
            else:
                bill_txt_area.insert(END,"\nCoupon Applied : 5% Off Upto Rs.1000")

            bill_txt_area.insert(END,"\nDiscount Offered : Rs."+str(d))
            bill_txt_area.insert(END,"\nTotal Price(after Discount) = Rs."+str(total_price-d))
            bill_area.pack()
# Button to save the INvoice
            save_btn = Button(root,border=6,text="Save Invoice",bg="skyblue",font=("times",20,"bold"),width=10,fg="white",command=save_Invoice)
            save_btn.place(x=1165,y=600)

            def KeepShop():
                root.destroy()
                import subprocess
                cmd='python main.py'
                pc=subprocess.Popen(cmd,shell=True)
            KeepShoping_button = Button(root, border=6, text=" Keep Shopping", font=("times", 20, "bold"), bg="skyblue",fg="white", activebackground="purple",width=12,command=KeepShop)
            KeepShoping_button.place(x=1165, y=665)
                
# Frame and the Button of Coupons
        Cou_frame = LabelFrame(root,border=2,relief="groove",text="Apply For Coupon",fg="green",font=("arial",16,"bold")).place(x=500,y=150,width=380,height=300)

        cou1 = Button(Cou_frame,text="15% Off Upto Rs.500",font=("times",20,"bold"),bg="cadetblue",fg="white",activebackground="light blue",width=17,border=6,command=lambda:GenBill(discount[0],1))
        cou1.place(x=540,y=190)

        cou2 = Button(Cou_frame,text="10% Off Upto Rs.750",font=("times",20,"bold"),bg="cadetblue",fg="white",activebackground="light blue",width=17,border=6,command=lambda:GenBill(discount[1],2))
        cou2.place(x=540,y=280)

        cou3 = Button(Cou_frame,text="5% Off Upto Rs.1000",font=("times",20,"bold"),bg="cadetblue",fg="white",activebackground="light blue",width=17,border=6,command=lambda:GenBill(discount[2],3))
        cou3.place(x=540,y=370)
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can Continue Shopping Now.")

# Button to Generate the Bill

bill_gen_button = Button(Heading,border=4,text="Processed to CheckOut",font=("times",18,"bold"),bg="skyblue",fg="white",activebackground="purple",command=bill)
bill_gen_button.place(x=1263,y=0)


root.mainloop()