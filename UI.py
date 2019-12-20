from tkinter import *

class UI(Frame):
    # Les widgets seront stockés ici en tant qu'attributs de cette fenêtre

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=800, height=500, **kwargs)
        self.pack()

        Frame1 = Frame(fenetre)
        Frame1.pack(side=BOTTOM, padx=50, pady=50)

        self.button_quit = Button(Frame1,text="Quitter",command=self.quit)
        # self.button_quit = Button(Frame1,text="Quitter",padx=10,pady=10,command=self.quit)
        self.button_quit.pack(side=LEFT)