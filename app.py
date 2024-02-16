from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo('', 'Thanks Magal')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('survey')  # Fixed typo: 'title' to 'title'
root.resizable(width=False, height=False)
root['bg'] = 'white'

# Use a Label widget instead of reusing the name 'Label'
question_label = Label(root, text='Você é gay?', font='Arial 20 bold', bg='white')
question_label.pack()

# Create and place the 'Sim' (Yes) button
btnYes = Button(root, text='Não', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)  # Corrected method name to 'bind'

# Create and place the 'Não' (No) button
btnNo = Button(root, text='Sim', font='Arial 20 bold', command=no)
btnNo.place(x=350, y=100)

root.mainloop()



