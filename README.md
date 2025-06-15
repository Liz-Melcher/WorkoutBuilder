# WorkoutBuilder

Ask user for:
  - goal total laps
  - starting laps (minimum step)
  - increment (how fast to climb the pyramid)
  - match type (<= or >=)

Initialize peak to starting laps

While True:
  Build pyramid: climb up from start to peak by increment, then down
  For each step in pyramid:
    Add step laps of work
    Add 1 lap rest
  Calculate total laps (work + rest)

  If match type condition is met (>= or <=):
    break
  Else:
    peak += increment

Print pyramid plan
Print total laps


es — you're thinking like a developer now. 👏
You're seeing shared inputs and logic between two workflows:
🔁 Shared Concepts Across Both Modes
Feature	Used In "From Goal"	Used In "From Base"	Shared
increment	✅	✅	✅
rest_laps_per_set	✅	✅	✅
start (starting reps)	✅	✅	✅
peak (max reps)	❌ (calculated)	✅	
goal_total_laps	✅	❌	
match type (>=, <=)	✅	❌	
🧱 Suggested Refactor: A Unified Structure

Split the app like this:
1. Core Logic (Shared) in a pyramid_utils.py:

    build_pyramid(start, peak, increment)

    total_laps(pyramid, rest_laps_per_set)

    Maybe: validate_inputs()

2. CLI Entry Points:

    pyramid_from_goal.py

    pyramid_from_base.py

Each one:

    Handles its specific inputs (goal vs peak)

    Calls the shared logic

