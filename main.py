import time
import math
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as Mb

# global var

opsi = 1
opsi2 = 1
inputs = 0

# configure

root = tk.Tk()
p1 = tk.PhotoImage(file='David design.png')
root.iconphoto(False, p1)
root.title('Konversi temperatur')
root.resizable(False, False)
canvas1 = tk.Canvas(root, width=300, height=300, bg='gray90',
                    relief='raised')
canvas1.pack()


# Cek apakah input adalah float

def isFloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def myCmd():
    global inputs
    if isFloat(variabel_teks.get()):
        inputs = float(variabel_teks.get())
        process()
    elif isFloat(variabel_teks.get()) is not True \
        and variabel_teks.get() != '':

        error = tk.StringVar()
        error.set('MASUKAN NOMOR')
        print ('[', time.strftime('%H:%M:%S', time.localtime()), ']',
               'NOT VALID FLOAT')
        variabel_teks.set('')
        label_hasil.config(textvariable=error)


def process():
    global inputs
    hasil = tk.IntVar()
    #optimisasi if else dengan metode branchless programming
    hasil.set(round((inputs)*(int(not(1/opsi - math.floor(opsi/1))))
                    + ((273.15) * (int(not(3/opsi2 - math.floor(opsi2/3))))) *(int(not(1/opsi - math.floor(opsi/1))))
                    + ((inputs * 9/5 + 32 ) * (int(not (2 / opsi2 - math.floor(opsi2 / 2))))) *(int(not(1/opsi - math.floor(opsi/1))))
                    - (inputs)*(int(not(2/opsi2 - math.floor(opsi2/2)))) *(int(not(1/opsi - math.floor(opsi/1))))
                    +(((inputs)*(int(not(2/opsi - math.floor(opsi/2))))
                       + ( inputs - 32 ) * (5/9)*(int(not(1/opsi2 - math.floor(opsi2/1))))) * (int(not(2/opsi - math.floor(opsi/2)))))
                    - (inputs)*(int(not(1/opsi2 - math.floor(opsi2/1)))) * (int(not(2/opsi - math.floor(opsi/2))))
                    + ((273.15)*(int(not(3/opsi2 - math.floor(opsi2/3))))) * (int(not(2/opsi - math.floor(opsi/2))))
                    + ((inputs - 32) * (5/9)*(int(not(3/opsi2 - math.floor(opsi2/3))))) * (int(not(2/opsi - math.floor(opsi/2))))
                    - (inputs)*(int(not(3/opsi2 - math.floor(opsi2/3)))) * (int(not(2/opsi - math.floor(opsi/2))))
                    + (inputs)*(int(not(3/opsi - math.floor(opsi/3))))
                    - ((273.15)*(int(not(1/opsi2 - math.floor(opsi2/1))))) *(int(not(3/opsi - math.floor(opsi/3))))
                    + ((((inputs - 273.15)*9/5 +32)) * (int(not(2/opsi2 - math.floor(opsi2/2)))) *(int(not(3/opsi - math.floor(opsi/3))))
                       - (inputs)* (int(not(2/opsi2 - math.floor(opsi2/2)))))*(int(not(3/opsi - math.floor(opsi/3)))),2))
    print ('[', time.strftime('%H:%M:%S', time.localtime()), ']',
           'Hasil konversi: ' + str(hasil.get()))
    label_hasil.config(textvariable=hasil)

def choices(event):

    # print(choice_var.get())
    # os.system("cls")

    global opsi
    global opsi2

    # Pengerjaan ulang untuk pengecekan kondisi opsi

    for i in range(len(worklist)):
        if choice_var.get() == worklist[i]:
            opsi = i+1

    for i in range(len(worklist)):
        if choice_var2.get() == worklist[i]:
            opsi2 = i+1

    print ('[', time.strftime('%H:%M:%S', time.localtime()), ']',
           'Indeks opsi pertama yang terpilih: ' + str(opsi))
    print ('[', time.strftime('%H:%M:%S', time.localtime()), ']',
           'Indeks opsi kedua yang terpilih: ' + str(opsi2))


def about():
    print ('[', time.strftime('%H:%M:%S', time.localtime()), ']',
           'Message box popped')
    Mb.showinfo('About',
                'Temperature converter \n Copyright David Yusuf 2021')


worklist = ['Celcius', 'Fahrenheit', 'Kelvin']
choice_var = tk.StringVar()

choice_var2 = tk.StringVar()

# menu opsi

optionmen = ttk.OptionMenu(root, choice_var, worklist[0],
                           command=choices, *worklist)
optionmen2 = ttk.OptionMenu(root, choice_var2, worklist[0],
                            command=choices, *worklist)

canvas1.create_window(100, 50, window=optionmen)
canvas1.create_window(200, 50, window=optionmen2)

# label

label_hasil = tk.Label(root, font=('bold', 11), anchor='c')
label_hasil.config(width=14, bg='black', fg='white')
canvas1.create_window(150, 80, window=label_hasil)

# entry

variabel_teks = tk.StringVar()
input_entry = tk.Entry(root, textvariable=variabel_teks)
canvas1.create_window(150, 120, window=input_entry)

# button

About_button = ttk.Button(text='About', command=about)
button1 = ttk.Button(text='      konversi      ', command=myCmd)
canvas1.create_window(150, 150, window=button1)
canvas1.create_window(50, 280, window=About_button)

root.mainloop()