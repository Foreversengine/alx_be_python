from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculate and display a future date after adding a specified number of days to the current date.
    """
    try:
        # Prompt the user to enter the number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Calculate the future date
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        
        # Format and display the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input! Please enter an integer value for the number of days.")

def main():
    """
    Main function to execute the script.
    """
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()
