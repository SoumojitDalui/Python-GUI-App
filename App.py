import tkinter as tk
from tkinter import filedialog, Text
import os

root=tk.Tk()
apps=[]

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    #filename=filedialog.askopenfile(initialdir="/Applications",title="Select File",filetypes=(("app","*.app"),("all files","*.*"))

    apps.append(filename)
    print(filename)

    for app in apps:
        label=tk.Label(frame,Text=app)
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas=tk.Canvas(root,height=700,width=700, bg="#63B82C")
canvas.pack()

frame=tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

openFile=tk.Button(root,text="Open File",padx=320,pady=5,bg="#B8B23B",command=addApp)
openFile.pack()

runApps=tk.Button(root,text="Run the Applications",padx=288,pady=5,bg="#B8B23B",command=runApps)
runApps.pack()

root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app+',')