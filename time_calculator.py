def add_time(start_time, duration, weekday=None):
    modify_start_time = start_time.replace(":", " ")
    start_list = [int(i) for i in modify_start_time.split()[:2]]
    duration_list = [int(i) for i in duration.split(":")]

    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    # Special cases of 12am and 12pm
    if start_list[0] == 12:
        start_list[0] = 0

    # Assume start times are AM and add 12 to duration if PM
    am_or_pm = "AM"
    if "PM" in start_time and start_list[0] != 12:
        duration_list[0] += 12

    # Change total minutes to hours and mins
    mins_as_hours = (start_list[1] + duration_list[1]) / 60
    hour_min = int(mins_as_hours)
    min_min = (start_list[1] + duration_list[1]) % 60
    if min_min < 10:
        min_min = f"0{min_min}"

    # Does the time run into the next day? (next day) or (n days later)
    day_message = None
    days_in_hours = start_list[0] + duration_list[0] + hour_min
    if days_in_hours >= 24 and days_in_hours < 48:
        day_message = "(next day)"
    if days_in_hours >= 48:
        weekdays_n = int(days_in_hours / 24)
        day_message = f"({weekdays_n} days later)"

    # Find which day it is
    if weekday != None:
        start_day = weekdays.index(weekday.title())
        end_day = weekdays[(start_day + int((days_in_hours / 24))) % 7]

    # Is it morning or afternoon
    if days_in_hours % 24 >= 12:
        am_or_pm = "PM"
    if days_in_hours % 24 < 12:
        am_or_pm = "AM"

    new_hour = days_in_hours % 12
    if new_hour == 0:
        new_hour = 12
    new_time = f"{new_hour}:{min_min}"

    # Formulate output
    if day_message == None and weekday == None:
        print(f"{new_time} {am_or_pm}")
    if day_message != None and weekday == None:
        print(f"{new_time} {am_or_pm} {day_message}")
    if day_message != None and weekday != None:
        print(f"{new_time} {am_or_pm}, {end_day} {day_message}")
    if day_message == None and weekday != None:
        print(f"{new_time} {am_or_pm}, {end_day}")


add_time("11:40 AM", "24:25", "fRidAy")
