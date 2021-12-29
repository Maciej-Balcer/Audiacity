from tkinter import *

import Prog as P
import os

global sample
global data

#Key function
def load_on_click():
    global data
    global sample
    entered_text=nazwa_pliku.get()
    if os.path.isfile(str(entered_text)):
        sample, data = P.load_file(entered_text)
        output.delete(0.0,END)
        output.insert(END,"Wczytano plik")
    else:
        output.delete(0.0,END)
        output.insert(END,"Nie ma pliku o podanej nazwie")
    #print (sample)
    #print(data)

def save_on_click():
    entered_text = save_box.get()
    P.save_file(entered_text,sample,data)
    output.delete(0.0,END)
    output.insert(END,"Zapisano plik")

def play_on_click():
    if os.path.isfile(str(nazwa_pliku.get())):
        P.play(sample,data)

def click_exit():
    window.destroy()
    exit()

def Fade_in():
    if int(Time_box1.get())<0:
        output.delete(0.0,END)
        output.insert(END,"Wpisz poprawną wartość")
    else:
        global data, sample
        time = int(Time_box1.get())
        new_data = P.Fadein(data,sample,time)
        data = new_data
        output.delete(0.0,END)
        output.insert(END,"Wykonano operację")


def Fade_out():
    if int(Time_box2.get())<0:
        output.delete(0.0,END)
        output.insert(END,"Wpisz poprawną wartość")
    else:
        global data, sample
        time = int(Time_box2.get())
        new_data = P.Fadeout(data,sample,time)
        data = new_data
        output.delete(0.0,END)
        output.insert(END,"Wykonano operację")

def Zmiana_predkosci():
    if float(Speed_box.get())<0:
        output.delete(0.0,END)
        output.insert(END,"Wpisz poprawną wartość")
    else:
        global data
        gain = float(Speed_box.get())
        new_data = P.speed_controll(data,gain)
        data = new_data
        output.delete(0.0,END)
        output.insert(END,"Wykonano operację")

def Zglasnianie():
    if float(Pitch_box.get())<0:
        output.delete(0.0,END)
        output.insert(END,"Wpisz poprawną wartość")
    else:
        global data
        gain = float(Pitch_box.get())
        new_data = P.volume_controll(data,gain)
        data = new_data
        output.delete(0.0,END)
        output.insert(END,"Wykonano operację")

def Echo():
    if int(Echo_box.get())<0:
        output.delete(0.0,END)
        output.insert(END,"Wpisz poprawną wartość")
    else:
        global data, sample
        time = int(Echo_box.get())
        new_data = P.Echo(data,sample,time)
        data = new_data
        output.delete(0.0,END)
        output.insert(END,"Wykonano operację")

def Inverse():
    global data
    new_data = P.Inverse(data)
    data = new_data
    output.delete(0.0,END)
    output.insert(END,"Wykonano operację")




#Main
window = Tk()
window.title("Procesory Sygnałowe")
window.configure(background="whitesmoke")


Frame1 = LabelFrame(window, text=" 1. Odczyt/zapis pliku: ")
Frame1.grid(row=0, columnspan=7, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

help = LabelFrame(window, text="Powiadomienia")
help.grid(row=0, column=9, columnspan=2, rowspan=8, sticky='NS', padx=5, pady=5)

effects = LabelFrame(window, text="2. Lista dostępnych efektów")
effects.grid(row=2, columnspan=7, sticky='W', padx=5, pady=5, ipadx=50)

instrukcja = LabelFrame(window, text="3. Instrukcja obługi")
instrukcja.grid(row=3, columnspan=7, sticky='W', padx=5, pady=5, ipadx=50)

LoadLabel = Label(Frame1, text="Wprowadź nazwę pliku z rozszerzeniem .wav :")
LoadLabel.grid(row=1, column=0, sticky='E', padx=20, pady=2)

SaveLabel = Label(Frame1, text="Zapisz plik z rozszerzeniem .wav :")
SaveLabel.grid(row=2, column=0, sticky='E', padx=20, pady=2)

Label (effects, text="Fade in").grid(row=0,column=0,sticky='W')
Label (effects, text="Fade out").grid(row=1,column=0,sticky='W')
Label (effects, text="Zmiana prędkości").grid(row=2,column=0,sticky='W')
Label (effects, text="Zmiana głośności").grid(row=3,column=0,sticky='W')
Label (effects, text="Utwór od tyłu").grid(row=5,column=0,sticky='W',pady=10, padx = 5)
Label (effects, text="Echo").grid(row=4,column=0,sticky='W')

Label (instrukcja, text="Aby efekty takie jak filtry, zmiana prędkości oraz zmiana głośności zadziałały,").grid(row=0,column=0,sticky='W', padx = 5)
Label (instrukcja, text="należy wprowadzić odpowiednie dane w okienka obok danego efektu:").grid(row=1,column=0,sticky='W', padx = 5)
Label (instrukcja, text="Fade in/ Fade out: czas w [s] na wejście/wyjście utworu").grid(row=2,column=0,sticky='W', padx = 5)
Label (instrukcja, text="Zmiana prędkośći: mnożnik ile razy utwór ma być szybszy/wolniejszy").grid(row=3,column=0,sticky='W',padx = 5)
Label (instrukcja, text="Zmiana głośności: mnożnik ile razy utwór ma być głośniejszy/cichszy").grid(row=4,column=0,sticky='W',padx = 5)
Label (instrukcja, text="Echo: czas w [s] o ile przesunięte będzie echo względem oryginalnego utworu").grid(row=5,column=0,sticky='W',padx = 5)

#Text box
nazwa_pliku = Entry(Frame1)
nazwa_pliku.grid(row=1, column=1, columnspan=7, sticky="WE", pady=10, padx = 5)

save_box = Entry(Frame1)
save_box.grid(row=2,column=1,columnspan=7, sticky="WE", pady=10, padx = 5)

output = Text(help,width = 20, height = 15,wrap = WORD)
output.grid(row = 1, column = 9, columnspan = 2)

Time_box1 = Entry(effects)
Time_box1.grid(row=0, column=1, columnspan=2, sticky="WE", pady=10, padx = 5)

Time_box2 = Entry(effects)
Time_box2.grid(row=1, column=1, columnspan=2, sticky="WE", pady=10, padx = 5)

Speed_box = Entry(effects)
Speed_box.grid(row=2, column=1, columnspan=2, sticky="WE", pady=10, padx = 5)

Pitch_box = Entry(effects)
Pitch_box.grid(row=3, column=1, columnspan=2, sticky="WE", pady=10, padx = 5)

Echo_box = Entry(effects)
Echo_box.grid(row=4,column=1,columnspan=2,sticky="WE",pady=10,padx=5)

#Button
Button(Frame1, text="Załaduj", command=load_on_click).grid(row=1,column=8,sticky='W',padx=5,pady=2)
Button(Frame1, text="Zapisz", command=save_on_click).grid(row=2,column=8,sticky='W',padx=5,pady=2)
Button(window,text="Exit", width = 14, command=click_exit).grid(row=100,column=10,sticky='E',pady=5, padx = 5)
Button(window,text="Play", width = 14, command=play_on_click).grid(row=100,column=9,sticky='E',pady=5, padx = 5)
Button(effects,text="Wybierz", command=Fade_in).grid(row=0,column=3,sticky='W',padx=5,pady=2)
Button(effects,text="Wybierz", command=Fade_out).grid(row=1,column=3,sticky='W',padx=5,pady=2)
Button(effects,text="Wybierz", command=Zmiana_predkosci).grid(row=2,column=3,sticky='W',padx=5,pady=2)
Button(effects,text="Wybierz", command=Zglasnianie).grid(row=3,column=3,sticky='W',padx=5,pady=2)
Button(effects,text="Wybierz", command=Inverse).grid(row=5,column=3,sticky='W',padx=5,pady=2)
Button(effects,text="Wybierz", command=Echo).grid(row=4,column=3,sticky='W',padx=5,pady=2)


window.mainloop()
