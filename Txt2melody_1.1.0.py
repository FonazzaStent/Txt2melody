import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.filedialog import asksaveasfilename
import os
from midiutil import MIDIFile

img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH5gQHCzMaYcK/7QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAICSURBVFjD7Ze9zylBFId/PjZvLAqFRIJOoRIkCoVESKiVCoVSpdroiZ5/QUWnUiytRiQSUVIoRLIUS2GzH3HeioiLi71Wc59kmt3MzLNzzuyZMRERQQeapoHneRyPRySTSTgcjtcGIJ1sNhsCQABoOp2+3N8MnVwuoCiKL/fXLXDJeDx+6wt0IQjCOQQMw9BisTA2BJeoqopyuYz1ev2dFTi1eDxOk8nkqf4fETiFo9VqkaIo3xE4tVqtRrIsGyPAcRxls9k/JDqdjjECs9mMZFmmXq9HXq/3/DwUCpEkScYInBiNRsQwzPmdIAif34aXxGIx1Ot1AIDb7QbLsp//E16TSqUAAIVCAXa73XgBl8sFAMjn88bUgmsURQHHcYhEIt8RAIBKpQKLxXL3vfWTkweDQWPL8Tv8F3g6B4gIkiRBURRYrVawLAuz2fx5AUEQMBgM0O12wfM8drsdfn5+kE6nkcvlEA6HdR8q79Lv98nv9z8styaT6WYteJa7KzAcDpHJZPC3a4POa8XtJFRVFdVqVffgbwuIogie57+3DW02Gzwez8uDOZ3Of5eEjUbjYfJdt2KxSJqmvZyEdwX2+z2VSqWnJk8kErRcLt86UT3chpIkUbvdpmg0enNin89HzWaTttvt20c60zPXc0mSMJ/PsVqtcDgczjkSCATei/sFv609YQ6jT2hbAAAAAElFTkSuQmCC'

root= tk.Tk()
top= root
top.geometry("600x450+468+138")
top.resizable(0,0)
top.title("Convert Text to Melody")
favicon=tk.PhotoImage(data=img) 
root.wm_iconphoto(True, favicon)


#Textbox
def create_textbox():
        global textbox
        textbox = Text(top)
        textbox.place(relx=0.033, rely=0.022, relheight=0.918, relwidth=0.933)
        scroll_1=Scrollbar (top)
        scroll_1.pack(side=RIGHT, fill=Y)
        textbox.configure(yscrollcommand=scroll_1.set)
        scroll_1.configure(command=textbox.yview)

def paste_text():
        textbox.event_generate(("<<Paste>>"))


def context_menu(event):
        try:
                menupaste.tk_popup(event.x_root, event.y_root)
        finally:
                menupaste.grab_release()

def paste_from_button(event):
        textbox.tag_add(SEL, "1.0", END)
        textbox.event_generate(("<<Paste>>"))

def Convertfn(event):
    global text
    text=textbox.get(1.0,2000.0)
    if text!='':
        asciitxt=unidecode(text)
    textbox.delete(1.0,2000.0)
    textbox.insert(INSERT, asciitxt)

def ClearTextBox():
    textbox.delete(1.0,2000.0)

def QuitApp():
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
        
def GenerateMelody():
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

#menu
def create_menu():
        menubar=tk.Menu(top, tearoff=0)
        top.configure(menu=menubar)
        sub_menu=tk.Menu(top, tearoff=0)
        menubar.add_cascade(menu=sub_menu,compound="left", label="Edit")
        sub_menu.add_command(compound="left", label="Paste", command=paste_text)
        sub_menu.add_command(compound="left",label="Clear", command=ClearTextBox)
        sub_menu1=tk.Menu(top, tearoff=0)
        menubar.add_cascade(menu=sub_menu1,compound="left", label="Convert")
        sub_menu1.add_command(compound="left", label="Generate Melody", command=GenerateMelody)
        menubar.add_command(compound="left",label="Quit", command=QuitApp)

#contextmenu
def create_context_menu():
        global menupaste
        root.bind("<Button-3>", context_menu)
        menupaste = Menu(root, tearoff = 0)
        menupaste.add_command(label="Paste", command=paste_text)

#main procedure
def main():
        create_textbox()
        create_menu()
        create_context_menu()
        textbox.focus_set()
main()
root.mainloop()
    
    
