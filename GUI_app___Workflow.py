import tkinter as tk
from tkinter import filedialog, Text
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

def runApps():
    for app in apps:
        os.startfile(app)

#Setup frame and buttons
canvas = tk.Canvas(root, height = 500, widt = 500, bg = "gray17")
canvas.pack()

frame = tk.Frame(root, bg="gray57")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text = "Open file", padx = 10, pady = 5, fg = "gray57", bg = "gray17", command = addApp)
openFile.pack()

runApps = tk.Button(root, text = "Run apps", padx = 10, pady = 5, fg = "white", bg = "gray17", command = runApps)
runApps.pack()

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