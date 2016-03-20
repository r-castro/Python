from tkinter import *


class App(Frame):
    """Documentation for LabelDemo
    
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.pack()

myapp = App()

myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

myapp.mainloop()
