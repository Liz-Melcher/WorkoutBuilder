def build_pyramid(start, peak, increment):
    """Creates a list representing a pyramid-style workout."""
    ascending = list(range(start, peak + 1, increment))
    descending = ascending[:-1][::-1]
    return ascending + descending

def total_laps(pyramid):
    """Calculates total laps including rest (1 rest per work set)."""
    work_laps = sum(pyramid)
    rest_laps = len(pyramid)  # 1 rest per work set  TODO: rest laps isn't asking for a value, and should be able to have any value 
    return work_laps + rest_laps

def find_best_pyramid(goal_laps, start, increment, match_type):
    """Finds the best pyramid that fits the user's goal criteria."""
    peak = start
    best_pyramid = []

    while True:
        pyramid = build_pyramid(start, peak, increment)
        total = total_laps(pyramid)

        if match_type == "at most" and total <= goal_laps:
            best_pyramid = pyramid
        elif match_type == "at least" and total >= goal_laps:
            return pyramid, total

        if match_type == "at most" and total > goal_laps:
            return best_pyramid, total_laps(best_pyramid)

        peak += increment

def main():
    print("🏋️ Pyramid Workout Planner 🏃‍♀️")
    try:
        goal_laps = int(input("Enter your goal total laps (including rest): "))
        start = int(input("Enter your starting work laps (e.g., 1): "))
        increment = int(input("Enter increment for each step (e.g., 1 or 2): "))
        match_type = input("Do you want 'at most' or 'at least' this many laps? ").strip().lower()
        
        if match_type not in ["at most", "at least"]:
            raise ValueError("Match type must be 'at most' or 'at least'.")

        pyramid, total = find_best_pyramid(goal_laps, start, increment, match_type)

        print("\n📋 Your Workout Plan:")
        for i, reps in enumerate(pyramid, 1):
            print(f"Set {i}: {reps} laps hard, 1 lap rest")

        print(f"\n🏁 Total laps (including rest): {total}")

    except ValueError as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
