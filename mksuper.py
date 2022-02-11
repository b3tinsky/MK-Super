from tkinter import *
from time import sleep
from random import randrange
from keyboard import add_hotkey, unhook_all_hotkeys
from pickle import dump, load
from os import getcwd
from pathlib import Path

print('''  
                                                       `-.`'.-'                                    
                                                      `-.        .-'.                              
                                                   `-.    -./\.-    .-'                            
                                                       -.  /_|\  .-                                
                                                   `-.   `/____\'   .-'.                           
                                                `-.    -./.-""-.\.-      '                         
                                                   `-.  /< (()) >\  .-'                            
                                                 -   .`/__`-..-'__\'   .-                          
                                               ,...`-./___|____|___\.-'.,.                         
                                                  ,-'   ,` . . ',   `-,                            
                                               ,-'   ________________  `-,                         
                                                  ,'/____|_____|_____\'                            
                                   
                                   
Hello stranger, this program has the intention of adding personalized subliminal messages to your mind (as a way to hack yourself). The main purpose is helping you generate your own desires and goals (not the ones by third parties). Add the subliminals you would like to see, and they will randomly flash on your screen in random intervals (from 0 to 20 seconds). Do not use this program if you begin to feel headaches, nausea or dizziness. Do not use this program for extended time frames. Do not use this program with others. Enjoy.

| INFO |
- The middle box is for writing your subliminals
- The outer boxes are for time intervals in seconds. From (left box) to (right box). The default times are 0 to 20 seconds.
Example: [1][I LIKE TO READ][5], it will flash I LIKE TO READ in random intervals from 1 to 5 seconds.
- You can save a set of subliminals with the VAULT button
- Shorter subliminals are better
- Don't use negations in your subliminals
Example: I never get tired, I don't cheat
- Think through your subliminals, since they could have unintended effects.
Example: If you feel sleepy at work, do not use [I'M NOT SLEEPY], as it may cause trouble sleeping at night
- Try only using affirmations
Example: [I AM PRODUCTIVE][I LOVE READING][I AM ENERGETIC]

| HOTKEYS |
ENTER - It sets the current text in the box to Subliminals
SHIFT+ENTER - It sets the specified times (Both boxes must have a number inside)
CTRL+ENTER - It plays Subliminals
CTRL+SHIFT+ENTER - It plays Vault
BACKSPACE - It deletes a subliminal
''')

add_hotkey("enter", lambda: setSubliminal())
add_hotkey("shift+enter", lambda: setTimes())
add_hotkey("ctrl+enter", lambda: playSubliminals())
add_hotkey("ctrl+shift+enter", lambda: playVault())
add_hotkey("backspace", lambda: deleteSubliminal())

retrievedVault = []
subliminals = []
vault = []
times = [0, 20]

if Path(getcwd() + '/MK_VAULT.dat').exists():
    retrievedVault = load(open("MK_VAULT.dat", "rb"))

root= Tk()

canvas1 = Canvas(root, width = 400, height = 300, bg="#000")
canvas1.pack()

subliminalEntry = Entry(root, bg="#000", fg="#f0f", justify="center", font=('Iosevka', 10)) 
canvas1.create_window(200, 140, window=subliminalEntry)
initialTimeEntry = Entry(root, width = 3, bg="#000", fg="#0f0", justify="center", font=('Iosevka', 10)) 
canvas1.create_window(120, 140, window=initialTimeEntry)
finalTimeEntry = Entry(root, width = 3, bg="#000", fg="#0f0", justify="center", font=('Iosevka', 10)) 
canvas1.create_window(280, 140, window=finalTimeEntry)
label1 = Label(root, text='PROJECT MK SUPER')
label1.config(font=('Haettenschweiler', 25), bg="#000" ,fg="#fff")
canvas1.create_window(200, 25, window=label1)

def setTimes():
    times.pop()
    times.pop()
    times.append(initialTimeEntry.get())
    times.append(finalTimeEntry.get())
    initialTimeEntry.delete(0, len(initialTimeEntry.get()))
    finalTimeEntry.delete(0, len(finalTimeEntry.get()))


def setSubliminal():  
    message = subliminalEntry.get()
    subliminals.append(message)
    currentSubliminals_list.insert(END, message)
    subliminalEntry.delete(0, len(message))

def deleteSubliminal():
    if(currentSubliminals_list.get(ANCHOR) != ''):
        subliminals.remove(currentSubliminals_list.get(ANCHOR))
        currentSubliminals_list.delete(ANCHOR)
    if(vault_list.get(ANCHOR) != ''):
        vault.remove(vault_list.get(ANCHOR))
        vault_list.delete(ANCHOR)
        dump(vault, open("MK_VAULT.dat", "wb"))


def playSubliminals():
    unhook_all_hotkeys()   
    root.destroy() 

def playVault():
    if subliminals:
        for x in range(len(subliminals)):
            subliminals.pop()
    subliminals.extend(vault)
    unhook_all_hotkeys()   
    root.destroy() 

def saveSubliminals():  
    if subliminals:
        vault_list.delete(0, END)
        vault = subliminals
        for x in vault:
            vault_list.insert(END, x)
        dump(vault, open("MK_VAULT.dat", "wb"))

# Buttons
button1 = Button(text='SET', command=setSubliminal, font=('Iosevka', 10), bg="#000", fg="#fff", width=16)
button2 = Button(text='SAVE', command=saveSubliminals, font=('Iosevka', 10),bg="#000", fg="#fff", width=16)
button3 = Button(text='PLAY SUBLIMINALS', command=playSubliminals, font=('Iosevka', 10),bg="#000", fg="#fff", width=16)
button4 = Button(text='PLAY VAULT', command=playVault, font=('Iosevka', 10), bg="#000", fg="#fff", width=16)

canvas1.create_window(200, 170, window=button1)
canvas1.create_window(200, 200, window=button2)
canvas1.create_window(200, 230, window=button3)
canvas1.create_window(200, 260, window=button4)


# Current Subliminals
currentSubliminals_label = Label(root, text='SUBLIMINALS')
currentSubliminals_label.config(font=('Haettenschweiler', 17), bg="#000" ,fg="#fff")
currentSubliminals_label.pack(fill="x", anchor="w")
currentSubliminals_list = Listbox(root, bg="#000", fg="#f00", highlightcolor="#f00", selectbackground="#f00", selectforeground="#fff", justify="center", font=('Iosevka', 16)) 
currentSubliminals_list.pack(side = TOP, anchor="w", fill = BOTH)
currentSubliminals_scrollbar = Scrollbar(root)       
currentSubliminals_list.config(yscrollcommand = currentSubliminals_scrollbar.set)  
currentSubliminals_scrollbar.config(command = currentSubliminals_list.yview) 

# Saved Subliminals
vault_label = Label(root, text='VAULT')
vault_label.config(font=('Haettenschweiler', 17), bg="#000" ,fg="#fff")
vault_label.pack(fill="x", anchor="w")
vault_list = Listbox(root, bg="#000", fg="#00f", highlightcolor="#00f", selectbackground="#00f", selectforeground="#fff", justify="center", font=('Iosevka', 16)) 
vault_list.pack(side = TOP, anchor="w", fill = BOTH)  
vault_scrollbar = Scrollbar(root)       
vault_list.config(yscrollcommand = vault_scrollbar.set)  
vault_scrollbar.config(command = vault_list.yview) 

# Validate if there is a saved vault
if retrievedVault:
    vault = retrievedVault
    for x in vault:
        vault_list.insert(END, x)

root.mainloop()

length = len(subliminals)

if length == 0:
    sys.exit(0)

while True:
    window = Tk()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    window.wm_attributes('-fullscreen','true', '-topmost', 'true')
    text = Text(window, font=("Haettenschweiler",100), bg='#000', fg='#fff', wrap='word', pady='250')
    subliminal = subliminals[randrange(length)]
    text.tag_configure("center", justify='center')
    text.insert(INSERT, subliminal)
    text.tag_add("center", "1.0", "end")
    text.pack()

    window.geometry('%dx%d+%d+%d' %(ws, hs, 0, 0))

    window.update()
    text.delete(1.0,END)
    sleep(0.1)
    window.destroy()

    sleep(randrange(int(times[0]), int(times[1])))