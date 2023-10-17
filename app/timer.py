import tkinter as tk
from config import Config
from utilities import toggle_contador, reiniciar_contador, update_time
import time


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

        self.label_time = tk.Label(root, text="00:00:00.000", font=("Lucida Console", 24), bg="#1f1f1f", fg="white")
        self.label_time.pack(pady=10)

        self.frame_buttons = tk.Frame(root, bg="#1f1f1f")
        self.frame_buttons.pack()

        self.buttom_start = tk.Button(self.frame_buttons, text="Start", command=self.toggle_contador, bg="gray", fg="white", highlightbackground="white")
        self.buttom_restart = tk.Button(self.frame_buttons, text="Restart", command=self.reiniciar_contador, state=tk.DISABLED, bg="gray", fg="white", highlightbackground="white")

        self.buttom_start.pack(side="left", padx=5, pady=10)
        self.buttom_restart.pack(side="left", padx=5, pady=10)

        # Agregar un enlace de tecla de espacio
        self.root.bind("<space>", self.toggle_contador)

    # def toggle_contador(self, event=None):
    #     if not self.started:
    #         if self.initial_time is None:
    #             self.initial_time = time.time()
    #         else:
    #             self.initial_time += time.time() - self.stoped_time
    #         self.started = True
    #         self.update_time()
    #         self.buttom_start.config(text="Detener")
    #         self.buttom_restart.config(state=tk.DISABLED)
    #     else:
    #         self.started = False
    #         self.stoped_time = time.time()
    #         self.buttom_start.config(text="Continuar")
    #         self.buttom_restart.config(state=tk.NORMAL)

    # def reiniciar_contador(self):
    #     self.started = False
    #     self.initial_time = None
    #     self.remaining_time = 0
    #     self.label_time.config(text="00:00:00.000")
    #     self.buttom_start.config(text="Iniciar")
    #     self.buttom_restart.config(state=tk.DISABLED)

    # def update_time(self):
    #     if self.started:
    #         elapsed_time = time.time() - self.initial_time + self.remaining_time
    #         hours, minutes = divmod(int(elapsed_time), 3600)
    #         minutes, seconds = divmod(minutes, 60)
    #         milliseconds = int((elapsed_time % 1) * 1000)
    #         self.label_time.config(text=f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}")
    #         self.root.after(1, self.update_time)


    def toggle_contador(self, event=None):
        toggle_contador(self)

    def reiniciar_contador(self):
        reiniciar_contador(self)

    def update_time(self):
        update_time(self)

    def configure_application(self):
        config = Config(self.root)
        config.configure_app()




