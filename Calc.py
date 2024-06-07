import tkinter as tk

def calculate_frames():
    try:
        timing_started = float(entry_started.get())
        timing_ended = float(entry_ended.get())

        frames = (timing_ended - timing_started) / 60.0988139
        minutes = int(frames / 60)
        seconds = frames % 60

        result_label.config(text=f"Time: {minutes:02d}:{seconds:06.3f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Super Mario Bros 1 TAS Frame Calculator")

# Create and place input boxes and labels
label_started = tk.Label(window, text="Frame Timing Started:")
label_started.grid(row=0, column=0, padx=10, pady=5, sticky="E")

entry_started = tk.Entry(window)
entry_started.grid(row=0, column=1, padx=10, pady=5)

label_ended = tk.Label(window, text="Frame Timing Ended:")
label_ended.grid(row=1, column=0, padx=10, pady=5, sticky="E")

entry_ended = tk.Entry(window)
entry_ended.grid(row=1, column=1, padx=10, pady=5)

# Create and place the calculate button
calculate_button = tk.Button(window, text="Calculate Frames", command=calculate_frames)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Start the main loop
window.mainloop()
