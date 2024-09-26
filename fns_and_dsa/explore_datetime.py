from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the date and time in "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted current date and time
    print("Current date and time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date in "YYYY-MM-DD"
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Call the function to display the current date and time
    display_current_datetime()
    
    # Call the function to calculate the future date
    calculate_future_date()

if __name__ == "__main__":
    main()
