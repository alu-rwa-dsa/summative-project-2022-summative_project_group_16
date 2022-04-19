# Importing the necessary modules
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *

# Defining a variable that stores a called tkinter function
win = Tk()

# Defining the dimensions of our GUI landing page
width_of_window = 427
height_of_window = 250
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
win.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
win.overrideredirect(1)

# Creating the progress bar
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress = Progressbar(win, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate', )


# Function that controls the progress bar
def load():
    # Displays the loading test on the window
    lbl = Label(win, text='Loading...', fg='white', bg=a)
    lbl_font = ('Calibri (Body)', 10)
    lbl.config(font=lbl_font)
    lbl.place(x=18, y=210)
    # Import the time module
    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        win.update_idletasks()
        time.sleep(0.03)
        r = r + 1
    # Current window is destoryed and the main function runs
    win.destroy()
    import main


progress.place(x=-10, y=235)

# Create frame dimensions
a = '#249794'
Frame(win, width=427, height=241, bg=a).place(x=0, y=0)
# Create button which when clicked the load function runs
b1 = Button(win, width=10, height=1, text='Place Order', command=load, border=0, fg=a, bg='white')
b1.place(x=170, y=200)

# Label containing text describing our project
l1 = Label(win, text='ORDER', fg='white', bg=a)
lst1 = ('Calibri (Body)', 18, 'bold')
l1.config(font=lst1)
l1.place(x=50, y=80)
# Label containing text describing our project
l2 = Label(win, text='DETAILS TRACKING', fg='white', bg=a)
lst2 = ('Calibri (Body)', 18)
l2.config(font=lst2)
l2.place(x=145, y=82)
# Label containing text describing our project
l3 = Label(win, text='APP', fg='white', bg=a)
lst3 = ('Calibri (Body)', 13)
l3.config(font=lst3)
l3.place(x=50, y=110)
# Calling the mainloop with the tkinter function to enable display of the landing page
win.mainloop()
