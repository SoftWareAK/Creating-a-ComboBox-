import tkinter as tk
from tkinter.ttk import *

def secimAl():
    print(combo.get())
def secimAl2():
    print(combo2.get())




#pencere
pencere=tk.Tk()
pencere.geometry("300x150")
pencere.configure(bg="gray")
pencere.title("Ahmet's calculator")

sayi1=tk.Entry(width=10)
sayi1.place(x=20,y=20)

sayi2=tk.Entry(width=10)
sayi2.place(x=100,y=20)

sonuc=tk.Label(text=":)",bg="blue")
sonuc['font'] = "Verdana 12 bold"
sonuc['fg'] = '#000000'   #hex code renk tanımlamasını kabul eder
sonuc.place(x=180,y=20)



etiket=tk.Label(text="Combo-----Box").pack()



combo=Combobox()
combo['values']=("İstanbul","Antalya","Alanya","Manavgat","Güzelbağ")
combo.current(2) #,değerlerden 2 numarada olanı seçer
combo.place(x=20,y=20)

combo2=Combobox()
combo2['values']=("'da Otelde","da Evde","da Yaylada")
combo2.current(2) #,değerlerden 2 numarada olanı seçer
combo2.place(x=20,y=40)

button=tk.Button(text="işlem",command=secimAl)
button.place(x=20,y=60)

button=tk.Button(text="işlem",command=secimAl2)
button.place(x=60,y=60)

pencere.mainloop()