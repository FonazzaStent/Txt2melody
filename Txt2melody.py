import os
import math
from midiutil import MIDIFile

text= open("text.txt")
if os.path.isfile("melody.mid")== True:
    os.remove("melody.mid")
midifile= open("melody.mid",'wb')

track    = 0
channel  = 0
time     = 0    # In beats
duration = 0.1   # In beats
tempo    = 100   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

    
def sine(note, duration):
    MyMIDI.addNote(track, channel, note, time, duration/5, volume)
    
    
def triangle (note, duration):
    MyMIDI.addNote(track, channel, note, time, duration/5, volume)
    

def square (note, duration):
    MyMIDI.addNote(track, channel, note, time, duration/5, volume)
    
              
def end():
    text.close
    midifile.close

for letters in range (1,20):
    char=text.read(1)
    if char=='':
        end
    else:
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123) or char==" ":
            if char=="A":
                triangle(69,1)
                time=time+0.2
            if char=="K":
                triangle(69,2)
                time=time+0.4
            if char=="M":
                triangle(69,3)
                time=time+0.6
            if char=="N":
                triangle(69,4)
                time=time+0.8
            if char=="Z":
                triangle(69,5)
                time=time+1
            if char=="k":
                triangle(70,1)
                time=time+0.2
            if char=="z":
                triangle(70,2)
                time=time+0.4
            if char=="V":
                triangle(71,1)
                time=time+0.2
            if char=="W":
                triangle(71,2)
                time=time+0.4
            if char=="X":
                triangle(71,3)
                time=time+0.6
            if char=="Y":
                triangle(71,4)
                time=time+0.8
            if char=="v":
                triangle(60,1)
                time=time+0.2
            if char=="w":
                triangle(60,2)
                time=time+0.4
            if char=="x":
                triangle(60,3)
                time=time+0.6
            if char=="y":
                triangle(60,4)
                time=time+0.8
            if char=="E":
                square(65,1)
                time=time+0.2
            if char=="F":
                square(65,2)
                time=time+0.4
            if char=="I":
                square(65,3)
                time=time+0.6
            if char=="f":
                square(66,1)
                time=time+0.2
            if char=="h":
                square(66,3)
                time=time+0.6
            if char=="m":
                square(66,4)
                time=time+0.8
            if char=="n":
                square(66,5)
                time=time+1
            if char=="r":
                square(66,6)
                time=time+1.2
            if char=="t":
                square(66,7)
                time=time+1.4
            if char=="H":
                square(67,1)
                time=time+0.2
            if char=="I":
                square(67,2)
                time=time+0.4
            if char=="L":
                square(67,3)
                time=time+0.6
            if char=="T":
                square(67,4)
                time=time+0.8
            if char=="i":
                square(68,2)
                time=time+0.4
            if char=="l":
                square(68,2)
                time=time+0.4
            if char=="B":
                sine(61,1)
                time=time+0.2
            if char=="D":
                sine(61,1)
                time=time+0.2
            if char=="J":
                sine(61,2)
                time=time+0.4
            if char=="O":
                sine(61,3)
                time=time+0.6
            if char=="P":
                sine(61,4)
                time=time+0.8
            if char=="Q":
                sine(61,5)
                time=time+1
            if char=="b":
                sine(62,1)
                time=time+0.2
            if char=="j":
                sine(62,2)
                time=time+0.4
            if char=="o":
                sine(62,3)
                time=time+0.6
            if char=="p":
                sine(62,4)
                time=time+0.8
            if char=="C":
                sine(63,1)
                time=time+0.2
            if char=="G":
                sine(63,2)
                time=time+0.4
            if char=="R":
                sine(63,3)
                time=time+0.6
            if char=="S":
                sine(63,4)
                time=time+0.8
            if char=="U":
                sine(63,5)
                time=time+1
            if char=="a":
                sine(64,1)
                time=time+0.2
            if char=="c":
                sine(64,2)
                time=time+0.4
            if char=="d":
                sine(64,3)
                time=time+0.6
            if char=="e":
                sine(64,4)
                time=time+0.8
            if char=="g":
                sine(64,5)
                time=time+1
            if char=="q":
                sine(64,6)
                time=time+1.2
            if char=="s":
                sine(64,7)
                time=time+1.4
            if char=="u":
                sine(64,8)
                time=time+1.6
MyMIDI.writeFile(midifile)
                
end
    
    
