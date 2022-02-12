import time
import os
from random import randint
from application.voice import say
from application.data_base import show_data

# print(time.ctime())
# path to this file to get the path to input.txt
path = '\\'.join(os.getcwd().split(os.sep)[:-1]) + '\\application\\input'
print(path)
txt = show_data(path)

text = txt.split()

real_time = 0
for i in text:
    mode = ''

    try:
        num = int(i)

        unit = text[text.index(i) + 1]
        if unit == 'minutes' or unit == 'minute':
            num *= 60
            real_time += num
        elif unit == 'hours' or unit == 'hour':
            num *= 3600
            real_time += num
        elif unit == 'seconds' or unit == 'second':
            real_time += num
    except:
        pass

saying = show_data('scripts//database//clock//done').split(',')
say(saying[randint(0,abs(len(saying)-1))])


time.sleep(real_time)

saying = show_data('scripts//database//clock//timeup').split(',')
say(saying[randint(0,abs(len(saying)-1))])

print(real_time,path )