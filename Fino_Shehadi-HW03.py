# Shehadi Fino
# UWYO COSC 1010
# 11-4-24
# HW 03
# Lab Section: 14
# Sources, people worked with, help given to: Ryan
# your
# comments
# here

days_in_a_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wedensday", "Thursday", "Friday", "Saturday"]

def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

def calculate_jan_day_1(year):
    y = year -1
    return (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7

def valid_date(month, day, year):
    if month < 1 or month > 12:
        return False
    if day < 1: 
        return False
    max_days = days_in_a_month[month]
    if month == 2 and leap_year(year):
        max_days = 29
    return day <= max_days

def days_since_jan_day_1(month, day, year):
    days = sum(days_in_a_month[m] for m in range(1, month)) + day - 1
    if month > 2 and leap_year(year):
        days += 1
    return days

def get_day_of_the_week(date_t):
    try:
        month, day, year = map(int, date_t.split('/'))
    except ValueError:
        return "Invalid Date"
    
    if not valid_date(month, day, year):
        return f"{date_t} Invalid Date"
    
    jan_day_1 = calculate_jan_day_1(year)
    days_from_jan_day_1 = days_since_jan_day_1(month, day, year)
    day_of_week = (jan_day_1 + days_from_jan_day_1) % 7

    return f"{date_t} {days_of_the_week[day_of_week]}"

dates = ["02/21/2022", "01/01/2022","02/29/2024", "02/29/2023",
    "04/31/2023", "02/00/2023"
]
for date in dates:
    print(get_day_of_the_week(date))

def main():
    while True:
        date_user_input = input("Enter a date in MM/DD/YYYY format (type 'exit' to quit): ")
        if date_user_input.lower() == 'exit':
            break
        result = get_day_of_the_week(date_user_input)
        print(result)

if __name__ == "__main__":
    main()