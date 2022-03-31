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
    
def AddNote(note, duration):
    global time
    MyMIDI.addNote(track, channel, note, time, duration/5, volume)
    time=time+(duration/5)          
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
                if char=="B" or char=="b":
                        AddNote(61,1)
                if char=="C" or char=="c":
                        AddNote(61,2)
                if char=="D" or char=="d":
                        AddNote(62,3)
                if char=="G" or char=="g":
                        AddNote(62,4)
                if char=="J" or char=="j":
                        AddNote(63,5)
                if char=="O" or char=="o":
                        AddNote(63,6)
                if char=="P" or char=="p":
                        AddNote(64,7)
                if char=="Q" or char=="q":
                        AddNote(64,8)
                if char=="R" or char=="r":
                        AddNote(65,9)
                if char=="S" or char=="s":
                        AddNote(65,10)
                if char=="U" or char=="u":
                        AddNote(65,11)
                if char=="E" or char=="e":
                        AddNote(66,1)
                if char=="F" or char=="f":
                        AddNote(66,2)
                if char=="H" or char=="h":
                        AddNote(66,3)
                if char=="I" or char=="i":
                        AddNote(67,4)
                if char=="L" or char=="l":
                        AddNote(67,5)
                if char=="T" or char=="t":
                        AddNote(67,6)
                if char=="A" or char=="a":
                        AddNote(68,1)
                if char=="K" or char=="k":
                        AddNote(68,2)
                if char=="M" or char=="m":
                        AddNote(69,3)
                if char=="N" or char=="n":
                        AddNote(69,4)
                if char=="V" or char=="v":
                        AddNote(70,5)
                if char=="X" or char=="x":
                        AddNote(70,6)
                if char=="Y" or char=="y":
                        AddNote(71,7)
                if char=="W" or char=="w":
                        AddNote(72,8)
                if char=="Z" or char=="z":
                        AddNote(72,9)

    WriteFile()

          
Convert.bind("<Button-1>",GenerateMelody)
quitbutton.bind("<Button-1>",QuitApp)
clearbutton.bind("<Button-1>", ClearTextBox)
pastebutton.bind("<Button-1>",paste_from_button)
root.bind("<Button-3>", context_menu)

textbox.focus_set()

root.mainloop()
    
    
