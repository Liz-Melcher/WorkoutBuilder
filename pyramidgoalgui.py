import tkinter as tk
from tkinter import ttk, messagebox

def build_pyramid(start, peak, increment):
    """Creates a list representing a pyramid-style workout."""
    ascending = list(range(start, peak + 1, increment))
    descending = ascending[:-1][::-1]
    return ascending + descending

def total_laps(pyramid, rest_laps_per_set):
    """Calculates total laps/time including rest."""
    work = sum(pyramid)
    rest = len(pyramid) * rest_laps_per_set
    return work + rest

def find_best_pyramid(goal, start, increment, match_type):
    """Finds best pyramid matching goal."""
    peak = start
    best_pyramid = []
    best_total = 0

    while True:
        pyramid = build_pyramid(start, peak, increment)
        total = total_laps(pyramid, rest_laps_per_set=1)  # Temporary rest laps for calc

        if match_type == "at most" and total <= goal:
            best_pyramid = pyramid
            best_total = total
        elif match_type == "at least" and total >= goal:
            return pyramid, total

        if match_type == "at most" and total > goal:
            return best_pyramid, best_total

        peak += increment

def convert_time_to_seconds(time_str):
    """Convert mm:ss or seconds string to total seconds."""
    if ':' in time_str:
        mins, secs = time_str.split(':')
        return int(mins)*60 + int(secs)
    else:
        return int(time_str)

def convert_seconds_to_time(sec):
    """Convert total seconds to mm:ss format."""
    mins = sec // 60
    secs = sec % 60
    return f"{mins}:{secs:02}"

class WorkoutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🏋️ Pyramid Workout Planner 🏃‍♀️")

        # Variables
        self.goal_var = tk.StringVar()
        self.start_var = tk.StringVar(value='1')
        self.increment_var = tk.StringVar(value='1')
        self.match_type_var = tk.StringVar(value='at most')
        self.unit_var = tk.StringVar(value='laps')
        self.rest_var = tk.StringVar(value='1')

        # Layout
        ttk.Label(self, text="Goal total (laps or mm:ss):").grid(row=0, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.goal_var).grid(row=0, column=1)

        ttk.Label(self, text="Starting work (laps or mm:ss):").grid(row=1, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.start_var).grid(row=1, column=1)

        ttk.Label(self, text="Increment (laps or mm:ss):").grid(row=2, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.increment_var).grid(row=2, column=1)

        ttk.Label(self, text="Rest after each set (laps or mm:ss):").grid(row=3, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.rest_var).grid(row=3, column=1)

        ttk.Label(self, text="Match Type:").grid(row=4, column=0, sticky="w")
        ttk.Combobox(self, values=["at most", "at least"], textvariable=self.match_type_var, state="readonly").grid(row=4, column=1)

        ttk.Label(self, text="Unit:").grid(row=5, column=0, sticky="w")
        ttk.Combobox(self, values=["laps", "time"], textvariable=self.unit_var, state="readonly").grid(row=5, column=1)

        ttk.Button(self, text="Build Workout", command=self.build_workout).grid(row=6, column=0, columnspan=2, pady=10)

        self.output_text = tk.Text(self, width=40, height=15, state='disabled')
        self.output_text.grid(row=7, column=0, columnspan=2)

    def build_workout(self):
        try:
            unit = self.unit_var.get()
            match_type = self.match_type_var.get()

            # Convert inputs based on unit
            if unit == 'laps':
                goal = int(self.goal_var.get())
                start = int(self.start_var.get())
                increment = int(self.increment_var.get())
                rest_laps_per_set = int(self.rest_var.get())
            else:
                goal = convert_time_to_seconds(self.goal_var.get())
                start = convert_time_to_seconds(self.start_var.get())
                increment = convert_time_to_seconds(self.increment_var.get())
                rest_laps_per_set = convert_time_to_seconds(self.rest_var.get())

            # Validate inputs
            if start <= 0 or increment <= 0 or rest_laps_per_set < 0:
                raise ValueError("Start and increment must be > 0; rest must be ≥ 0.")
            if match_type not in ["at most", "at least"]:
                raise ValueError("Match type must be 'at most' or 'at least'.")

            # Modify find_best_pyramid to accept rest_laps_per_set for total calculation
            peak = start
            best_pyramid = []
            best_total = 0
            while True:
                pyramid = build_pyramid(start, peak, increment)
                total = total_laps(pyramid, rest_laps_per_set)

                if match_type == "at most" and total <= goal:
                    best_pyramid = pyramid
                    best_total = total
                elif match_type == "at least" and total >= goal:
                    best_pyramid = pyramid
                    best_total = total
                    break

                if match_type == "at most" and total > goal:
                    break

                peak += increment

            # Display output
            self.output_text.config(state='normal')
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, "📋 Your Workout Plan:\n")
            for i, reps in enumerate(best_pyramid, 1):
                if unit == 'laps':
                    rest_display = f"{rest_laps_per_set} lap{'s' if rest_laps_per_set != 1 else ''} rest"
                    self.output_text.insert(tk.END, f"Set {i}: {reps} laps hard, {rest_display}\n")
                else:
                    rest_display = convert_seconds_to_time(rest_laps_per_set) + " rest"
                    self.output_text.insert(tk.END, f"Set {i}: {convert_seconds_to_time(reps)} time hard, {rest_display}\n")

            if unit == 'laps':
                self.output_text.insert(tk.END, f"\n🏁 Total laps (including rest): {best_total}\n")
            else:
                self.output_text.insert(tk.END, f"\n🏁 Total time (including rest): {convert_seconds_to_time(best_total)}\n")

            self.output_text.config(state='disabled')

        except ValueError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = WorkoutApp()
    app.mainloop()
