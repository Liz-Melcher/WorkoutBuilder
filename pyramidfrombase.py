def build_pyramid(start, peak, increment):
    """Creates a list representing a pyramid-style workout."""
    ascending = list(range(start, peak + 1, increment))
    descending = ascending[:-1][::-1]
    return ascending + descending

def total_laps(pyramid, rest_laps_per_set):
    """Calculates total laps including rest after every set."""
    work_laps = sum(pyramid)
    rest_laps = len(pyramid) * rest_laps_per_set  # rest after every set
    return work_laps + rest_laps

def calculate_pyramid(start, peak, increment, rest_laps_per_set):
    """Calculates the pyramid workout and total laps."""
    pyramid = build_pyramid(start, peak, increment)
    total = total_laps(pyramid, rest_laps_per_set)
    return pyramid, total

def main(): 
    print("🏋️ Pyramid Workout Planner 🏃‍♀️")
    try:
        start = int(input("Enter your starting work laps (e.g., 1): "))
        peak = int(input("Enter your peak work laps (e.g., 5): "))
        increment = int(input("Enter increment for each step (e.g., 1 or 2): "))
        rest_laps_per_set = int(input("How many rest laps after each set? (e.g., 1, 2, or 0): "))

        if start <= 0 or peak <= 0 or increment <= 0:
            raise ValueError("All inputs must be positive integers.")
        if peak < start:
            raise ValueError("Peak must be greater than or equal to start.")
        if rest_laps_per_set < 0:
            raise ValueError("Rest laps must be 0 or greater.")

        pyramid, total = calculate_pyramid(start, peak, increment, rest_laps_per_set)

        print("\n📋 Your Workout Plan:")
        for i, reps in enumerate(pyramid):
            print(f"Set {i+1}: {reps} laps hard, {rest_laps_per_set} lap(s) rest")

        print(f"\n🏁 Total laps (including rest): {total}")

    except ValueError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
