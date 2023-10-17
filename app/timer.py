import tkinter as tk
from config import Config
from utilities import toggle_contador, restart_timer, update_time
import json

with open("config.json", "r") as file:
    config = json.load(file)

class Timer:
    def __init__(self, root):
        self.root = root

        #Initialize the configuration of the application
        self.configure_application()

        # Initialize the variables
        self.remaining_time = 0
        self.started = False
        self.initial_time = None
        self.stoped_time = None


        # Create the time label
        self.label_time = tk.Label(root, text="00:00:00.000", font=("Lucida Console", 24), bg=config.get("bg_color"), fg=config.get("font_color"))
        self.label_time.pack(pady=10)

        # Create the frame for the buttons
        self.frame_buttons = tk.Frame(root, bg=config.get("bg_color"))
        self.frame_buttons.pack()

        # Create the buttons
        self.buttom_start = tk.Button(self.frame_buttons, text="Start", command=self.toggle_contador, bg=config.get("btn_color"), fg=config.get("font_color"), highlightbackground="white")
        self.buttom_restart = tk.Button(self.frame_buttons, text="Restart", command=self.restart_timer, state=tk.DISABLED, bg=config.get("btn_color"), fg=config.get("font_color"), highlightbackground="white")

        # Position the buttons
        self.buttom_start.pack(side="left", padx=5, pady=10)
        self.buttom_restart.pack(side="left", padx=5, pady=10)

        # Add the key bindings
        self.root.bind("<space>", self.toggle_contador)



    # Initialize the methods
    
    def toggle_contador(self, event=None):
        toggle_contador(self)

    def restart_timer(self):
        restart_timer(self)

    def update_time(self):
        update_time(self)

    def configure_application(self):
        config = Config(self.root)
        config.configure_app()




