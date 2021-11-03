#!/usr/bin/env python3

"""
Compute the activity report for University of Gothenburg, for the PhD students.

Author: Romain Caneill

Licence:
Copyright © 2021 Romain Caneill <romain.caneill@gu.se>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See below for more details.

       DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""

"""
/* This program is free software. It comes without any warranty, to
     * the extent permitted by applicable law. You can redistribute it
     * and/or modify it under the terms of the Do What The Fuck You Want
     * To Public License, Version 2, as published by Sam Hocevar. See
     * http://www.wtfpl.net/ for more details. */
"""

# Number of working hours per semester
WORK_HOURS = 877.
WORK_DAY_HOURS = 8. # hours

# Number of teaching hours and departmental duties
teaching = float(input('Number of teaching hours: '))
duties = float(input('Number of hours for other departmental duties: '))

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
    
tot_hours = teaching + duties + leave_hours

print('')
print('*** Summary ***')
print(f'{teaching} hours of teaching')
print(f'{duties} hours of other duties')
for i in log:
    print(f'{i[0]} days at {i[1]}% of leave = {i[2]} hours')
    
activity = 100 - (tot_hours / WORK_HOURS) * 100
print('')
print('We use this formula to compute your percentage of activity:')
print('activity in % = 100 - (total_hours_not_worked / number_of_hours_per_semester) * 100')
print(f'Your activity percentage is: 100 - ({tot_hours} / {WORK_HOURS}) * 100 = {activity}')
