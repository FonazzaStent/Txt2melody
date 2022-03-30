import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
from tkinter.filedialog import asksaveasfilename
import os
import subprocess
import io
import math
from midiutil import MIDIFile

img=b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH5gMeDgAyOeZ0yQAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABRSURBVCjPtVI5DgAwCIKm/3+SH3Owm+kVe6RlVAgBpZlhBpIAxm3CIV4LSIpIM4kzOJy2cLgJ3Wn+tFSb/L9DDqpcOOywX2eYPkGq16oaswEU+FwjPek/kRkAAAAASUVORK5CYII='

root= tk.Tk()
top= root
top.geometry("600x450+468+138")
top.resizable(0,0)
top.title("Convert Text to Melody")
favicon=tk.PhotoImage(data=img) 
root.wm_iconphoto(True, favicon)

#Paste button
pastebutton=tk.Button(top)
pastebutton.place(relx=0.230,rely=0.911,height=24,width=67)
pastebutton.configure(text='''Paste''')

#Convert button
Convert=tk.Button(top)
Convert.place(relx=0.367, rely=0.911, height=24, width=100)
Convert.configure(text='''Generate Melody''')

#Textbox
textbox = Text(top)
textbox.place(relx=0.033, rely=0.022, relheight=0.878, relwidth=0.933)
scroll_1=Scrollbar (top)
scroll_1.pack(side=RIGHT, fill=Y)
textbox.configure(yscrollcommand=scroll_1.set)
scroll_1.configure(command=textbox.yview)

#clear button
clearbutton=tk.Button(top)
clearbutton.place (relx=0.550, rely=0.911, height=24, width=34)
clearbutton.configure(text='''Clear''')

#quit button
quitbutton=tk.Button(top)
quitbutton.place (relx=0.620, rely=0.911, height=24, width=34)
quitbutton.configure(text='''Quit''')

def paste_text():
        textbox.event_generate(("<<Paste>>"))

menu = Menu(root, tearoff = 0)
menu.add_command(label="Paste", command=paste_text)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()

def paste_from_button(event):
        textbox.event_generate(("<<Paste>>"))

def Convertfn(event):
    global text
    text=textbox.get(1.0,2000.0)
    if text!='':
        asciitxt=unidecode(text)
    textbox.delete(1.0,2000.0)
    textbox.insert(INSERT, asciitxt)

def Copyfn(event):
    global text
    text=textbox.get(1.0,2000.0)
    pyperclip.copy(text)

def ClearTextBox(event):
    textbox.delete(1.0,2000.0)

def QuitApp(event):
    top.destroy()
    
def AddNote(note, duration, timevalue):
    global time
    time=time+timevalue
    MyMIDI.addNote(track, channel, note, time, duration/5, volume)
              
def WriteFile():
    data=[('MIDI', '*.mid')]
    midifile=asksaveasfilename(filetypes= data, defaultextension= data)
    if os.path.isfile(midifile)== True:
            os.remove(midifile)
    if str(midifile)!='':
        midifilesave=open(midifile,'wb')
        MyMIDI.writeFile(midifilesave)
        midifilesave.close()

#Generate Melody
        
def GenerateMelody(event):
    global track
    track    = 0
    global channel
    channel  = 0
    global time
    time     = 0    # In beats
    #global duration
    #duration = 0.1   # In beats
    global tempo
    tempo    = 100   # In BPM
    global volume
    volume   = 100  # 0-127, as per the MIDI standard

    global MyMIDI
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
    MyMIDI.addTempo(track, time, tempo)
    global text
    text=textbox.get(1.0,2000.0)
    if text=='':
        text="Hello World"
    textlength=len(text)
    for letters in range (0,textlength):
        char=text[letters]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123) or char==" ":
            if char=="A":
                AddNote(69,1,0.2)
            if char=="K":
                AddNote(69,2, 0.4)
            if char=="M":
                AddNote(69,3, 0.6)
            if char=="N":
                AddNote(69,4, 0.8)
            if char=="Z":
                AddNote(69,5, 1)
            if char=="k":
                AddNote(70,1, 0.2)
            if char=="z":
                AddNote(70,2, 0.4)
            if char=="V":
                AddNote(71,1, 0.2)
            if char=="W":
                AddNote(71,2, 0.4)
            if char=="X":
                AddNote(71,3, 0.6)
            if char=="Y":
                AddNote(71,4, 0.8)
            if char=="v":
                AddNote(60,1, 0.2)
            if char=="w":
                AddNote(60,2, 0.4)
            if char=="x":
                AddNote(60,3, 0.6)
            if char=="y":
                AddNote(60,4, 0.8)
            if char=="E":
                AddNote(65,1, 0.2)
            if char=="F":
                AddNote(65,2, 0.4)
            if char=="I":
                AddNote(65,3, 0.6)
            if char=="f":
                AddNote(66,1, 0.2)
            if char=="h":
                AddNote(66,3, 0.6)
            if char=="m":
                AddNote(66,4, 0.8)
            if char=="n":
                AddNote(66,5,1)
            if char=="r":
                AddNote(66,6,1.2)
            if char=="t":
                AddNote(66,7,1.4)
            if char=="H":
                AddNote(67,1,0.2)
            if char=="I":
                AddNote(67,2,0.4)
            if char=="L":
                AddNote(67,3,0.6)
            if char=="T":
                AddNote(67,4,0.8)
            if char=="i":
                AddNote(68,2,0.4)
            if char=="l":
                AddNote(68,2,0.4)
            if char=="B":
                AddNote(61,1,0.2)
            if char=="D":
                AddNote(61,1,0.2)
            if char=="J":
                AddNote(61,2,0.4)
            if char=="O":
                AddNote(61,3,0.6)
            if char=="P":
                AddNote(61,4,0.8)
            if char=="Q":
                AddNote(61,5,1)
            if char=="b":
                AddNote(62,1,0.2)
            if char=="j":
                AddNote(62,2,0.4)
            if char=="o":
                AddNote(62,3,0.6)
            if char=="p":
                AddNote(62,4,0.8)
            if char=="C":
                AddNote(63,1,0.2)
            if char=="G":
                AddNote(63,2,0.4)
            if char=="R":
                AddNote(63,3,0.6)
            if char=="S":
                AddNote(63,4,0.8)
            if char=="U":
                AddNote(63,5,1)
            if char=="a":
                AddNote(64,1,0.2)
            if char=="c":
                AddNote(64,2, 0.4)
            if char=="d":
                AddNote(64,3,0.6)
            if char=="e":
                AddNote(64,4,0.8)
            if char=="g":
                AddNote(64,5,1)
            if char=="q":
                AddNote(64,6,1.2)
            if char=="s":
                AddNote(64,7,1.4)
            if char=="u":
                AddNote(64,8,1.6)
    WriteFile()

          
Convert.bind("<Button-1>",GenerateMelody)
quitbutton.bind("<Button-1>",QuitApp)
clearbutton.bind("<Button-1>", ClearTextBox)
pastebutton.bind("<Button-1>",paste_from_button)
root.bind("<Button-3>", context_menu)

textbox.focus_set()

root.mainloop()
    
    
