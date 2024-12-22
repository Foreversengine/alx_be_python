# Prompt the user for a single task description
task = input("Enter your task: ")

# Prompt for the task's priority level
priority = input("Priority (high/medium/low): ").strip().lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate a customized reminder using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority."

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the final reminder
print(f"Reminder: {reminder}")