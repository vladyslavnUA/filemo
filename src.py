# Python Built GUI for opening up applications on your 
# local directory with one click.

import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


if os.path.isfile('saved.txt'):
    with open('saved.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip('')]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="#D2A334")
        label.pack()

def runApps():
    for app in apps:
        os.system('open %a' % app)     # MAC
        # os.startfile(app)     # WINDOWS

canvas = tk.Canvas(root, height=700, width=700, bg="#34D244")
canvas.pack()

frame = tk.Frame(root, bg="#C9D234")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, 
                    pady=5, fg="blue", bg="#34D244", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, 
                    pady=5, fg="blue", bg="#34D244", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('saved.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')