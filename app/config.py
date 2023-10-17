import tkinter as tk


class Config:
    def __init__(self, root):
        self.root = root

    def configure_app(self):
        
        # Set the title for the window
        self.root.title("Timer")

        # Set the default window size
        self.root.geometry("300x150")

        # Disable resizing the window
        self.root.resizable(False, False)

        # Center the window
        self.root.eval('tk::PlaceWindow . center') 

        # Set the icon of the window
        self.root.iconbitmap("images/timer_icon.ico")

        # Cambiar el fondo de la ventana principal a negro
        self.root.configure(bg="#1f1f1f")

        
