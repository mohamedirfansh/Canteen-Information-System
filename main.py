# -----------Import modules for usage--------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import time
from datetime import datetime
from data import *
from tkcalendar import Calendar, DateEntry
from tkinter.simpledialog import askstring
from random import randint
from functions import *
import pygame

# -----------Global variables----------------------------------------------------------------------------------------------------------------------------------------
LARGE_FONT = ("Verdana", 12)  # Font that we use often in our program for displaying
day = 0
time = 0
date = 0
database_choice = ''
userInputCondition = False  # To check if time and date is set by user or using current time and date
HOURS = [i for i in range(24)]
MINUTES = [i for i in range(60)]


# ---------For the multiple frames-----------------------------------------------------------------------------------------------------------------------------------
class window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for page in (StartPage, ViewStallPage, AllStallsPage, IndividualStallPage, InstructionPage):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


# ---------The first frame that shows up when you first run the program----------------------------------------------------------------------------------------------
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.musicIsPlaying = True

        # Background Image for the StartPage
        self.background_img = ImageTk.PhotoImage(file='assets/background.png')
        self.background = Label(self, image=self.background_img)
        self.background.place(relwidth=1, relheight=1)

        # -------Label to show current time--------
        self.label_time = Label(self, justify='center')
        self.label_time.place(relx=0.373, rely=0.02)
        self.clock()

        # --------Button to view stalls--------
        self.logo_viewstalls = ImageTk.PhotoImage(file="assets/viewstalls.png")
        self.button_viewstalls = Button(self, image=self.logo_viewstalls, relief='flat', borderwidth=0,\
                                        compound="center", highlightthickness=0,\
                                        command=lambda: controller.show_frame(ViewStallPage))
        self.button_viewstalls.place(x=503, y=357)

        # -------Button to get user input for date and time--------
        self.logo_datetime = ImageTk.PhotoImage(file="assets/datetime.png")
        button_setDateAndTime = Button(self, image=self.logo_datetime, relief='flat', borderwidth=0, compound="center",\
                                       highlightthickness=0, command=lambda: self.calender(controller))
        button_setDateAndTime.place(relx=0.394, rely=0.686)

        # --------Button to see how to use--------
        self.logo_howtouse = ImageTk.PhotoImage(file="assets/howtouse.png")
        self.button_howtouse = Button(self, image=self.logo_howtouse, relief='flat', borderwidth=0, compound="center",\
                                      highlightthickness=0, command=lambda: controller.show_frame(InstructionPage))
        self.button_howtouse.place(x=503, y=559)

        # --------Button pause or play the music--------
        self.button_playMusic = Button(self, text='Pause Music', relief='flat', fg='white', bg='#00b150',\
                                       font='Helvetica 12', height=2, width=10, command=self.music)
        self.button_playMusic.place(relx=0.90, rely=0.01)

    
    # --------Function to pause or resume playing the background music. Funtion done by: NEO RUI XUAN BERLYNN-----------
    def music(self):
        self.musicIsPlaying = not self.musicIsPlaying
        if self.musicIsPlaying:
            self.button_playMusic.configure(text="Pause Music")
            pygame.mixer.music.unpause()
            self.musicIsPlaying = True
        else:
            self.button_playMusic.configure(text="Play Music")
            pygame.mixer.music.pause()
            self.musicIsPlaying = False

    # --------Clock function to display current time. Done by: MUHAMMAD IRFAN----------------
    def clock(self):
        self.now = datetime.now()
        self.time_str = self.now.strftime("%d/%m/%Y %H:%M:%S")  # .strftime('%I:%M:%S',time.localtime())
        if self.time_str != '':
            self.label_time.config(text=self.time_str, font='helvetica 26', fg='white', bg='#383838')
        self.after(100, self.clock)

    # --------Function to display calendar and time for user's input. Functions done by: MUHUAMMAD ZUFIQQAR----------------
    def calender(self, controller):
        global database_choice, day, time, date

        # --------Actions to be taken user presses the ok button after input.----------------
        def updateUserSelection(toplevel_calendar, controller, drop_sel, hour, minute):
            global database_choice, day, time, date, userInputCondition

            # ----------Update Global Variables based on user's inputs-------------
            time = (100 * int(hour)) + int(minute)
            date = drop_sel
            day = datetime.strptime(str(drop_sel), '%Y-%m-%d').weekday()

            # ----------Close the calendar window and update userInputCondition to True-------------
            toplevel_calendar.destroy()
            userInputCondition = True

        # -------Create a TopLevel to be used for displaying calendar-------------
        toplevel_calendar = Toplevel(self, bg='black')
        toplevel_calendar.grab_set()

        # -------Create an Actual Calendar from tkcalendar module for the user to set date and time-------------
        calendar = Calendar(toplevel_calendar, font="Arial 14", selectmode='day', locale='en_US',\
                            mindate=datetime.now(), background='black', foreground='white', \
                            selectbackground='green', bordercolor='blue', normalforeground='blue',\
                            weekendforeground='blue', headersbackground='blue', headersforeground='white', \
                            cursor="hand1", year=int(date.strftime('%Y')), month=int(date.strftime('%m')),\
                            day=int(date.strftime('%d')))
        calendar.pack(fill="both", expand=True)

        # -------Create a Canvas inside TopLevel to be used later-------------
        canvas = Canvas(toplevel_calendar)
        canvas.pack(side=BOTTOM)

        # -------Label for hours-------------
        hour_label = Label(canvas, text="Time", font=LARGE_FONT, fg='white', bg='#00a99e')
        hour_label.pack(side=LEFT)

        # -------Populate values 0-23 in a comboBox-------------
        hour = ttk.Combobox(canvas, state='readonly')
        hour['values'] = HOURS
        hour.config(width=5, font=('Helvetica', 12))
        hour.pack(side=LEFT)
        hour.current(time // 100)

        # -------Label for minutes-------------
        minute_label = Label(canvas, text=":", font=LARGE_FONT, fg='white', bg='#00a99e')
        minute_label.pack(side=LEFT)

        # -------Populate values 0-59 in a comboBox-------------
        minute = ttk.Combobox(canvas, state='readonly')
        minute['values'] = MINUTES
        minute.config(width=5, font=('Helvetica', 12))
        minute.pack(side=LEFT)
        minute.current(time % 100)

        # -------Button for user to press after setting the date and time-------------
        user_button = Button(canvas, width=10, height=1, text="OK", font='Helvetica 10', relief='flat', fg='white',\
                             bg='#00b150', \
                             command=lambda: updateUserSelection(toplevel_calendar, controller,\
                                                                 calendar.selection_get(), hour.get(), minute.get()))
        user_button.pack(side='bottom')


# ---------Second frame in-line after start page---------------------------------------------------------------------------------------------------------------------
class ViewStallPage(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)

        # Background Image for the ViewStallPage
        self.background_img = ImageTk.PhotoImage(file='assets/stallspage.png')
        self.background = Label(self, image=self.background_img)
        self.background.place(relwidth=1, relheight=1)

        # ----------Mcdonalds Button---------------
        self.logo_mcdonalds = ImageTk.PhotoImage(file="assets/mcdonald.png")
        self.button_mcdonlads = Button(self, image=self.logo_mcdonalds, relief='flat', borderwidth=0, compound="center",\
                                       highlightthickness=0,\
                                       command=lambda: self.stallSelection(controller, "Mac Donald"))
        self.button_mcdonlads.place(x=172, y=148)
        # -----------------------------------------
        # ---------------KFC Button----------------
        self.logo_kfc = ImageTk.PhotoImage(file="assets/kfc.png")
        self.button_kfc = Button(self, image=self.logo_kfc, relief='flat', borderwidth=0, compound="center",\
                                 highlightthickness=0, command=lambda: self.stallSelection(controller, "KFC"))
        self.button_kfc.place(x=531, y=148)
        # -----------------------------------------
        # ---------------Malay BBQ Button----------
        self.logo_malaybbq = ImageTk.PhotoImage(file="assets/malaybbq.png")
        self.button_malaybbq = Button(self, image=self.logo_malaybbq, relief='flat', borderwidth=0, compound="center",\
                                      highlightthickness=0,\
                                      command=lambda: self.stallSelection(controller, "Malay Stall"))
        self.button_malaybbq.place(x=888, y=150)
        # -----------------------------------------
        # ---------------Yong Tau Foo Button-------
        self.logo_ytfoo = ImageTk.PhotoImage(file="assets/ytfoo.png")
        self.button_ytfoo = Button(self, image=self.logo_ytfoo, relief='flat', borderwidth=0, compound="center",\
                                   highlightthickness=0,\
                                   command=lambda: self.stallSelection(controller, "Yong Tau Foo Stall"))
        self.button_ytfoo.place(x=174, y=402)
        # -----------------------------------------
        # ---------------Drinks Button-------------
        self.logo_drinks = ImageTk.PhotoImage(file="assets/drinks.png")
        self.button_drinks = Button(self, image=self.logo_drinks, relief='flat', borderwidth=0, compound="center",\
                                    highlightthickness=0,\
                                    command=lambda: self.stallSelection(controller, "Beverages Stall"))
        self.button_drinks.place(x=532, y=400)
        # -----------------------------------------
        # ---------------Home Button---------------
        self.home_button = Button(self, text='Home', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                  height=2, width=10, command=lambda: controller.show_frame(StartPage))
        self.home_button.place(x=10, y=10)
        # -----------------------------------------
        # ---------------All Stalls Button---------------
        self.home_button = Button(self, text='All Stalls', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                  height=2, width=10, command=lambda: controller.show_frame(AllStallsPage))
        self.home_button.place(x=130, y=10)
        # -----------------------------------------
        # ---------------Random Stall Button------------- 
        self.randomStall = ImageTk.PhotoImage(file="assets/randomstall.png")
        self.button_drinks = Button(self, image=self.randomStall, relief='flat', borderwidth=0,\
                                    compound="center", highlightthickness=0,\
                                    command=lambda: self.buttonRandomStall(controller))
        self.button_drinks.place(x=888, y=400)
        # -----------------------------------------

    # ----------Function to Display A Random Stall-------------
    def buttonRandomStall(self, controller):
        # ----------Get all the stall's names from a function-------------
        howManyStall = getAllStallNames()

        # ----------Generate a random stall's name and pass it as argument-------------
        stall = howManyStall[randint(0, len(howManyStall) - 1)]
        self.stallSelection(controller, stall)

    # ----------Function to Display A Random Stall-------------
    def stallSelection(self, controller, stall):
        global database_choice, userInputCondition, date, time, day

        # ----------Update database_choice variable based on user's/random stall selection-------------
        database_choice = stall

        # ----------If user didn't set date and time, update them before retrieving the stall's info for more accuracy-------------
        if (not userInputCondition):
            date, time, day = updateTime()

        # ----------Execute the execute() function first before jumping to IndividualStallPage Frame-------------
        page = self.controller.get_page(IndividualStallPage)
        page.execute()
        controller.show_frame(IndividualStallPage)


# ---------Frame that shows all the stall menus available------------------------------------------------------------------------------------------------------------
class AllStallsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(bg="black")

        # ---------Background Image for the AllStallsPage-------------------------
        background_image = ImageTk.PhotoImage(file='assets/cool1.jpg')
        image_label = Label(self, image=background_image)
        image_label.place(x=0, y=0)
        image_label.image = background_image

        # ---------------Return to ViewStallPage Button---------------
        self.back_button = Button(self, text='View Stalls', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                  height=2, width=10, command=lambda: controller.show_frame(ViewStallPage))
        self.back_button.place(x=10, y=10)

        # ---------------Create a empty canvas for future usage---------------
        self.canvas = Canvas(self, width=600, height=700, background='black')
        self.canvas.pack(side=LEFT, expand=True)

        # ---------------Scrollbar for the Canvas---------------
        self.yscrollbar = Scrollbar(self)
        self.yscrollbar.pack(side=LEFT, fill=Y)

        # ---------------Populate a empty frame inside the Canvas for future usage---------------
        self.frame = Frame(self.canvas, bg='black')
        self.frame.pack(fill=Y, expand=False)

        # ---------------Configuration of the Scrollbar for the Canvas---------------
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)
        self.canvas.bind('<Configure>', self.on_configure)
        self.yscrollbar.configure(command=self.canvas.yview)

        # ---------------Configuration of the Scrollbar for the Canvas---------------
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # ----------Get all the stall's names from a function-------------
        howManyStall = getAllStallNames()

        # ----------Dynamically create the neccessary widgets for each stall each time it loops-------------
        for stall in howManyStall:
            # ----------Title for each stall-------------
            disp_title = Label(self.frame, text="Click Icon to view " + stall, font=LARGE_FONT, fg='white', bg='black')
            disp_title.pack(expand=1)

            # ----------Button for each stall with picture. Upon pressing, it will display IndividualStallPage with the selected stall-------------
            stall_image = ImageTk.PhotoImage(file=outlet[stall][0])
            image_label = Button(self.frame, image=stall_image, justify=LEFT,\
                                 command=lambda z=stall: self.goToPageTwo(controller, z))
            image_label.pack(expand=1)
            image_label.image = stall_image

            # ----------Label for displaying stall's menu-------------
            disp_menu = Label(self.frame, font=LARGE_FONT, fg='white', bg='black', justify=LEFT, highlightcolor='white')
            disp_menu.pack(expand=1)

            # ----------Frame to show -------------
            bottomframe = Label(self.frame, font=LARGE_FONT, fg='white', bg='black')
            bottomframe.config(text="____________________________________________________________\n")
            bottomframe.pack()

            # ----------Label for displaying stall's menu-------------
            menu_string = get_allMenu(stall, day)
            disp_menu.configure(text=menu_string)

    # ---------------Update the dimensions of the canvas when items are added or deleted---------------
    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    # ----------Function that update the user's stall choice and timing if needed before jumping to IndividualStallPage Frame-------------
    def goToPageTwo(self, controller, stall):
        global database_choice, userInputCondition

        # ---------------Update the database_choice global variable from user's selection---------------
        database_choice = stall

        # ----------If user didn't set date and time, update them before retrieving the stall's info for more accuracy-------------
        if (not userInputCondition):
            date, time, day

        # ----------Execute the execute() function first before jumping to IndividualStallPage Frame-------------
        page = controller.get_page(IndividualStallPage)
        page.execute()
        controller.show_frame(IndividualStallPage)


# ---------Frame that shows individual stall menu and info based on user's input or random stall---------------------------------------------------------------------
class IndividualStallPage(Frame):
    def __init__(self, parent, controller):
        global database_choice
        Frame.__init__(self, parent)

        # ---------Background Image for the IndividualStallPage-------------------------
        self.backgroundImageLbl = Label(self)
        self.backgroundImageLbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ---------------Return to ViewStallPage Button---------------
        back_button = Button(self, text='View Stalls', relief='flat', fg='white', bg='#00b150', font='Helvetica 12', height=2,\
                             width=9, command=lambda: controller.show_frame(ViewStallPage))
        back_button.place(x=10, y=10)

        # ---------------Label to show the address of the selected stall in NTU---------------
        self.address = Label(self, font=LARGE_FONT, justify=LEFT, fg='white', bg='black')
        self.address.place(relx=0.1, rely=0.85)

        # ---------------Label to show the menu of the selected stall---------------
        self.menu = Label(self, justify=LEFT, fg='white', bg='black', font=("Helvetica", 20))
        self.menu.place(relx=0.55, rely=0.35)

        # -------Button to get user input for date and time------------------
        self.logo_datetime = ImageTk.PhotoImage(file="assets/datetime.png")
        button_setDateAndTime = Button(self, text='SET DATE & TIME', relief='flat', fg='white', bg='#00b150',\
                                       font='Helvetica 12', height=2, width=18, borderwidth=0, compound="center", \
                                       highlightthickness=0, command=lambda: self.calender(controller))
        button_setDateAndTime.place(relx=0.96, rely=0.87, anchor="ne")

        # -------Button to display the operating hours of the selected stalls------------------
        disp_OP_Hours = Button(self, text="Operating Hours", relief='flat', fg='white', bg='#00b150',\
                               font='Helvetica 12', height=2, width=14, command=self.print_OP_Hours)
        disp_OP_Hours.place(relx=0.2, rely=0.016, anchor="ne")

        # -------Button to display the Estimated Queue Time of the selected stalls------------------
        disp_queue = Button(self, text="Estimated Queue Time", relief='flat', fg='white', bg='#00b150',\
                            font='Helvetica 12', height=2, width=19, command=self.print_queue)
        disp_queue.place(relx=0.352, rely=0.016, anchor="ne")

        # -------Button to reset/update the time, day, date to current values------------------
        self.reset_time = Button(self, text='RESET TIME', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                 height=2, width=14, borderwidth=0, compound="center", \
                                 highlightthickness=0, command = self.resetTime)
        self.reset_time.place(relx=0.82, rely=0.87, anchor="ne")

        # -------Button to view the reviews of the stall------------------
        self.review_button = Button(self, text='REVIEWS', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                    height=2, width=13, borderwidth=0, compound="center", \
                                    highlightthickness=0, command=self.stallReviews)
        self.review_button.place(relx=0.71, rely=0.87, anchor="ne")

    # -------Store the review in other own stall's file that user has entered. Function done by: NEO RUI XUAN BERLYNN------------------
    def postReviews(self, database, frameReview, userReview):
        # -------Append the new review to existing reviews of the stall------------------
        with open(database['Review'], 'a+') as file:
            file.write('\n» ' + userReview)

        # -------Destroy the review frame and display it again with updated reviews------------------
        frameReview.destroy()
        self.stallReviews()

    # -------Function that display the reviews of the stall and user can post review too. Function done by: NEO RUI XUAN BERLYNN------------------
    def stallReviews(self):
        global database_choice, day, time

        # -------Create a TopLevel for displaying reviews of a stall-------------
        toplevel_review = Toplevel(self, bg='black')
        toplevel_review.title("Reviews")
        toplevel_review.wm_geometry("400x400")
        toplevel_review.grab_set()

        # ---------------Label to show reviews of the selected stall---------------
        review = Label(toplevel_review, font=LARGE_FONT, fg='white', bg='black', justify='left')
        review.pack()

        # -------Create a Canvas inside the Toplevel-------------
        canvas = Canvas(toplevel_review)
        canvas.pack(side=BOTTOM)

        # -------Button to post the user's new input review of the stall------------------
        postReviewButton = Button(canvas, text="Post", font=LARGE_FONT, fg='white', bg='#00b150',\
                                  command=lambda: self.postReviews(database, toplevel_review, userReviewEntry.get()))
        postReviewButton.pack(side=RIGHT)

        # -------For user to type review in it------------------
        userReviewEntry = Entry(canvas, font=LARGE_FONT, fg='black', bg='white', width=10)
        userReviewEntry.pack(side=RIGHT)
        userReviewEntry.pack(ipadx=12, ipady=8)

        # -------Get the correct reviews of the selected stall for display------------------
        database = choosing_database(database_choice, time, day)
        with open(database['Review'], 'a+') as file:
            file.seek(0)
            review.config(text=file.read())

    # -------Update the time, day, date to current and display the stall's menu and info based on that conditions. Function done by: MUHAMMAD ZUFIQQAR------------------
    def resetTime(self):
        # -------Global variable userInputCondition is used to check if the timing, day, date is based on datetime.now() or user's input------------------
        global userInputCondition, date, time, day

        # -------Reset userInputCondition variable and update the time, day, date to current and displaying the correct menu accordingly by executing the execute() function--------
        userInputCondition = False
        date, time, day = updateTime()
        self.execute()

    # -------Function for displaying estimated queue time for the stall. Functions done by: MUHAMMAD ZUFIQQAR ------------------
    def print_queue(self):
        global database_choice, day, time

        # -------Keep prompting the user's input until it is valid------------------
        while True:
            # -------Button for user to cancel setting date and time
            try:
                # -------Prompt user for input-----------------
                noOfpax = (askstring('Estimated waiting time', 'How many people are in queue currently?'))

                #-------If user presses x or cancel button-----------------
                if noOfpax is None:
                    break
                #-------Else try to convert user's input into integer-----------------
                else:
                    noOfpax = int(noOfpax)

            except:
                # -------Display warning if invalid input-----------------
                messagebox.showwarning(title='Estimated waiting time', message='Input only accept integer values')
            else:
                #-------If input is integer, else prompt user again-----------------
                if noOfpax or noOfpax == 0:

                    # -------If input is negative integer, show warning and prompt user again-----------------
                    if noOfpax < 0:
                        messagebox.showwarning(title='Estimated waiting time',\
                                               message='Input only accept NATURAL numbers.')

                    # -------Else get the queue time per pax from the stall's database, display the estimated queuing time and break from the loop-----------------
                    
                    elif noOfpax >= 50:
                            messagebox.showwarning(title='Estimated waiting time',\
                                                   message='Maximum input exceeded. Please enter number less than 50.')
                    else:
                        database = choosing_database(database_choice, time, day)
                        messagebox.showinfo(title=database['Title'],\
                                                message='Estimated Waiting time: {} minutes'.format(\
                                                    (database['Queue'] * (noOfpax + 1))))
                        break

    # -------Function to display Operating Hours of a stall. Function done by: NEO RUI XUAN BERLYNN-----------------
    def print_OP_Hours(self):
        global database_choice, day, time

        # -------Get the Operating Hours from the selected stall's database and display it-----------------
        database = choosing_database(database_choice, time, day)
        messagebox.showinfo(title='Operating Hours', message=database['Hours'])

    # --------Function to display calendar and time for user's input. Functions done by: MUHAMMAD ZUFIQQAR----------------
    def calender(self, controller):
        global database_choice, day, time, date

        # --------Update day, time, date based on user's input and show the correct stall's menu----------------
        def updateUserSelection(toplevel_calendar, controller, drop_sel, hour, minute):
            global day, time, date, userInputCondition

            # --------Update day, time, date based on user's input----------------
            time = (100 * int(hour)) + int(minute)
            date = drop_sel
            day = datetime.strptime(str(drop_sel), '%Y-%m-%d').weekday()

            # --------Destroy the calendar frame----------------
            toplevel_calendar.destroy()

            # --------Displaying the correct stall's menu based on user's selection and update userInputCondition to True-----------------------------
            userInputCondition = True
            page = controller.get_page(IndividualStallPage)
            page.execute()
            controller.show_frame(IndividualStallPage)

        # -------Create a TopLevel to be used for displaying calendar-------------
        toplevel_calendar = Toplevel(self, bg='black')
        toplevel_calendar.grab_set()
        
        # -------Create a Actual Calendar from tkcalendar module-------------
        calendar = Calendar(toplevel_calendar, font="Arial 14", selectmode='day', locale='en_US',\
                            mindate=datetime.now(), background='black', foreground='white', \
                            selectbackground='green', bordercolor='blue', normalforeground='blue',\
                            weekendforeground='blue', headersbackground='blue', headersforeground='white', \
                            cursor="hand1", year=int(date.strftime('%Y')), month=int(date.strftime('%m')),\
                            day=int(date.strftime('%d')))
        calendar.pack(fill="both", expand=True)

        # -------Create a Canvas inside TopLevel to be used later-------------
        canvas = Canvas(toplevel_calendar)
        canvas.pack(side=BOTTOM)

        # -------Label for hours-------------
        hour_label = Label(canvas, text="Time", font=LARGE_FONT, fg='white', bg='#00a99e')
        hour_label.pack(side=LEFT)

        # -------Populate values 0-23 (24-hours format) in a comboBox-------------
        hour = ttk.Combobox(canvas, state='readonly')
        hour['values'] = HOURS
        hour.config(width=5, font=('Helvetica', 12))
        hour.pack(side=LEFT)
        hour.current(time // 100)

        # -------Label for hours-------------
        minute_label = Label(canvas, text=":", font=LARGE_FONT, fg='white', bg='#00a99e')
        minute_label.pack(side=LEFT)

        # -------Populate values 0-59 (60 seconds) in a comboBox-------------
        minute = ttk.Combobox(canvas, state='readonly')
        minute['values'] = MINUTES
        minute.config(width=5, font=('Helvetica', 12))
        minute.pack(side=LEFT)
        minute.current(time % 100)

        # -------Button for user to press after setting the date and time-------------
        button = Button(canvas, width=10, height=1, text="OK", font='Helvetica 10', relief='flat', fg='white',bg='#00b150', \
                        command=lambda: updateUserSelection(toplevel_calendar, controller, calendar.selection_get(),\
                                                            hour.get(), minute.get()))
        button.pack(side='bottom')

    # -------Run this function first before showing IndividualStallPage to display the correct stall info and menu. Function done by: MUHAMMAD ZUFIQQAR-------------
    def execute(self):
        global database_choice, day, time

        # ---------------Display the Image Icon of the stall---------------
        bg_image = ImageTk.PhotoImage(file=outlet[database_choice][1])
        self.backgroundImageLbl.configure(image=bg_image, width=1280, height=721)
        self.backgroundImageLbl.image = bg_image

        # ---------------Display the location of the stall in NTU---------------
        database = choosing_database(database_choice, time, day)
        self.address.configure(text=database['Location'])

        # ---------------Display the title and menu of the stall---------------
        menu_string = database['Title'] + '\n'
        menu_string += get_menu_from_database(database, time, day)
        self.menu.configure(text=menu_string)


# -------For displaying instructions on how to use this application--------------------------------------------------------------------------------------------------
class InstructionPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        # ---------------Display the image that consists of the instructions---------------
        self.background_img = ImageTk.PhotoImage(file='assets/instructions.png')
        self.background = Label(self, image=self.background_img)
        self.background.place(relwidth=1, relheight=1)

        # ---------------Return to StartPage---------------
        self.home_button = Button(self, text='Home', relief='flat', fg='white', bg='#00b150', font='Helvetica 12',\
                                  height=2, width=10, command=lambda: controller.show_frame(StartPage))
        self.home_button.place(x=10, y=10)

# ---------Things to do when you press x close button of the window--------------------------------------------------------------------------------------------------
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        GUI.destroy()
        pygame.mixer.music.stop()

# --------Get the cureent time, date and day when this program first starts up
date, time, day = updateTime()

# --------Add music in the background to enhance the user experience-------------------------------------------------------------------------------------------------
pygame.mixer.init()
pygame.mixer.music.load("assets/Welcome to NTU.ogg")
pygame.mixer.music.play(-1)

# --------MAIN GUI---------------------------------------------------------------------------------------------------------------------------------------------------
GUI = window()
GUI.title("NTU Canteen Management System")
GUI.geometry('1275x670')
GUI.resizable(False, True)
GUI.protocol("WM_DELETE_WINDOW", on_closing)
GUI.mainloop()

