import tkinter as tk
import time


def toggle_contador(self, event=None):
    if not self.started:
        if self.initial_time is None:
            self.initial_time = time.time()
        else:
            self.initial_time += time.time() - self.stoped_time
        self.started = True
        self.update_time()
        self.buttom_start.config(text="Detener")
        self.buttom_restart.config(state=tk.DISABLED)
    else:
        self.started = False
        self.stoped_time = time.time()
        self.buttom_start.config(text="Continuar")
        self.buttom_restart.config(state=tk.NORMAL)

def reiniciar_contador(self):
    self.started = False
    self.initial_time = None
    self.remaining_time = 0
    self.label_time.config(text="00:00:00.000")
    self.buttom_start.config(text="Iniciar")
    self.buttom_restart.config(state=tk.DISABLED)

def update_time(self):
    if self.started:
        elapsed_time = time.time() - self.initial_time + self.remaining_time
        hours, minutes = divmod(int(elapsed_time), 3600)
        minutes, seconds = divmod(minutes, 60)
        milliseconds = int((elapsed_time % 1) * 1000)
        self.label_time.config(text=f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}")
        self.root.after(1, self.update_time)