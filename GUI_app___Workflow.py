import tkinter as tk
from tkinter import filedialog, Text, RIGHT
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'): #Load save file.
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp(): #add application to list.
    
    #Delete a empty row.
    for widget in frame.winfo_children():
        widget.destroy()
    
    #setup search dialog for searching applications
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("executables", "*.exe"), ("all files", "*.")))

    #Print destination app
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()

def runApps(): #Run selected apps
    for app in apps:
        os.startfile(app)

def deleteSave(): #Delete save file and clean the frame of any saved applications
    try:
        os.remove("save.txt")
        del apps[:]
        for widget in frame.winfo_children():
            widget.destroy()
    except:
        pass
    

#Setup frame and buttons
canvas = tk.Canvas(root, height = 500, widt = 500, bg = "gray17")
canvas.pack()

frame = tk.Frame(root, bg="gray57")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

deleteSave = tk.Button(root, text = "Delete save file", padx = 10, pady = 10, fg = "white", bg = "gray17", command = deleteSave)
deleteSave.pack(side = RIGHT)

runApps = tk.Button(root, text = "Run apps", padx = 10, pady = 10, fg = "white", bg = "gray17", command = runApps)
runApps.pack(side = RIGHT)

openFile = tk.Button(root, text = "Open file", padx = 10, pady = 10, fg = "gray57", bg = "gray17", command = addApp)
openFile.pack( side = RIGHT)

#print saved programs from last time so you can continue working with same programs.
for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

#Load main program
root.mainloop()

#Generate save file when app will be closed.
with open('save.txt', 'w') as f: 
    for app in apps:
        f.write(app + ',')