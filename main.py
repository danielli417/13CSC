import sys
from sys import setrecursionlimit
from tkinter import *  # Importing all classes from tkinter module
import customtkinter
from PIL import Image, ImageTk
import random
#Home page
class HomePage:
    def nextpage(self):
        self.pframe.destroy()

    def help_page(self):
        self.about_image = Image.open("about.png")  # background image for the help button
        self.about_image_tk = ImageTk.PhotoImage(self.about_image)

        self.help_label = Label(self.pframe, image=self.about_image_tk)
        self.help_label.place(relx=0.5, rely=0.5, relwidth=0.30, relheight=0.25, anchor="center")



    def destroyhelp(self):
        self.help_label.destroy()

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

        # label for image
        self.image_label = Label(self.pframe, image=self.bg_image_tk)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always

        # setting a  image (using my canva design without any widgets)
        self.continue_image = Image.open("continuebutton.png")  # using my canva design
        self.continue_image_tk = ImageTk.PhotoImage(self.continue_image)

        # The button which allows the user to continue from the homepage into the quiz
        self.continue_button = Button(self.pframe, command=self.nextpage, image=self.continue_image_tk, background=background_color,
                                      activebackground=background_color, borderwidth = 0, cursor = "hand2")
        self.continue_button.place(relx=0.5, rely=0.8, anchor="center")

        # setting a  image (using my canva design without any widgets)
        self.question_image = Image.open("questionmark.png")  # using my canva design
        self.question_image_tk = ImageTk.PhotoImage(self.question_image)

        # The button which allows the user to continue from the homepage into the quiz
        self.question_button = Button(self.pframe, command=self.help_page, image=self.question_image_tk, background=background_color,
                                      activebackground=background_color, borderwidth = 0, cursor = "hand2")
        self.question_button.place(relx=0.62, rely=0.8, anchor="center")

        #creates label that has body text
        self.body_text = Label(self.pframe, font=("Inter", "30"), text="""Everyone at MRGS deserves running facilities, and you can help 
        us maintain this with only a little effort on your part. 
        This website allows you to report all instances of damage to the 
        school whenever spotted and the damage will be fixed as soon 
        as possible.""", fg="#FFFFFF", bg=background_color)
        self.body_text.place(relx=0.5,rely=0.55,anchor="center")


class choice:
    pass

root = Tk()  # create the main window
root.title("MRGS TOILETS")  # set the title of the window
root.attributes("-fullscreen", True)
program = HomePage(root)  # create an instance of HomePage and pass the root window
root.mainloop()  # start the Tkinter event loop to display the window and wait for user interaction