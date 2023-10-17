import tkinter as tk
import time


def toggle_contador(self, event=None):
    # Check if the timer is not started
    if not self.started:
        # If not started, start the timer
        if self.initial_time is None:
            self.initial_time = time.time()
        else:
            # Else, update the elapsed time
            self.initial_time += time.time() - self.stoped_time
        # start the timer
        self.started = True
        # Display the elapsed time
        self.update_time()
        # Change the button text 
        self.buttom_start.config(text="Stop")
        # Disable button
        self.buttom_restart.config(state=tk.DISABLED)
    else:
        # If the timer is started stop the timer
        self.started = False
        # Store the elapsed time
        self.stoped_time = time.time()
        # Change the button text
        self.buttom_start.config(text="Continue")
        # Enable button
        self.buttom_restart.config(state=tk.NORMAL)

def restart_timer(self):
    # Restart the status of the timer
    self.started = False
    self.initial_time = None
    self.remaining_time = 0
    self.label_time.config(text="00:00:00.000")

    # Change the button text 
    self.buttom_start.config(text="Start")
    # Disable the button
    self.buttom_restart.config(state=tk.DISABLED)

def update_time(self):
    # If the timer is running update the elapsed time
    if self.started:
        # Calculate the elapsed time
        elapsed_time = time.time() - self.initial_time + self.remaining_time
        # Get the hours, minutes, seconds and milliseconds
        hours, minutes = divmod(int(elapsed_time), 3600)
        minutes, seconds = divmod(minutes, 60)
        milliseconds = int((elapsed_time % 1) * 1000)
        # Update the displayed time in a specific format
        self.label_time.config(text=f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}")
        # update the time every 1 ms
        self.root.after(1, self.update_time)
