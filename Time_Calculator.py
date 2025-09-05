def add_time(start, duration, starting_day=None):
    # determine if the time is AM or PM
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # determine the new minute and any additional hours
    additional_hours = 0
    new_minute = start_minute + duration_minute
    if new_minute >= 60:
        additional_hours = new_minute // 60
        new_minute = new_minute % 60

    # determine the new hour
    new_hour = start_hour + duration_hour + additional_hours

    # determine the number of periods passed
    periods_passed = (new_hour) // 12

    # adjust the new hour to a 12-hour format
    new_hour = new_hour % 12
    if new_hour == 0:
        new_hour = 12

    # determine the new period
    new_period = period
    if periods_passed % 2 == 1:
        new_period = 'PM' if period == 'AM' else 'AM'

    new_time = str(new_hour) + ':' + str(new_minute).zfill(2) + ' ' + new_period

    # determine the day
    additional_days = periods_passed // 2 + (1 if new_period == 'AM' and period == 'PM' and periods_passed > 0 else 0)
    if starting_day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        starting_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (starting_day_index + additional_days) % 7
        new_day = days_of_week[new_day_index]
        new_time += ', ' + new_day.capitalize()

    # add information about the number of days passed
    if additional_days == 1:
        new_time += ' (next day)'
    elif additional_days > 1:
        new_time += ' (' + str(additional_days) + ' days later)'

    return new_time