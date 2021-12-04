import os
import math
from pydub import AudioSegment

textfile= open("text.txt")
text=textfile.read()
length=len(text)
trianglecheck=0
squarecheck=0
sinecheck=0

if os.path.isfile("triangle.wav")==True:
    os.remove("triangle.wav")
trianglewave= open ("triangle.wav",'ab')

if os.path.isfile("square.wav")==True:
    os.remove("square.wav")
squarewave= open ("square.wav",'ab')

if os.path.isfile("sine.wav")==True:
    os.remove("sine.wav")
sinewave= open ("sine.wav",'ab')
    
headerbytes=b'RIFF\xce\x07\xf1\x0bWAVEfmt \x10\x00\x00\x00\x01\x00\x02\x00\x11+\x00\x00"V\x00\x00\x02\x00\x08\x00data&\x06\xf1\x0b'
trianglewave.write(headerbytes)
squarewave.write(headerbytes)
sinewave.write(headerbytes)

def triangle (amp, samples):
    global trianglecheck
    posamp=128+amp
    negamp= 128-amp
    freq= int(256/samples)
    negfreq=freq-freq*2
    for i in range (128,posamp,freq):
        bytewrite=i.to_bytes(1,'big')
        trianglewave.write(bytewrite)
    for n in range (posamp,negamp,negfreq):
        bytewrite=n.to_bytes(1,'big')
        trianglewave.write(bytewrite)
    for m in range (negamp,128,freq):
        bytewrite=m.to_bytes(1,'big')
        trianglewave.write(bytewrite)
    trianglecheck=1

def square (amp, samples):
    global squarecheck
    posamp=128+amp
    negamp=128-amp
    freq=int(samples/2)
    for i in range (0,freq,1):
        bytewrite=negamp.to_bytes(1,'big')
        squarewave.write(bytewrite)
    for n in range (0,freq,1):
        bytewrite=posamp.to_bytes(1,'big')
        squarewave.write(bytewrite)
    squarecheck=1

def sine(amp, samples):
    global sinecheck
    posamp=128+amp
    negamp=128-amp
    freq=int(360/samples)
    for angle in range(0,360, freq):
        y = math.sin(math.radians(angle))
        value=int(y*amp)+128
        bytewrite=value.to_bytes(1,'big')
        sinewave.write(bytewrite)
    sinecheck=1

def closefiles():
    trianglewave.close()
    squarewave.close()
    sinewave.close()
    textfile.close()

for letters in range (0,length):
    char=text[letters]
    if char=='':
        end
    else:
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            if char=="A":
                triangle(5,5)
            if char=="a":
                sine(5,5)
            if char=="B" or char=="b":
                sine (10,10)
            if char=="C" or char=="c":
                sine(15,15)
            if char=="D":
                sine(20,20)
            if char=="d":
                sine(20,20)
            if char=="E":
                square(25,25)
            if char=="e":
                sine(25,25)
            if char=="F" or char=="f":
                square(30,30)
            if char=="G" or char=="g":
                sine(35,35)
            if char=="H":
                square(40,40)
            if char=="h":
                square(40,40)
            if char=="i" or char=="I":
                square(45,45)
            if char=="J" or char=="j":
                sine(50,50)
            if char=="K":
                triangle(55,55)
            if char=="k":
                triangle(55,55)
            if char=="L" or char=="l":
                square(60,60)
            if char=="M":
                triangle(65,65)
            if char=="m":
                square(65,65)
            if char=="N":
                triangle(70,70)
            if char=="n":
                square(70,70)
            if char=="O" or char=="o":
                sine(75,75)
            if char=="P" or char=="p":
                sine(80,80)
            if char=="Q":
                sine(85,85)
            if char=="q":
                sine(85,85)
            if char=="R":
                sine(90,90)
            if char=="r":
                square(90,90)
            if char=="S" or char=="s":
                sine(95,95)
            if char=="T":
                square(100,100)
            if char=="t":
                square(100,100)
            if char=="U" or char=="u":
                sine(105,105)
            if char=="V" or char=="v":
                triangle(110,110)
            if char=="W" or char=="w":
                triangle(115,115)
            if char=="X" or char=="x":
                triangle(120,120)
            if char=="Y" or char=="y":
                triangle(125,125)
            if char=="Z" or char=="z":
                triangle(127,127)

trianglesize=trianglewave.tell()
squaresize=squarewave.tell()
sinesize=sinewave.tell()
wavesizes=[trianglesize,squaresize,sinesize]
maxsize=max(wavesizes)-44


if trianglecheck==0:
    for n in range(maxsize):
        bytevalue=128
        bytewrite=bytevalue.to_bytes(1,'big')
        trianglewave.write(bytewrite)

if squarecheck==0:
    for n in range(maxsize):
        bytevalue=128
        bytewrite=bytevalue.to_bytes(1,'big')
        squarewave.write(bytewrite)

if sinecheck==0:
    for n in range(maxsize):
        bytevalue=128
        bytewrite=bytevalue.to_bytes(1,'big')
        sinewave.write(bytewrite)

closefiles()

  
trianglefile = AudioSegment.from_file("triangle.wav")
squarefile = AudioSegment.from_file("square.wav")
sinefile = AudioSegment.from_file("sine.wav")

trianglesquare = trianglefile[:1000].overlay(squarefile)
trianglesquare.export('trianglesquare.wav', format='wav')
trianglesquaresine=trianglesquare[:1000].overlay(sinefile)
trianglesquaresine.export('waveform.wav', format='wav')
os.remove("triangle.wav")
os.remove("square.wav")
os.remove("sine.wav")
os.remove("trianglesquare.wav")
