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
