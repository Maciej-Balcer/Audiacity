from scipy.io import wavfile
import numpy as np
from numpy import int16, array
import os, time
import simpleaudio as sa


#Wczytywanie pliku
def load_file(file_name):
    samplerate, data = wavfile.read(str(file_name))
    return samplerate, data

#Zapisywanie pliku
def save_file(file_name,samplerate,data):
    wavfile.write(str(file_name),samplerate,data)

#Odtwarzanie utworu
def play(samplerate,data):
    wavfile.write("tmp_data.wav",samplerate,data)
    wave_obj = sa.WaveObject.from_wave_file("tmp_data.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing
    if os.path.isfile("tmp_data.wav"):
        os.remove("tmp_data.wav")

#Kontrola głośności - wymaga rzutowania
def volume_controll(data,gain):
    volume_data = np.zeros(shape=(len(data),2))
    pom = 0

    ######################
    for i in data:
        volume_data[pom,0] = gain*data[pom,0]
        volume_data[pom,1] = gain*data[pom,1]
        pom+=1
    ########################

    volume_data = scalling(volume_data)
    return volume_data

#Rzutowanie na int16
def scalling(data):
    scaled = int16(data)

    return scaled

#Prędkość odtwarzania
def speed_controll(data,speed):
    speed_data = data
    #######################
    pom1 = np.arange(0,len(speed_data),speed)
    pom1=pom1[pom1<len(speed_data)]
    speed_data = speed_data[pom1.astype(int)]
    #######################
    return speed_data

#Odwracanie danych - wymaga rzutowania
def Inverse(data):
    inverse_data = np.zeros(shape=(len(data),2))
    begin = 0
    end = len(data) - 1
    ######################
    for i in data:
        inverse_data[begin,0] = data[end,0]
        inverse_data[begin,1] = data[end,1]
        begin+=1
        end-=1
    ######################
    inverse_data = scalling(inverse_data)
    return inverse_data

def Fadein(data, samplerate, time):
    Fadedata = np.zeros(shape=(len(data),2))
    x = int(time * samplerate)

    k = 1 / x
    pom = 0
    j=0

    for i in range(len(data)):
        Fadedata[i] = data[i]

    for i in range(len(data)):
        if i<x:
            Fadedata[pom,0] = data[pom,0] * k * j
            Fadedata[pom,1] = data[pom,0] * k * j
            j+=1
        pom+=1

    Fadedata = scalling(Fadedata)

    return Fadedata

def Fadeout(data, samplerate, time):
    Fadedata = np.zeros(shape=(len(data),2))
    x = int(time * samplerate)

    lastindx = len(data) - x

    k = 1 / x
    j = x - 1

    for i in range(len(data)):
        Fadedata[i] = data[i]

    for i in range(lastindx,len(data)):
        Fadedata[i,0] = data[i,0] * k * j
        Fadedata[i,1] = data[i,1] * k * j
        j-=1

    Fadedata = scalling(Fadedata)
    return Fadedata

def Echo(data,samplerate,time):
    x = time * samplerate
    Echodata = np.zeros(shape=(len(data),2))
    gain = 0.4

    j = 0
    pom = 0

    for i in range(len(data)):
        if i>x:
            Echodata[pom,0] = data[pom,0] + gain*data[j,0]
            Echodata[pom,1] = data[pom,1] + gain*data[j,1]
            j+=1
        else:
            Echodata[pom,0] = data[i,0]
            Echodata[pom,1] = data[i,1]
        pom+=1

        Echodata = scalling(Echodata)
    return Echodata
