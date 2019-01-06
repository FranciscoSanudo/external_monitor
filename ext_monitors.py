#!/usr/bin/python

import os

##This section is for brightness adjustments in external monitors

ext_monitor = ''
while ext_monitor not in ('one', 'two'):
    print('Please type how many monitors are connected:')
    ext_monitor = input()

print('Entry: ' + ext_monitor)

print('Brightnes level:')
bri_monitor = float(input())/10
bri_exec = bri_monitor

if ext_monitor == 'one':
    sc1_monitor = "xrandr --output DP2-3 --brightness " + str(bri_monitor)
    os.system(sc1_monitor)
else:
    sc2_monitor = "xrandr --output DP2-2 --brightness " + str(bri_monitor)
    sc3_monitor = "xrandr --output DP2-3 --brightness " + str(bri_monitor)
    os.system(sc2_monitor)
    os.system(sc3_monitor)

print('Is it okay? (y/n)')

bri_loop = input()
while bri_loop not in ('y'):
    bri_monitor2 = float(input())/10
    sc2_monitor = "xrandr --output DP2-2 --brightness " + str(bri_monitor2)
    sc3_monitor = "xrandr --output DP2-3 --brightness " + str(bri_monitor2)
    os.system(sc2_monitor)
    os.system(sc3_monitor)
