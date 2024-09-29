from datetime import datetime, timedelta

def display_current_datetime():

    current_date = datetime.now()
    current_date_format = current_date
    return current_date_format

print("Current date and time: " + display_current_datetime().strftime("%Y-%m-%d %H:%M:%S"))

number_of_days = float(input("Enter the number of days to add to the current date: "))

def calculate_future_date(number_of_days):

    current_date = display_current_datetime()
    future_date = current_date + timedelta(days = number_of_days)
    future_date_format = future_date.strftime("%Y-%m-%d")

    return future_date_format

print("Future date: " + calculate_future_date(number_of_days))