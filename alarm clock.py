import time
import win32api
from plyer import notification  # for getting notification on your PC
import requests
import win10toast

result1 = time.localtime()

name_tuple = time.strftime('%H:%M:%S', result1)
print('Current time: ',name_tuple)
hr = result1.tm_hour
mn = result1.tm_min

print('At what time would you like to put your alarm?')
hour = int(input('hour:'))
minute = int(input('minute:'))
name = input('Alarm Name:')
description = input('Add a description: ')

alrm_hr = abs(hour - hr)
alrm_min = abs(minute - mn)

print('Alarm set at %d' % alrm_hr, 'hr %d' % alrm_min, 'min from current time')



sleep_time = alrm_hr * 60 * 60 + alrm_min * 60
# print(sleep_time)
time.sleep(sleep_time)
# print('alarm')
# win32api.MessageBox(0, 'Times Up', 'Alarm')

toaster = win10toast.ToastNotifier()
toaster.show_toast(name, description, duration=20)

print('Success')
