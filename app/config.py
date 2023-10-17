import tkinter as tk
import json

with open("config.json", "r") as file:
    config = json.load(file)

class Config:
    def __init__(self, root):
        self.root = root

    def configure_app(self):
        
        # Set the title for the window
        self.root.title(config.get("app_title"))

        # Set the default window size
        self.root.geometry(config.get("window_size"))

        # Disable resizing the window
        self.root.resizable(False, False)

        # Center the window
        self.root.eval('tk::PlaceWindow . center') 

        # Set the icon of the window
        self.root.iconbitmap(config.get("app_icon"))

        # Set the background color
        self.root.configure(bg=config.get("bg_color"))

        
