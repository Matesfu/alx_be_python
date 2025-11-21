from datetime import datetime, timedelta

def display_current_datetime():
    return datetime.now()
current_date = display_current_datetime()
formatted_date = current_date.strftime("%y-%m-%d %H:%M:%S")
print("Current date and time: ", formatted_date)

number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date(number_of_days):
    return (current_date + timedelta(days=number_of_days)).strftime("%y-%m-%d")
future_date = calculate_future_date(number_of_days=number_of_days)
print("Future date: ", future_date)
