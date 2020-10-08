import tkinter
from controllers.controller import controller

class tk_view:
    def __init__(self):
        self.controller=controller()
        self.controller.open("https://web.whatsapp.com/")
        #?------------------Creating-the-main-screen-----------------------------
        self.app = tkinter.Tk() #Making the main root
        self.app.geometry("200x200") # Setting the size of the main window
        self.app.title("Cd Burner") 
        #self.app.iconbitmap("icons/icon.ico") #Setting the main left top icon
        #?-----------------Populating-the-main-screen----------------------------
        self.button_main = tkinter.Button(master=self.app,text="Start",command=self.run_time,height = 5, width = 9)
        self.button_main.pack(padx=10,pady=40)

    def run_time(self):
        self.controller.printer("adoro-te, és linda",50)