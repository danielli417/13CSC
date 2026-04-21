import sys
from sys import setrecursionlimit
from tkinter import *  # Importing all classes from tkinter module
from PIL import Image, ImageTk
import random
#Home page
class HomePage:
    def nextpage(self):
        self.pframe.destroy()
    def __init__(self, parent):
        #makes variables that have the value of the parent screen width (eg if a device aspect ratio is 3:4, the variables are 3:4)
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()
        background_color = "#364156"

        # frame set up
        self.pframe = Frame(parent, bg=background_color)
        self.pframe.pack(fill=BOTH, expand=TRUE)


        #setting a background image (using my canva design without any widgets)
        self.bg_image = Image.open("Homepage.png") #using my canva design
        self.bg_image = self.bg_image.resize((self.window_width, self.window_height), Image.LANCZOS) #resizes the image to match the parent aspect ratio
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)

root = Tk()  # create the main window
root.title("MRGS TOILETS")  # set the title of the window
root.attributes("-fullscreen", True)
program = HomePage(root)  # create an instance of HomePage and pass the root window
root.mainloop()  # start the Tkinter event loop to display the window and wait for user interaction