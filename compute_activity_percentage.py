#!/usr/bin/env python3

"""
Compute the activity report for University of Gothenburg, for the PhD students.

Author: Romain Caneill

Licence: see attached LICENSE file.

Versions:
* 2021-11-03: v0.1, initial version
  by Romain Caneill
* 2021-11-08: v0.2, fix number of days / year, add option for start/end date
  by Romain Caneill
"""

"""
/* This program is free software. It comes without any warranty, to
     * the extent permitted by applicable law. You can redistribute it
     * and/or modify it under the terms of the Do What The Fuck You Want
     * To Public License, Version 2, as published by Sam Hocevar. See
     * http://www.wtfpl.net/ for more details. */
"""

def str_to_float(var):
    if var == '':
        return 0
    else:
        return float(var)

# Number of working hours per semester
WORK_DAY_HOURS = 8. # hours
WORK_HOURS = 260 * WORK_DAY_HOURS / 2

# Start / end day
print('Please enter the period: 1 for January=>June and 2 for July=>December:')
period=float(input('period: '))

print('')
print('If you started in the middle of the period you are registering, '
    'please enter your starting date. Else leave empty and hit Enter')
start_date = input('Start date in format MM-DD: ')
print('')
print('Similarly, enter your ending date if you are ending in the middle '
    'of the period you are registering')
end_date = input('End date in format MM-DD: ')
# We compute an approximate number of unemployed days
if start_date == '':
    unemployed = 0
else:
    [start_month, start_day_of_month] = [float(i) for i in start_date.split('-')]
    unemployed = ((start_month - 1 - (period - 1)*6)*30.5 + start_day_of_month) * 5/7
if end_date != '':
    [end_month, end_day_of_month] = [float(i) for i in end_date.split('-')]
    unemployed += ((7 - end_month + (period - 1)*6)*30.5 - end_day_of_month) * 5/7
unemployed *= WORK_DAY_HOURS

# Number of teaching hours and departmental duties
teaching = str_to_float(input('Number of teaching hours: '))
duties = str_to_float(input('Number of hours for other departmental duties: '))

# Number of sick leave, parental leave, etc
print('')
print('You will be asked to indicate all leaves you had. '
    'You need to give 1) the number of days and 2) the percentage of leave '
    'separated by a space\n'
    'e.g. if you were sick 1 full day and took 20 days at 60% leave, the first time '
    'you will enter "1 100" and the second time you will enter '
    '"20 60". You can give floating numbers, with a dot "." as decimal separator.\n\n')

print('You will be prompt as many times as you need to enter days.\n')

leave_hours = 0.
log = []
while True:
    days = input('Enter number of leave days and percentage, separated by a space, '
        'or leave empty and hit Enter key to continue: ')
    if days == '':
        break
    days = days.split(" ")
    h = float(days[0]) * float(days[1]) / 100 * WORK_DAY_HOURS
    leave_hours += h
    log.append([days[0], days[1], h])
    
tot_hours = teaching + duties + leave_hours + unemployed

print('')
print('*** Summary ***')
print(f'{unemployed / WORK_DAY_HOURS} days of unemployment (due to start / end date)')
print(f'{teaching} hours of teaching')
print(f'{duties} hours of other duties')
for i in log:
    print(f'{i[0]} days at {i[1]}% of leave = {i[2]} hours')
    
activity = 100 - (tot_hours / WORK_HOURS) * 100
print('')
print('We use this formula to compute your percentage of activity:')
print('activity in % = 100 - (total_hours_not_worked / number_of_hours_per_semester) * 100')
print(f'Your activity percentage is: 100 - ({tot_hours} / {WORK_HOURS}) * 100 = {activity}')
