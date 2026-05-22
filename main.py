import sys
from sys import setrecursionlimit
from tkinter import *  # Importing all classes from tkinter module
import customtkinter
import pywinstyles
from PIL import Image, ImageTk
import random
#Home page

class HomePage:
    def nextpage(self):
        self.pframe.destroy()
        Choice(root)
    def help_page(self):
        #sets a label which looks like a popup, and will contain text explaining what the program is meant to do
        self.about_image = Image.open("about.png")  # background image for the help button
        self.about_image_tk = ImageTk.PhotoImage(self.about_image)
        self.help_label = Label(self.pframe, image=self.about_image_tk, bg = "#3d3739")
        self.help_label.place(relx=0.5, rely=0.5, anchor="center")
        pywinstyles.set_opacity(self.help_label, color="#3d3739")

        #sets a button with an x sign, which will close the popup when clicked on
        self.exithelp_image = Image.open("exithelp.png")  # using my canva design
        self.exithelp_image_tk = ImageTk.PhotoImage(self.exithelp_image)

        self.exithelp_button = Button(self.pframe, command=self.destroyhelp, image=self.exithelp_image_tk, borderwidth=0, cursor="hand2", bg = "#3d3739")
        self.exithelp_button.place(relx=0.655, rely=0.385, anchor="center")
        pywinstyles.set_opacity(self.exithelp_button, color="#3d3739")

        self.help_text = Label(self.pframe, text = """This program allows students to report 
        damage within the school’s toilets, and will 
        help our staff repair damage and clean the 
        bathroom faster. Press CONTINUE to report""", font=("Inter", "22"), fg="#ffffff", bg = "#4e4a59") #HAVE TO FIX THIS
        self.help_text.place(relx=0.49, rely=0.5, anchor="center")

    def destroyhelp(self):
        self.help_label.destroy()
        self.exithelp_button.destroy()
        self.help_text.destroy()

    def shutdown(self):
        exit()

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

        # setting a image (using my canva design without any widgets)
        self.continue_image = Image.open("continuebutton.png")  # using my canva design
        self.continue_image_tk = ImageTk.PhotoImage(self.continue_image)

        # The button which allows the user to continue from the homepage into the quiz
        self.continue_button = Button(self.pframe, command=self.nextpage, image=self.continue_image_tk, background=background_color,
                                      activebackground=background_color, borderwidth = 0, cursor = "hand2")
        self.continue_button.place(relx=0.5, rely=0.8, anchor="center")

        # sets a button with an x sign, which will close the program when clicked on
        self.shutdown_image = Image.open("exithelp.png")
        self.shutdown_image_tk = ImageTk.PhotoImage(self.shutdown_image)

        self.shutdown_button = Button(self.pframe, command=self.shutdown, image=self.shutdown_image_tk, background=background_color,
                                      activebackground=background_color, borderwidth = 0, cursor = "hand2")
        self.shutdown_button.place(relx=0.95, rely=0.08, anchor="center")

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


class Choice:
    def backpage(self):
        self.pframe.destroy()
        HomePage(root)
    def nextpage(self):
        self.pframe.destroy()
        Selector(root)

    def clicked_a(self):
        global a_or_e
        a_or_e = 1 #this variable is changed to a (1 = a, 0 = e)
        self.nextpage()

    def shutdown(self):
        exit()

    def __init__(self, parent):
        # makes variables that have the value of the parent screen width (eg if a device aspect ratio is 3:4, the variables are 3:4)
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()
        background_color = "#364156"
        button_color = "#01122e"
        global a_or_e
        a_or_e = 0

        # frame set up
        self.pframe = Frame(parent, bg=background_color)
        self.pframe.pack(fill=BOTH, expand=TRUE)

        # setting a background image (using my canva design without any widgets)
        self.bg_image2 = Image.open("choice.png")  # using my canva design
        self.bg_image2 = self.bg_image2.resize((self.window_width, self.window_height),
                                             Image.LANCZOS)  # resizes the image to match the parent aspect ratio
        self.bg_image2_tk = ImageTk.PhotoImage(self.bg_image2)

        # label for image
        self.image_label = Label(self.pframe, image=self.bg_image2_tk)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
        self.image_label.image = self.bg_image2_tk

        # button for selecting a block
        self.A_button = Button(self.pframe, command = self.clicked_a, bg=button_color, activebackground=button_color, font=("Inter", "400", "bold"), text = "A", fg="white", borderwidth=0, cursor="hand2")
        self.A_button.place(relx=0.295, rely=0.535, relwidth=0.365, relheight=0.68, anchor="center")

        #button for selecting e block
        self.E_button = Button(self.pframe, command = self.nextpage, bg=button_color, activebackground=button_color, font=("Inter", "400", "bold"), text = "E", fg="white", borderwidth=0, cursor="hand2")
        self.E_button.place(relx=0.705, rely=0.535, relwidth=0.365, relheight=0.68, anchor="center")

        #label for the subheader
        self.click_label = Label(self.pframe, bg=background_color, font=("Inter", "28", "underline"), fg="white", text = "Click to select")
        self.click_label.place(relx = 0.5, rely = 0.12, anchor="center")

        #labels saying "block" under the buttons
        self.A_label = Label(self.pframe, bg=button_color, font=("Inter", "50", "bold"), text = "Block", fg="white")
        self.A_label.place(relx=0.295, rely=0.8, anchor="center")

        self.E_label = Label(self.pframe, bg=button_color, font=("Inter", "50", "bold"), text = "Block", fg="white")
        self.E_label.place(relx=0.705, rely=0.8, anchor="center")

        # setting an image for the back button
        self.back_button_img = Image.open("backarrow.png")  # using my canva design
        self.back_button_img_tk = ImageTk.PhotoImage(self.back_button_img)

        # Back button
        self.back_button = Button(self.pframe, image=self.back_button_img_tk, command=self.backpage, bg="#364156", activebackground="#364156",
                                    borderwidth=0, cursor="hand2")
        self.back_button.place(relx=0.05, rely=0.89 , anchor="center")
        self.back_button.image = self.back_button_img_tk

        # sets a button with an x sign, which will close the program when clicked on
        self.shutdown_image = Image.open("exithelp.png")
        self.shutdown_image_tk = ImageTk.PhotoImage(self.shutdown_image)

        self.shutdown_button = Button(self.pframe, command=self.shutdown, image=self.shutdown_image_tk,
                                      background=background_color,
                                      activebackground=background_color, borderwidth=0, cursor="hand2")
        self.shutdown_button.place(relx=0.95, rely=0.08, anchor="center")

class Selector:
    def shutdown(self):
        exit()
    def backpage(self):
        self.pframe.destroy()
        Choice(root)
    def __init__(self, parent):
        # makes variables that have the value of the parent screen width (eg if a device aspect ratio is 3:4, the variables are 3:4)
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()
        background_color = "#364156"
        button_color = "#01122e"
        block = ''
        stall = ''
        global a_or_e
        if a_or_e:
            block = 'A'
        else:
            block = 'E'
        # frame set up
        self.pframe = Frame(parent, bg=background_color)
        self.pframe.pack(fill=BOTH, expand=TRUE)

        # setting a background image (using my canva design without any widgets)
        self.bg_image3 = Image.open("select.png")  # using my canva design
        self.bg_image3 = self.bg_image3.resize((self.window_width, self.window_height),
                                                   Image.LANCZOS)  # resizes the image to match the parent aspect ratio
        self.bg_image3_tk = ImageTk.PhotoImage(self.bg_image3)

        # label for background image
        self.image_label = Label(self.pframe, image=self.bg_image3_tk)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
        self.image_label.image = self.bg_image3_tk

        # label for the main selection image in the centre of the screen
        self.selection = Label(self.pframe, bg = "black")
        self.selection.place(relx=0.5, rely=0.4275, relwidth = 0.915, relheight =0.635, anchor="center")

        # setting an image for my report button
        self.report_button = Image.open("reportbutton.png")  # using my canva design
        self.report_button_tk = ImageTk.PhotoImage(self.report_button)

        # Report button
        self.report_button = Button(self.pframe, image=self.report_button_tk, bg="#293142", activebackground="#293142",
                                    borderwidth=0, cursor="hand2")
        self.report_button.place(relx=0.8, rely=0.89 , anchor="center")
        self.report_button.image = self.report_button_tk

        # setting an image for the back button
        self.back_button_img = Image.open("backarrow.png")  # using my canva design
        self.back_button_img_tk = ImageTk.PhotoImage(self.back_button_img)

        # Back button
        self.back_button = Button(self.pframe, image=self.back_button_img_tk, command=self.backpage, bg="#293142", activebackground="#293142",
                                    borderwidth=0, cursor="hand2")
        self.back_button.place(relx=0.07, rely=0.89 , anchor="center")
        self.back_button.image = self.back_button_img_tk

        #Label to display the currently selected toilet stall
        self.current_selection = Label(self.pframe, bg="#394053", fg="white", font=("Inter", "27"), text=f"Currently Selected: {block} stall {stall}")
        self.current_selection.place(relx=0.38, rely=0.89, relwidth=0.45, relheight=0.12, anchor="center")  # make label l to fit the parent window always

        # sets a button with an x sign, which will close the program when clicked on
        self.shutdown_image = Image.open("exithelp.png")
        self.shutdown_image_tk = ImageTk.PhotoImage(self.shutdown_image)

        self.shutdown_button = Button(self.pframe, command=self.shutdown, image=self.shutdown_image_tk,
                                      background=background_color,
                                      activebackground=background_color, borderwidth=0, cursor="hand2")
        self.shutdown_button.place(relx=0.95, rely=0.06, anchor="center")

        # for a
        if a_or_e == 1:
            self.selection = Label(self.pframe)
            #skip this for now

        #for e
        else:
            self.button = Button()

class ReportDetails:
    def __init__(self, parent):
        # makes variables that have the value of the parent screen width (eg if a device aspect ratio is 3:4, the variables are 3:4)
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()
        background_color = "#364156"
        button_color = "#01122e"
        global a_or_e

        # frame set up
        self.pframe = Frame(parent, bg=background_color)
        self.pframe.pack(fill=BOTH, expand=TRUE)

        # setting a background image (using my canva design without any widgets)
        self.bg_image4 = Image.open("ReportDetails.png")  # using my canva design
        self.bg_image4 = self.bg_image4.resize((self.window_width, self.window_height),
                                               Image.LANCZOS)  # resizes the image to match the parent aspect ratio
        self.bg_image4_tk = ImageTk.PhotoImage(self.bg_image4)



root = Tk()  # create the main window
root.title("MRGS TOILETS")  # set the title of the window
root.attributes("-fullscreen", True)
program = HomePage(root)  # create an instance of HomePage and pass the root window
root.mainloop()  # start the Tkinter event loop to display the window and wait for user interaction