import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as Mb

#global var
opsi = 0
opsi2 = 0
inputs = 0
#configure
root= tk.Tk()
p1 = tk.PhotoImage(file= "David design.png")
root.iconphoto(False,p1)
root.title("Konversi temperatur")
root.resizable(False,False)
canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'gray90', relief = 'raised')
canvas1.pack()
#Cek apakah input adalah float
def isFloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
def myCmd ():
    global inputs
    if isFloat(variabel_teks.get()):
        inputs = float(variabel_teks.get())
        process()

    elif isFloat(variabel_teks.get()) != True and variabel_teks.get() != "":
        error = tk.StringVar()
        error.set("MASUKAN NOMOR")
        print("[",time.strftime("%H:%M:%S", time.localtime()),"]","NOT VALID FLOAT")
        variabel_teks.set("")
        label_hasil.config(textvariable=error)
def process():
    global inputs
    hasil = tk.IntVar()
    #celcius
    if opsi == opsi2:
        hasil.set(inputs)
    elif opsi == 0 and opsi2 == 1:
        hasil.set((inputs * 9/5 )+32)
        #hasie = (inputs * 9/5 )+32
        #print(hasie)
    elif opsi == 0 and opsi2 == 2:
        hasil.set(inputs + 273.15)
    #fahrenheit
    elif opsi == 1 and opsi2 == 0:
        hasil.set(round((inputs - 32)*5/9,2))
    elif opsi == 1 and opsi2 == 2:
        hasil.set(round(273.15 + (inputs - 32) * 5/9,2) )
    #kelvin
    elif opsi == 2 and opsi2 == 0:
        hasil.set(round(inputs-273.15,2))
    elif opsi == 2 and opsi2 == 1:
        hasil.set(round((inputs -273.15)*9/5 +32,2))
    print("[",time.strftime("%H:%M:%S",time.localtime()),"]","Hasil konversi: "  + str(hasil.get()))
    label_hasil.config(textvariable=hasil)
def choices(event):
    #print(choice_var.get())
    #os.system("cls")
    global opsi
    global opsi2
    if choice_var.get() == "Celcius":
        opsi = 0
    elif choice_var.get() == "Fahrenheit":
        opsi = 1
    elif choice_var.get() == "Kelvin":
        opsi = 2

    if choice_var2.get() == "Celcius":
        opsi2 = 0
    elif choice_var2.get() == "Fahrenheit":
        opsi2 = 1
    elif choice_var2.get() == "Kelvin":
        opsi2 = 2
    print("[",time.strftime("%H:%M:%S",time.localtime()),"]","Indeks opsi pertama yang terpilih: " + str(opsi))
    print("[",time.strftime("%H:%M:%S",time.localtime()),"]","Indeks opsi kedua yang terpilih: " + str(opsi2))
def about():
    {
        Mb.showinfo("about", "Temperature converter \n Copyright David Yusuf 2021")
    }

worklist = ["Celcius","Fahrenheit","Kelvin"]
choice_var = tk.StringVar()
#choice_var.set(worklist[0])
choice_var2 = tk.StringVar()
#choice_var2.set(worklist[0])
#menu opsi
optionmen = ttk.OptionMenu(root,choice_var,worklist[0],*worklist,command=choices)
optionmen2 = ttk.OptionMenu(root,choice_var2,worklist[0],*worklist,command=choices)
#optionmen.config(width=30)
canvas1.create_window(100,50,window=optionmen)
canvas1.create_window(200,50,window=optionmen2)
#label
label_hasil = tk.Label(root,font=('bold',11),anchor='c')
label_hasil.config(width=14,bg='black',fg='white')
canvas1.create_window(150,80,window=label_hasil)

#entry
variabel_teks = tk.StringVar()
input_entry = tk.Entry(root, textvariable=variabel_teks)
canvas1.create_window(150,120,window=input_entry)
#button
#button1 = tk.Button(text='      konversi      ', command=myCmd, bg='green', fg='white', font=('helvetica', 12, 'bold'))
About_button = ttk.Button(text="About",command=about)
button1 = ttk.Button(text='      konversi      ', command=myCmd)
canvas1.create_window(150, 150, window=button1)
canvas1.create_window(50,280,window=About_button)

root.mainloop()