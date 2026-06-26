from tkinter import *  # Importing all classes from tkinter module
import customtkinter
import pywinstyles
from PIL import Image, ImageTk
import webbrowser
import time
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
        bathroom faster. Press CONTINUE to report""", font=("Inter", 22), fg="#ffffff", bg = "#4e4a59")
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
        self.body_text = Label(self.pframe, font=("Inter", 30), text="""Everyone at MRGS deserves running facilities, and you can help 
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
        global block
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
        self.A_button = Button(self.pframe, command = self.clicked_a, bg=button_color, activebackground=button_color, font=("Inter", 400, "bold"), text = "A", fg="white", borderwidth=0, cursor="hand2")
        self.A_button.place(relx=0.295, rely=0.535, relwidth=0.365, relheight=0.68, anchor="center")

        #button for selecting e block
        self.E_button = Button(self.pframe, command = self.nextpage, bg=button_color, activebackground=button_color, font=("Inter", 400, "bold"), text = "E", fg="white", borderwidth=0, cursor="hand2")
        self.E_button.place(relx=0.705, rely=0.535, relwidth=0.365, relheight=0.68, anchor="center")

        #label for the subheader
        self.click_label = Label(self.pframe, bg=background_color, font=("Inter", 28, "underline"), fg="white", text = "Click to select")
        self.click_label.place(relx = 0.5, rely = 0.12, anchor="center")

        #labels saying "block" under the buttons
        self.A_label = Label(self.pframe, bg=button_color, font=("Inter", 50, "bold"), text = "Block", fg="white")
        self.A_label.place(relx=0.295, rely=0.8, anchor="center")

        self.E_label = Label(self.pframe, bg=button_color, font=("Inter", 50, "bold"), text = "Block", fg="white")
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
                                      background=background_color, activebackground=background_color, borderwidth=0, cursor="hand2")
        self.shutdown_button.place(relx=0.95, rely=0.08, anchor="center")

class Selector:
    def shutdown(self):
        exit()

    def backpage(self):
        self.pframe.destroy()
        Choice(root)

    def nextpage(self):
        self.pframe.destroy()
        ReportDetails(root)

    def stall1(self):
        stall=1
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall2(self):
        stall = 2
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall3(self):
        stall = 3
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall4(self):
        stall = 4
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall5(self):
        stall = 5
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall6(self):
        stall = 6
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall7(self):
        stall = 7
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall8(self):
        stall = 8
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall9(self):
        stall = 9
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall10(self):
        stall = 10
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall11(self):
        stall = 11
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def stall12(self):
        stall = 12
        self.current_selection.config(text=f"Currently Selected: {block} stall {stall}")

    def changescreen1(self):
        global currentpage
        if currentpage == "Centre":
            currentpage = "Left"
            self.toiletdisplay.destroy()
            self.stall1button.destroy()
            self.stall2button.destroy()
            self.stall3button.destroy()
            self.stall4button.destroy()
            self.stall5button.destroy()


            self.eblock3 = Image.open("eblock3.jpg")  # using my canva design
            self.eblock3_tk = ImageTk.PhotoImage(self.eblock3)

            # displaying the image of the toilets
            self.toiletdisplay = Label(self.pframe, bg="#ffffff", image=self.eblock3_tk)
            self.toiletdisplay.place(relx=0.5, rely=0.43, anchor="center")
            self.toiletdisplay.image = self.eblock3_tk

            self.stall9button = Button(self.pframe, command=self.stall9, font=("Inter", 25), text="Stall 9")
            self.stall9button.place(relx=0.25, rely=0.4)

            self.stall10button = Button(self.pframe, command=self.stall10, font=("Inter", 25), text="Stall 10")
            self.stall10button.place(relx=0.45, rely=0.4)

            self.stall11button = Button(self.pframe, command=self.stall11, font=("Inter", 25), text="Stall 11")
            self.stall11button.place(relx=0.6, rely=0.4)

            self.stall12button = Button(self.pframe, command=self.stall12, font=("Inter", 25), text="Stall 12")
            self.stall12button.place(relx=0.7, rely=0.4)

        elif currentpage == "Right":
            currentpage = "Centre"
            self.eblock1 = Image.open("eblock1.jpg")  # using my canva design
            self.eblock1_tk = ImageTk.PhotoImage(self.eblock1)

            # displaying the image of the toilets
            self.toiletdisplay = Label(self.pframe, bg="#ffffff", image=self.eblock1_tk)
            self.toiletdisplay.place(relx=0.5, rely=0.43, anchor="center")
            self.toiletdisplay.image = self.eblock1_tk

            self.stall1button = Button(self.pframe, command=self.stall1, font=("Inter", 25), text ="Stall 1")
            self.stall1button.place(relx=0.25,rely=0.4)

            self.stall2button = Button(self.pframe, command=self.stall2, font=("Inter", 25), text="Stall 2")
            self.stall2button.place(relx=0.45, rely=0.4)

            self.stall3button = Button(self.pframe, command=self.stall3, font=("Inter", 25), text="Stall 3")
            self.stall3button.place(relx=0.6, rely=0.4)

            self.stall4button = Button(self.pframe, command=self.stall4, font=("Inter", 25), text="Stall 4")
            self.stall4button.place(relx=0.67, rely=0.4)

            self.stall5button = Button(self.pframe, command=self.stall5, font=("Inter", 25), text="Stall 5")
            self.stall5button.place(relx=0.74, rely=0.4)

            # setting an image for the left button
            self.left_button_img = Image.open("left.png")  # using my canva design
            self.left_button_img_tk = ImageTk.PhotoImage(self.left_button_img)

            # left button
            self.left_button = Button(self.pframe, image=self.left_button_img_tk, command=self.changescreen1, bg="black",
                                      activebackground="#293142",
                                      borderwidth=0, cursor="hand2")
            self.left_button.place(relx=0.08
                                   , rely=0.45, anchor="center")
            self.left_button.image = self.left_button_img_tk

            # setting an image for the right button
            self.right_button_img = Image.open("right.png")  # using my canva design
            self.right_button_img_tk = ImageTk.PhotoImage(self.right_button_img)

            # left button
            self.right_button = Button(self.pframe, image=self.right_button_img_tk, command=self.changescreen2, bg="black",
                                      activebackground="#293142",
                                      borderwidth=0, cursor="hand2")
            self.right_button.place(relx=0.92, rely=0.45, anchor="center")
            self.right_button.image = self.right_button_img_tk
    def changescreen2(self):
        global currentpage
        if currentpage == "Centre":
            currentpage = "Right"
            self.toiletdisplay.destroy()
            self.stall1button.destroy()
            self.stall2button.destroy()
            self.stall3button.destroy()
            self.stall4button.destroy()
            self.stall5button.destroy()

            self.eblock2 = Image.open("eblock2.jpg")  # using my canva design
            self.eblock2_tk = ImageTk.PhotoImage(self.eblock2)

            # displaying the image of the toilets
            self.toiletdisplay = Label(self.pframe, bg="#ffffff", image=self.eblock2_tk)
            self.toiletdisplay.place(relx=0.5, rely=0.43, anchor="center")
            self.toiletdisplay.image = self.eblock2_tk

            self.stall5button = Button(self.pframe, command=self.stall5, font=("Inter", 25), text="Stall 5")
            self.stall5button.place(relx=0.2, rely=0.4)

            self.stall6button = Button(self.pframe, command=self.stall6, font=("Inter", 25), text="Stall 6")
            self.stall6button.place(relx=0.3, rely=0.4)

            self.stall7button = Button(self.pframe, command=self.stall7, font=("Inter", 25), text="Stall 7")
            self.stall7button.place(relx=0.43, rely=0.4)

            self.stall8button = Button(self.pframe, command=self.stall12, font=("Inter", 25), text="Stall 8")
            self.stall8button.place(relx=0.6, rely=0.4)

        elif currentpage == "Left":
            currentpage = "Centre"
            self.eblock1 = Image.open("eblock1.jpg")  # using my canva design
            self.eblock1_tk = ImageTk.PhotoImage(self.eblock1)

            # displaying the image of the toilets
            self.toiletdisplay = Label(self.pframe, bg="#ffffff", image=self.eblock1_tk)
            self.toiletdisplay.place(relx=0.5, rely=0.43, anchor="center")
            self.toiletdisplay.image = self.eblock1_tk

            self.stall1button = Button(self.pframe, command=self.stall1, font=("Inter", 25), text ="Stall 1")
            self.stall1button.place(relx=0.25,rely=0.4)

            self.stall2button = Button(self.pframe, command=self.stall2, font=("Inter", 25), text="Stall 2")
            self.stall2button.place(relx=0.45, rely=0.4)

            self.stall3button = Button(self.pframe, command=self.stall3, font=("Inter", 25), text="Stall 3")
            self.stall3button.place(relx=0.6, rely=0.4)

            self.stall4button = Button(self.pframe, command=self.stall4, font=("Inter", 25), text="Stall 4")
            self.stall4button.place(relx=0.67, rely=0.4)

            self.stall5button = Button(self.pframe, command=self.stall5, font=("Inter", 25), text="Stall 5")
            self.stall5button.place(relx=0.74, rely=0.4)

            # setting an image for the left button
            self.left_button_img = Image.open("left.png")  # using my canva design
            self.left_button_img_tk = ImageTk.PhotoImage(self.left_button_img)

            # left button
            self.left_button = Button(self.pframe, image=self.left_button_img_tk, command=self.changescreen1, bg="black",
                                      activebackground="#293142",
                                      borderwidth=0, cursor="hand2")
            self.left_button.place(relx=0.08
                                   , rely=0.45, anchor="center")
            self.left_button.image = self.left_button_img_tk

            # setting an image for the right button
            self.right_button_img = Image.open("right.png")  # using my canva design
            self.right_button_img_tk = ImageTk.PhotoImage(self.right_button_img)

            # left button
            self.right_button = Button(self.pframe, image=self.right_button_img_tk, command=self.changescreen2, bg="black",
                                      activebackground="#293142",
                                      borderwidth=0, cursor="hand2")
            self.right_button.place(relx=0.92, rely=0.45, anchor="center")
            self.right_button.image = self.right_button_img_tk

    def __init__(self, parent):
        # makes variables that have the value of the parent screen width (eg if a device aspect ratio is 3:4, the variables are 3:4)
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()
        background_color = "#364156"
        button_color = "#01122e"
        global stall
        global block
        global currentpage
        block = ''
        global a_or_e
        if a_or_e:
            block = 'A'
        else:
            block = 'E'
        stall = 1
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
                                    borderwidth=0, cursor="hand2", command=self.nextpage)
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
        self.current_selection = Label(self.pframe, bg="#394053", fg="white", font=("Inter", 27), text=f"Currently Selected: {block} stall {stall}")
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
            #displaying the image of the toilets
            self.ablock = Image.open("ablock.jpg")  # using my canva design
            self.ablock_tk = ImageTk.PhotoImage(self.ablock)

            self.toiletdisplay = Label(self.pframe, bg="#ffffff", image=self.ablock_tk)
            self.toiletdisplay.place(relx=0.5, rely=0.43, anchor="center")
            self.toiletdisplay.image = self.ablock_tk

            self.stall1button = Button(self.pframe, command=self.stall1, font=("Inter", 25), text ="Stall 1")
            self.stall1button.place(relx=0.3,rely=0.4)

            self.stall2button = Button(self.pframe, command=self.stall2, font=("Inter", 25), text="Stall 2")
            self.stall2button.place(relx=0.4, rely=0.45)

            self.stall3button = Button(self.pframe, command=self.stall3, font=("Inter", 25), text="Stall 3")
            self.stall3button.place(relx=0.5, rely=0.5)

            self.stall4button = Button(self.pframe, command=self.stall4, font=("Inter", 25), text="Stall 4")
            self.stall4button.place(relx=0.65, rely=0.5)


        #for e
        else:
            currentpage = "Centre"
            self.eblock1 = Image.open("eblock1.jpg")  # using my canva design
            self.eblock1_tk = ImageTk.PhotoImage(self.eblock1)

            # displaying the image of the toilets
            self.toiletdisplay = Label(self.pframe, bg="#ffffff", image=self.eblock1_tk)
            self.toiletdisplay.place(relx=0.5, rely=0.43, anchor="center")
            self.toiletdisplay.image = self.eblock1_tk

            self.stall1button = Button(self.pframe, command=self.stall1, font=("Inter", 25), text ="Stall 1")
            self.stall1button.place(relx=0.25,rely=0.4)

            self.stall2button = Button(self.pframe, command=self.stall2, font=("Inter", 25), text="Stall 2")
            self.stall2button.place(relx=0.45, rely=0.4)

            self.stall3button = Button(self.pframe, command=self.stall3, font=("Inter", 25), text="Stall 3")
            self.stall3button.place(relx=0.6, rely=0.4)

            self.stall4button = Button(self.pframe, command=self.stall4, font=("Inter", 25), text="Stall 4")
            self.stall4button.place(relx=0.67, rely=0.4)

            self.stall5button = Button(self.pframe, command=self.stall5, font=("Inter", 25), text="Stall 5")
            self.stall5button.place(relx=0.74, rely=0.4)

            # setting an image for the left button
            self.left_button_img = Image.open("left.png")  # using my canva design
            self.left_button_img_tk = ImageTk.PhotoImage(self.left_button_img)

            # left button
            self.left_button = Button(self.pframe, image=self.left_button_img_tk, command=self.changescreen1, bg="black",
                                      activebackground="#293142",
                                      borderwidth=0, cursor="hand2")
            self.left_button.place(relx=0.08
                                   , rely=0.45, anchor="center")
            self.left_button.image = self.left_button_img_tk

            # setting an image for the right button
            self.right_button_img = Image.open("right.png")  # using my canva design
            self.right_button_img_tk = ImageTk.PhotoImage(self.right_button_img)

            # left button
            self.right_button = Button(self.pframe, image=self.right_button_img_tk, command=self.changescreen2, bg="black",
                                      activebackground="#293142",
                                      borderwidth=0, cursor="hand2")
            self.right_button.place(relx=0.92, rely=0.45, anchor="center")
            self.right_button.image = self.right_button_img_tk



class ReportDetails:
    def openurl(self):
        webbrowser.open_new("https://www.mrgs.school.nz/")
    def destroy_conf(self):
        self.confirmation_label.destroy()
        self.yes_button.destroy()
        self.cancel_button.destroy()
    def endprogram(self):
        self.endlabel(self.pframe, )
        exit()
    def confirmation(self):
        #sets a label which looks like a popup, which will contain a confirmation message "Are you sure?"
        self.confirmation_image = Image.open("confirmation.png")  # background image for the help button
        self.confirmation_image_tk = ImageTk.PhotoImage(self.confirmation_image)
        self.confirmation_label = Label(self.pframe, image=self.confirmation_image_tk, bg = "#3d3739")
        self.confirmation_label.place(relx=0.5, rely=0.5, anchor="center")
        pywinstyles.set_opacity(self.confirmation_label, color="#3d3739")

        #sets a cancel button, which will close the popup when clicked on
        self.cancel_image = Image.open("cancel.png")  # using my canva design
        self.cancel_image_tk = ImageTk.PhotoImage(self.cancel_image)

        self.cancel_button = Button(self.pframe, image=self.cancel_image_tk, command=self.destroy_conf, borderwidth=0, cursor="hand2", bg = "#4e4a59", activebackground="#4e4a59")
        self.cancel_button.place(relx=0.6, rely=0.59, anchor="center")


        #sets a "yes" button, which will close the popup when clicked on
        self.yes_image = Image.open("yes.png")  # using my canva design
        self.yes_image_tk = ImageTk.PhotoImage(self.yes_image)

        self.yes_button = Button(self.pframe, image=self.yes_image_tk, command=self.shutdown, borderwidth=0, cursor="hand2", bg = "#4e4a59", activebackground="#4e4a59")
        self.yes_button.place(relx=0.4, rely=0.59, anchor="center")


    def clickedcheck1(self):
        self.checkb2.deselect()
        self.checkb3.deselect()
        self.checkb4.deselect()

    def clickedcheck2(self):
        self.checkb1.deselect()
        self.checkb3.deselect()
        self.checkb4.deselect()

    def clickedcheck3(self):
        self.checkb1.deselect()
        self.checkb2.deselect()
        self.checkb4.deselect()

    def clickedcheck4(self):
        self.checkb1.deselect()
        self.checkb2.deselect()
        self.checkb3.deselect()

    def backpage(self):
        self.pframe.destroy()
        Selector(root)
    def shutdown(self):
        exit()
    def nextpage(self):
        self.pframe.destroy()
        ReportDetails(root)
    def collection(self):
        usertext = self.submittext.get()
    def __init__(self, parent):
        # makes variables that have the value of the parent screen width (eg if a device aspect ratio is 3:4, the variables are 3:4)
        self.window_width = parent.winfo_screenwidth()
        self.window_height = parent.winfo_screenheight()
        background_color = "#364156"
        button_color = "#01122e"
        global a_or_e
        text_colour = "#394053"

        # frame set up
        self.pframe = Frame(parent, bg=background_color)
        self.pframe.pack(fill=BOTH, expand=TRUE)

        # setting a background image (using my canva design without any widgets)
        self.bg_image4 = Image.open("ReportDetails.png")  # using my canva design
        self.bg_image4 = self.bg_image4.resize((self.window_width, self.window_height),
                                               Image.LANCZOS)  # resizes the image to match the parent aspect ratio
        self.bg_image4_tk = ImageTk.PhotoImage(self.bg_image4)

        # label for background image
        self.image_label = Label(self.pframe, image=self.bg_image4_tk)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
        self.image_label.image = self.bg_image4_tk

        #4 labels for the text
        self.label1 = Label(self.pframe, bg = "#cdcdcd", fg=text_colour, font =("Inter",25,"bold"), text="Graffiti - Writing on the walls")
        self.label1.place(relx= 0.375, rely=0.314, relwidth=0.55, relheight=0.12, anchor="center")

        self.label2 = Label(self.pframe, bg = "#f7f8f8", fg="black", font =("Inter",25,"bold"), text="Damage to property - damage to the door, toilets")
        self.label2.place(relx= 0.375, rely=0.455, relwidth=0.55, relheight=0.12, anchor="center")

        self.label3 = Label(self.pframe, bg = "#cdcdcd", fg=text_colour, font =("Inter",25,"bold"), text="Waste - Dirty floors ")
        self.label3.place(relx= 0.375, rely=0.596, relwidth=0.55, relheight=0.12, anchor="center")

        self.label4 = Label(self.pframe, bg = "#f7f8f8", fg="black", font =("Inter",25,"bold"), text="Clogging - Clogged toilet, sinks")
        self.label4.place(relx= 0.375, rely=0.737, relwidth=0.55, relheight=0.12, anchor="center")

        #label for button
        self.support_image = Image.open("support.png")
        self.support_image_tk = ImageTk.PhotoImage(self.support_image)

        #Support us button
        self.support_button = Button(self.pframe, image=self.support_image_tk,
                                      background=background_color, command=self.openurl,
                                      activebackground=background_color, borderwidth=0, cursor="hand2")
        self.support_button.place(relx=0.15, rely=0.89, anchor="center")
        self.support_button.image = self.support_image_tk


        # setting an image for the back button
        self.back_button_img = Image.open("backarrow.png")  # using my canva design
        self.back_button_img_tk = ImageTk.PhotoImage(self.back_button_img)

        # Back button
        self.back_button = Button(self.pframe, image=self.back_button_img_tk, command=self.backpage, bg=background_color, activebackground=background_color,
                                    borderwidth=0, cursor="hand2")
        self.back_button.place(relx=0.05, rely=0.89, anchor="center")
        self.back_button.image = self.back_button_img_tk

        # sets a button with an x sign, which will close the program when clicked on
        self.shutdown_image = Image.open("exithelp.png")
        self.shutdown_image_tk = ImageTk.PhotoImage(self.shutdown_image)

        self.shutdown_button = Button(self.pframe, command=self.shutdown, image=self.shutdown_image_tk,
                                      background=background_color,
                                      activebackground=background_color, borderwidth=0, cursor="hand2")
        self.shutdown_button.place(relx=0.95, rely=0.06, anchor="center")
        self.shutdown_button.image = self.shutdown_image_tk

        #sendbutton
        self.send_image = Image.open("sendbutton.png")
        self.send_image_tk = ImageTk.PhotoImage(self.send_image)

        self.send_button = Button(self.pframe, command=self.confirmation, image=self.send_image_tk,
                                      background=background_color,
                                      activebackground=background_color, borderwidth=0, cursor="hand2")
        self.send_button.place(relx=0.5, rely=0.89, anchor="center")
        self.send_button.image = self.send_image_tk
        #checkbutton
        global check1
        global check2
        global check3
        global check4
        global checkb1
        global checkb2
        global checkb3
        global checkb4

        check1 = IntVar()
        check2 = IntVar()
        check3 = IntVar()
        check4 = IntVar()

        self.checkb1 = customtkinter.CTkCheckBox(self.pframe,
                variable = check1, text="", onvalue = 1, command=self.clickedcheck1, offvalue=0, checkbox_width=50, checkbox_height=50,
                                            width=50, height=50, bg_color="#cdcdcd", fg_color="green")
        self.checkb1.place(relx=0.62, rely=0.315, anchor="center")

        self.checkb2 = customtkinter.CTkCheckBox(self.pframe,
                variable = check2, text="", onvalue = 1, command=self.clickedcheck2, offvalue=0, checkbox_width=50, checkbox_height=50,
                                            width=50, height=50, bg_color="#f7f8f8", fg_color="green")
        self.checkb2.place(relx=0.62, rely=0.455, anchor="center")

        self.checkb3 = customtkinter.CTkCheckBox(self.pframe,
                variable = check3, text="", onvalue = 1, command=self.clickedcheck3, offvalue=0, checkbox_width=50, checkbox_height=50,
                                            width=50, height=50, bg_color="#cdcdcd", fg_color="green")
        self.checkb3.place(relx=0.62, rely=0.595, anchor="center")

        self.checkb4 = customtkinter.CTkCheckBox(self.pframe,
                variable = check4, text="", onvalue = 1, command=self.clickedcheck4, offvalue=0, checkbox_width=50, checkbox_height=50,
                                            width=50, height=50, bg_color="#f7f8f8", fg_color="green")
        self.checkb4.place(relx=0.62, rely=0.735, anchor="center")

        #textbox for users to describe damage
        self.usertext = ""
        self.submittext = customtkinter.CTkTextbox(self.pframe, fg_color="#f7f8f8", font=("Inter", 30), wrap = "word")
        self.submittext.place(relx = 0.81, rely = 0.525,
                              relheight=0.535, relwidth=0.26, anchor="center")
        self.explaintext = Label(self.pframe, bg = "#a7a9ab", fg = "#f7f8f8", font = ("Inter",12), text = "describe the damage here")
        self.explaintext.place(relx=0.6805,rely=0.77)


root = Tk()  # create the main window
root.title("MRGS TOILETS")  # set the title of the window
root.attributes("-fullscreen", True)
program = HomePage(root)  # create an instance of HomePage and pass the root window
root.mainloop()  # start the Tkinter event loop to display the window and wait for user interaction