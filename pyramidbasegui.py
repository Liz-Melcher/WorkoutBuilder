import tkinter as tk
from tkinter import messagebox

def build_pyramid(start, peak, increment):
    ascending = list(range(start, peak + 1, increment))
    descending = ascending[:-1][::-1]
    return ascending + descending

def total_laps(pyramid, rest_laps_per_set):
    work_laps = sum(pyramid)
    rest_laps = len(pyramid) * rest_laps_per_set
    return work_laps + rest_laps

def calculate_pyramid(start, peak, increment, rest_laps_per_set):
    pyramid = build_pyramid(start, peak, increment)
    total = total_laps(pyramid, rest_laps_per_set)
    return pyramid, total

def on_calculate():
    try:
        start = int(entry_start.get())
        peak = int(entry_peak.get())
        increment = int(entry_increment.get())
        rest = int(entry_rest.get())

        if start <= 0 or peak <= 0 or increment <= 0:
            raise ValueError("All inputs must be positive integers.")
        if peak < start:
            raise ValueError("Peak must be greater than or equal to start.")
        if rest < 0:
            raise ValueError("Rest laps must be 0 or greater.")

        pyramid, total = calculate_pyramid(start, peak, increment, rest)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "📋 Your Workout Plan:\n")
        for i, reps in enumerate(pyramid):
            output_text.insert(tk.END, f"Set {i+1}: {reps} laps hard, {rest} lap(s) rest\n")
        output_text.insert(tk.END, f"\n🏁 Total laps (including rest): {total}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# GUI setup
root = tk.Tk()
root.title("🏋️ Pyramid Workout Planner 🏃‍♀️")

# Input fields
tk.Label(root, text="Starting Laps:").grid(row=0, column=0, sticky="e")
entry_start = tk.Entry(root)
entry_start.grid(row=0, column=1)

tk.Label(root, text="Peak Laps:").grid(row=1, column=0, sticky="e")
entry_peak = tk.Entry(root)
entry_peak.grid(row=1, column=1)

tk.Label(root, text="Increment:").grid(row=2, column=0, sticky="e")
entry_increment = tk.Entry(root)
entry_increment.grid(row=2, column=1)

tk.Label(root, text="Rest Laps per Set:").grid(row=3, column=0, sticky="e")
entry_rest = tk.Entry(root)
entry_rest.grid(row=3, column=1)

# Calculate button
tk.Button(root, text="Calculate Workout", command=on_calculate).grid(row=4, column=0, columnspan=2, pady=10)

# Output text area
output_text = tk.Text(root, width=40, height=15, wrap="word")
output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
