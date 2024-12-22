# Prompt the user for a single task description
task = input("Enter the task description: ")

# Prompt for the task's priority level
priority = input("What is the task's priority? (high, medium, low): ").strip().lower()

# Ask if the task is time-bound
time_bound = input("Is the task time-sensitive? (yes or no): ").strip().lower()

# Generate a customized reminder based on the inputs
match priority:
    case "high":
        reminder = f"Your task: '{task}' is HIGH priority."
    case "medium":
        reminder = f"Your task: '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Your task: '{task}' is LOW priority."
    case _:
        reminder = f"Your task: '{task}' has an UNKNOWN priority."

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the final reminder
print(reminder)