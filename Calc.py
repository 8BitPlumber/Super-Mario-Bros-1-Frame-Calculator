import tkinter as tk
from tkinter import ttk

def calculate_frames():
    try:
        timing_started = float(entry_started.get())
        timing_ended = float(entry_ended.get())

        if framerate_var.get() == "NTSC":
            framerate = 60.098813897441
        elif framerate_var.get() == "PAL":
            framerate = 50.006978908189
        else:
            framerate = float(entry_custom_framerate.get())

        frames = (timing_ended - timing_started) / framerate
        minutes = int(frames / 60)
        seconds = frames % 60

        result_label.config(text=f"Time: {minutes:02d}:{seconds:06.3f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

def update_framerate_entry(*args):
    if framerate_var.get() == "Custom":
        label_custom_framerate.grid(row=3, column=0, padx=10, pady=5, sticky="E")
        entry_custom_framerate.grid(row=3, column=1, padx=10, pady=5, sticky="W")
    else:
        label_custom_framerate.grid_forget()
        entry_custom_framerate.grid_forget()

# Create the main window
window = tk.Tk()
window.title("Super Mario Bros 1 Frame Calculator")

# Create and place input boxes and labels
label_started = tk.Label(window, text="Frame Timing Started:")
label_started.grid(row=0, column=0, padx=10, pady=5, sticky="E")

entry_started = tk.Entry(window)
entry_started.grid(row=0, column=1, padx=10, pady=5)

label_ended = tk.Label(window, text="Frame Timing Ended:")
label_ended.grid(row=1, column=0, padx=10, pady=5, sticky="E")

entry_ended = tk.Entry(window)
entry_ended.grid(row=1, column=1, padx=10, pady=5)

# Create and place the framerate selection dropdown
label_framerate = tk.Label(window, text="Select Framerate:")
label_framerate.grid(row=2, column=0, padx=10, pady=5, sticky="E")

framerate_var = tk.StringVar(value="NTSC")
framerate_options = ["NTSC", "PAL", "Custom"]
framerate_menu = ttk.Combobox(window, textvariable=framerate_var, values=framerate_options, state="readonly")
framerate_menu.grid(row=2, column=1, padx=10, pady=5, sticky="W")
framerate_var.trace("w", update_framerate_entry)

# Create and place the custom framerate entry
label_custom_framerate = tk.Label(window, text="Custom Framerate:")
entry_custom_framerate = tk.Entry(window)
label_custom_framerate.grid_remove()
entry_custom_framerate.grid_remove()

# Create and place the calculate button
calculate_button = tk.Button(window, text="Calculate Time", command=calculate_frames)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=5)

# Start the main loop
window.mainloop()
