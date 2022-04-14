import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename
import os
import math

#create main window
def create_main_window():
        global top
        global root
        img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AYht+mFUVaBO0g4hCwOlkQFXGUKhbBQmkrtOpgcukfNGlIUlwcBdeCgz+LVQcXZ10dXAVB8AfE0clJ0UVK/C4ptIjx4O4e3vvel7vvAKFRYaoZmABUzTJS8ZiYza2K3a8IIIR+WkckZuqJ9GIGnuPrHj6+30V5lnfdnyOk5E0G+ETiOaYbFvEG8cympXPeJw6zkqQQnxOPG3RB4keuyy6/cS46LPDMsJFJzROHicViB8sdzEqGSjxNHFFUjfKFrMsK5y3OaqXGWvfkLwzmtZU012kOI44lJJCECBk1lFGBhSjtGikmUnQe8/APOf4kuWRylcHIsYAqVEiOH/wPfvfWLExNuknBGND1Ytsfo0D3LtCs2/b3sW03TwD/M3Cltf3VBjD7SXq9rUWOgL5t4OK6rcl7wOUOMPikS4bkSH6aQqEAvJ/RN+WAgVugd83tW+scpw9Ahnq1fAMcHAJjRcpe93h3T2ff/q1p9e8HSB5ylkmT+ZUAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfmBA0SCQ4i+81yAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAsxJREFUSMe1Vr1KM1EQPbkKESR3I1hJRESI2uYBJKSysrCwzgPYbRdYdfNjKaRMowa0sElgn8AXMJhC0CJKMEQE0biYhEB2YjFyvzXqavzWU83Ozp0zO7MzdwJEhL/EOIB0Or23t+e7a13XDcMIEFE4HLZtW0rpo3d22Gq1xvlZSvn09BQIBHzxPhgMpqamWBZK65f3IVdipJOZTCabzY5GxjUA0Gq1vE2bzWYkEhFCtNvtYDDobax8jvAFlUoFABG9vLz8/NQIBKVSiYVOp+M/QbPZPDw8ZPnbZP6G4OzsDEAkEgHw/Pz8vwT9fn9nZyeTyShNuVwGYBjGqAQgIimllJJcOD4+5rePj49E1Gg0ACSTyfPzcwAHBwduY8dxTNM0TdOtVD4/IahUKqpTqtUqEVmWBcCyrHq9DiCXy7l9XVxcsPHDw8NHAuHubzba3NwEsLW1BaBWq6n/JxaLTU5OAri7u3Pn4OTkhIXr6+svU8TjSEo5MTEB4OjoiINNpVIqP0TU7XaFEPF4XEV6c3OjZsP+/r5KmqZp71IEgFVSSsMwer1er9eLRqPRaJQDtCyLD8fjcSFEt9vlx3w+D6BYLAIYGxtjD5qmccT/CDRNcxyH3iOVSgGYn58H0Gg0WMkJ5HTf399LKVdWVjqdjmma0oVhgqG/iKFal/PDyOVyAOr1OhFx4OVyeeig4zifFPkjFhYWWFhfX1fKmZkZbmbbtnd3dxcXFxOJhMe4HvcgmJ2dZSEWiynl9PQ099rp6enV1VWxWAyFQt/cyR4j1zRNFTWDC3h7e1soFEKh0Orq6m862QPVahXA0tISgHw+/5XZj2rgcZNcXl4CWFtb8/M+YHAzc6vPzc39CYEQAsDGxsZPF6+REAwGt7e3B4PB8vKyz5f+L0r17tLnaerX4jWcItu21S7m4+r4VmRd1/1dTHnS6br+VoM/Xd9fAVRROIG1BVk9AAAAAElFTkSuQmCC'
        root= tk.Tk()
        top= root
        top.geometry("600x450+468+138")
        top.title("Text to Waveform")
        favicon=tk.PhotoImage(data=img) 
        root.wm_iconphoto(True, favicon)

#Textbox
def create_textbox():
        global textbox
        textbox = Text(top)
        textbox.place(relx=0.033, rely=0.022, relheight=0.878, relwidth=0.933)
        scroll_1=Scrollbar (top)
        scroll_1.pack(side=RIGHT, fill=Y)
        textbox.configure(yscrollcommand=scroll_1.set)
        scroll_1.configure(command=textbox.yview)
        textbox.focus_set()

#menu
def create_menu():
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="File")
    sub_menu.add_command(compound="left",label="Paste", command=paste_text)
    sub_menu.add_command(compound="left",label="Clear", command=ClearTextBox)
    sub_menu.add_command(compound="left",label="Convert", command=convert)
    sub_menu.add_command(compound="left",label="Quit", command=QuitApp)

#Quit
def QuitApp():
    top.destroy()

#Paste
def paste_code():
    #textbox.tag_add(SEL, "1.0", END)
    textbox.event_generate(("<<Paste>"))

#PasteContextMenu
def create_context_menu():
        global menu
        menu = Menu(root, tearoff = 0)
        menu.add_command(label="Paste", command=paste_text)
        root.bind("<Button-3>", context_menu)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()
        
def paste_text():
        textbox.event_generate(("<<Paste>>"))

#Clear
def ClearTextBox():
    textbox.delete(1.0,END)

#Save to file
def Save_to_file():
        data=[('Sound File','*.wav')]
        wavefilename=asksaveasfilename(filetypes=data, defaultextension=data)
        if str(wavefilename)!='':
              wavefile=open(wavefilename,'wb')
              headerbytes=b'RIFF\xce\x07\xf1\x0bWAVEfmt \x10\x00\x00\x00\x01\x00\x02\x00\x11+\x00\x00"V\x00\x00\x02\x00\x08\x00data&\x06\xf1\x0b'
              wavefile.write(headerbytes)
              tempfile=open("tempfile.wav",'rb')
              wavebytes=tempfile.read()
              wavefile.write(wavebytes)
              wavefile.close()
              tempfile.close()
              os.remove("tempfile.wav")

#Create waveform functions
def sine(amp, samples):
    amp=int(amp)
    samples=int(samples)
    posamp=128+amp
    negamp=128-amp
    freq=int(360/samples)
    for angle in range(0,360, freq):
        y = math.sin(math.radians(angle))
        value=int(y*amp)+128
        bytewrite=value.to_bytes(1,'big')
        tempfile.write(bytewrite)

        
def triangle (amp, samples):
    amp=int(amp)
    samples=int(samples)
    posamp=128+amp
    negamp= 128-amp
    freq= int(256/samples)
    negfreq=freq-freq*2
    for i in range (128,posamp,freq):
        bytewrite=i.to_bytes(1,'big')
        tempfile.write(bytewrite)
    for n in range (posamp,negamp,negfreq):
        bytewrite=n.to_bytes(1,'big')
        tempfile.write(bytewrite)
    for m in range (negamp,128,freq):
        bytewrite=m.to_bytes(1,'big')
        tempfile.write(bytewrite)

def square (amp, samples):
    amp=int(amp)
    samples=int(samples)
    global wavebyteslocal
    wavebyteslocal=""
    posamp=128+amp
    negamp=128-amp
    freq=int(samples/2)
    for i in range (0,freq,1):
        bytewrite=negamp.to_bytes(1,'big')
        tempfile.write(bytewrite)
    for n in range (0,freq,1):
        bytewrite=posamp.to_bytes(1,'big')
        tempfile.write(bytewrite)
        
#Convert letters
def convert():
    trc=14.11
    trcm=14.11
    sqc=21.16
    sqcm=21.16
    snc=11.54
    sncm=11.54
    global tempfile
    tempfile=open("tempfile.wav",'wb')
    text=textbox.get(1.0,END)
    length=len(text)
    for letters in range (0,length):
        char=text[letters]
        if char=='':
            end
        else:
            asciicode=ord(char)
            if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
                if char=="A" or char=="a":
                    triangle(trc,trcm)
                if char=="B" or char=="b":
                    sine (snc,sncm)
                if char=="C" or char=="c":
                    sine(snc*2,sncm*2)
                if char=="D" or char=="d":
                    sine(snc*3,sncm*3)
                if char=="E" or char=="e":
                    square(sqc,sqcm)
                if char=="F" or char=="f":
                    square(sqc*2,sqcm*2)
                if char=="G" or char=="g":
                    sine(snc*4,sncm*4)
                if char=="H" or char=="h":
                    square(sqc*3,sqcm*3)
                if char=="i" or char=="I":
                    square(sqc*4,sqcm*4)
                if char=="J" or char=="j":
                    sine(snc*5,sncm*5)
                if char=="K" or char=="k":
                    triangle(trc*2,trcm*2)
                if char=="L" or char=="l":
                    square(sqc*5,sqcm*5)
                if char=="M" or char=="m":
                    triangle(trc*3,trcm*3)
                if char=="N" or char=="n":
                    triangle(trc*4,trcm*4)
                if char=="O" or char=="o":
                    sine(snc*6,sncm*6)
                if char=="P" or char=="p":
                    sine(snc*7,sncm*7)
                if char=="Q" or char=="q":
                    sine(snc*8,sncm*8)
                if char=="R" or char=="r":
                    sine(snc*9,sncm*9)
                if char=="S" or char=="s":
                    sine(snc*10,sncm*10)
                if char=="T" or char=="t":
                    square(sqc*6,sqcm*6)
                if char=="U" or char=="u":
                    sine(snc*11,sncm*11)
                if char=="V" or char=="v":
                    triangle(trc*5,trcm*5)
                if char=="W" or char=="w":
                    triangle(trc*6,trcm*6)
                if char=="X" or char=="x":
                    triangle(trc*7,trcm*7)
                if char=="Y" or char=="y":
                    triangle(trc*8,trcm*8)
                if char=="Z" or char=="z":
                    triangle(trc*9,trcm*9)
    tempfile.close()
    Save_to_file()
    
#main             
def main():
        create_main_window()
        create_textbox()
        create_menu()
        create_context_menu()

main()
root.mainloop()
