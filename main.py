from tkinter import *
from tkinter import messagebox
import pickle

#----------------On tkinter window load function call--------------#
def loaddata():
    task = pickle.load(open("task.dat","rb"))
    for i in task:
        lb.insert(END, i)

#------------------Tkinter layout---------------------#
window = Tk()
window.geometry('500x450+500+200')
window.title("To-Do List")
window.config(bg="#223441")
window.resizable(0,0)
window.after_idle(loaddata)

#------------------------Functions------------------#
#add task
def addtask():
    task = my_entry.get()
    if task != "":
        lb.insert(END,task)
        my_entry.delete(0,END)
    else:
        messagebox.showwarning("Warning", "Please enter some task")

#delete task
def deltask():
    lb.delete(ANCHOR)

#save data
def savedata():
    end_index = lb.index("end")
    ok = messagebox.askokcancel("Quit", "Do you want to Quit?")
    if ok:
        if end_index > 0:
            task = lb.get(0,lb.size())
            pickle.dump(task, open("task.dat","wb"))
        else:
            messagebox.showwarning("Warning", "List is empty")
        window.destroy()
        
#---------------------------GUI----------------------#
frame = Frame(window)
frame.pack(pady=10)

#-----------Listbox---------#
lb = Listbox(
    frame,
    width = 30,
    height = 8,
    font=('Times',18),
    bd = 0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side = LEFT, fill=BOTH)

#------------scrollbar---------------#
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#-----------Entry Box---------#
my_entry = Entry(
    window,
    font=('Times',18),
)
my_entry.pack(pady=20)

#------------Buttons-----------#
#button frame
button_frame = Frame(window)
button_frame.pack(pady=20)

#Add button
add_task = Button(
    button_frame,
    text='Add Text',
    font = ("Times", 12),
    bg='#c5f776',
    padx=15,
    pady = 10,
    command = addtask
)
add_task.pack(fill=BOTH, expand=TRUE, side = LEFT)

#Delete button
del_task = Button(
    button_frame,
    text ='Delete Text',
    font = ("Times", 12),
    bg = '#ff8b61',
    padx=15,
    pady = 10,
    command = deltask
)
del_task.pack(fill=BOTH, expand=TRUE, side = LEFT)

window.protocol("WM_DELETE_WINDOW",savedata)
window.mainloop()   