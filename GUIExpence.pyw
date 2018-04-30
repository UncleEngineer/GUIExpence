# Create by UncleEngineer
# fb.com/Uncle Engineer
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import webbrowser as web

data = []

def writecsv(event=None):
    global dc
    global ep

    dc = description.get()
    ep = int(expence.get())
    textshow = "{} {:,d}".format(dc,ep)
    result.set(textshow)
    
    data1 = [dc,ep]
    dt = datetime.now().strftime('%Y-%m-%d')
    filename = 'Expence-' + dt + '.csv'
    with open(filename, 'a', newline='') as filecsv:
        fcsv = csv.writer(filecsv)
        fcsv.writerow(data1)

    count = len(data)
    if count < 5:
        adddata0()
    else:
    	adddata()
        
def calculatetotal():

    dt = datetime.now().strftime('%Y-%m-%d')
    filename = 'Expence-' + dt + '.csv'
    expcal = []
    with open(filename, newline='') as readfile:
        readdata = csv.reader(readfile)
        listdata = list(readdata)
        
        for desc,exp in listdata[1:]:
            expcal.append(int(exp))

    total = sum(expcal)

    messagebox.showinfo('Total Expence (Today)','Total ' + '{:,d}'.format(total))

def adddata0():
    listbox.insert(0, "{}({})".format(dc,ep))
    
def adddata():
    listbox.insert(0, "{}({})".format(dc,ep))
    listbox.delete(END)
    
def readcsv():
    dt = datetime.now().strftime('%Y-%m-%d')
    filename = 'Expence-' + dt + '.csv'
    with open(filename, newline='') as readfile:
        readdata = csv.reader(readfile)
        
        for desc,exp in readdata:
            textvalue = "{} ({})\n".format(desc,exp)
            data.append(textvalue)

    #for item in data[-5:]:
    for item in data:
        listbox.insert(0, item)
            
def goweb():
	url = 'http://uncle-engineer.com/python'
	web.open(url)
def goface():
	url = 'https://www.facebook.com/UncleEngineer'
	web.open(url)

GUI = Tk()

menubar = Menu(GUI)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=goweb)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=GUI.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
cal = Menu(menubar, tearoff=0)
cal.add_command(label="Loss", command=goweb)
cal.add_command(label="Income", command=goweb)
cal.add_command(label="Expence", command=calculatetotal)
menubar.add_cascade(label="Calculate", menu=cal)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Uncle Engineer", command=goweb)
helpmenu.add_command(label="Facebook", command=goface)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
GUI.config(menu=menubar)

GUI.title('Uncle Engineer Expence')
GUI.geometry('600x600')
GUI.bind('<Return>',writecsv)

description = StringVar()
expence = StringVar()
result = StringVar()
history = StringVar()

L1 = ttk.Label(GUI, text= 'Description: ').pack(padx=10,pady=5)
E1 = ttk.Entry(GUI, textvariable= description, font=('TH Sarabun New',22))
E1.pack(padx=10,pady=5)

L2 = ttk.Label(GUI, text= 'Expence(Baht): ')
L2.pack(padx=10,pady=5)
E2 = ttk.Entry(GUI, textvariable= expence, font=('TH Sarabun New',22))
E2.pack(padx=10,pady=5)
#Button


B1 = ttk.Button(GUI, text= 'Add', command=writecsv)
B1.pack(padx=10,pady=10)


R1 = ttk.Label(GUI, textvariable=result, foreground='green',font=('TH Sarabun New',30,'bold'))
R1.pack(padx=10,pady=5)

# Listbox
global listbox

listbox = Listbox(GUI,font=('TH Sarabun New',20),width=50)
listbox.pack(pady=20)


try:
    readcsv()
except FileNotFoundError:
    
    dt = datetime.now().strftime('%Y-%m-%d')
    header = ['Description','Expence']
    filename = 'Expence-' + dt + '.csv'
    with open(filename, 'a', newline='') as filecsv:
        fcsv = csv.writer(filecsv)
        fcsv.writerow(header)


GUI.mainloop()
