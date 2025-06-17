import tkinter as tk
from tkinter import messagebox, ttk

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

def parse_time_input(value: str) -> int:
    """Converts 'minutes:seconds' or 'float minutes' to total seconds (as int)."""
    value = value.strip()
    if ":" in value:
        try:
            mins, secs = map(int, value.split(":"))
            return mins * 60 + secs
        except ValueError:
            raise ValueError("Invalid time format. Use MM:SS or decimal minutes.")
    else:
        return int(float(value) * 60)

def parse_value(value: str, unit_type: str) -> int:
    """Parses the input string based on unit type ('laps' or 'time')"""
    if unit_type == "time":
        return parse_time_input(value)
    else:  # unit_type == 'laps'
        return int(value)

def format_seconds(seconds: int) -> str:
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes}:{secs:02d}"

def on_calculate():
    unit_type = unit_var.get()
    try:
        start = parse_value(entry_start.get(), unit_type)
        peak = parse_value(entry_peak.get(), unit_type)
        increment = parse_value(entry_increment.get(), unit_type)
        rest = parse_value(entry_rest.get(), unit_type)

        if start <= 0 or peak <= 0 or increment <= 0:
            raise ValueError("All inputs must be positive numbers.")
        if peak < start:
            raise ValueError("Peak must be greater than or equal to start.")
        if rest < 0:
            raise ValueError("Rest must be 0 or greater.")

        pyramid, total = calculate_pyramid(start, peak, increment, rest)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"📋 Your Workout Plan ({unit_type}):\n")
        for i, reps in enumerate(pyramid):
            reps_display = format_seconds(reps) if unit_type == "time" else reps
            rest_display = format_seconds(rest) if unit_type == "time" else rest
            output_text.insert(tk.END, f"Set {i+1}: {reps_display} {unit_type}, {rest_display} rest\n")

        total_display = format_seconds(total) if unit_type == "time" else total
        output_text.insert(tk.END, f"\n🏁 Total {unit_type} (including rest): {total_display}")
        print("Unit type:", unit_type)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# GUI setup
root = tk.Tk()
root.title("🏋️ Pyramid Workout Planner 🏃‍♀️")

# Dropdown for unit type
unit_var = tk.StringVar(value="laps")
tk.Label(root, text="Unit Type:").grid(row=0, column=0, sticky="e")
unit_menu = ttk.Combobox(root, textvariable=unit_var, values=["laps", "time"], state="readonly")
unit_menu.grid(row=0, column=1)

# Input fields
tk.Label(root, text="Starting Value:").grid(row=1, column=0, sticky="e")
entry_start = tk.Entry(root)
entry_start.grid(row=1, column=1)

tk.Label(root, text="Peak Value:").grid(row=2, column=0, sticky="e")
entry_peak = tk.Entry(root)
entry_peak.grid(row=2, column=1)

tk.Label(root, text="Increment per Step:").grid(row=3, column=0, sticky="e")
entry_increment = tk.Entry(root)
entry_increment.grid(row=3, column=1)

tk.Label(root, text="Rest per Set:").grid(row=4, column=0, sticky="e")
entry_rest = tk.Entry(root)
entry_rest.grid(row=4, column=1)

# Calculate button
tk.Button(root, text="Calculate Workout", command=on_calculate).grid(row=5, column=0, columnspan=2, pady=10)

# Output text area
output_text = tk.Text(root, width=50, height=15, wrap="word")
output_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
