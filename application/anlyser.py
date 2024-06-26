from voiceinput import keywords, talk  # importing stuff for checking keywords , and get mic input
import subprocess  # to tun scripts
import os  # splitting list
from data_base import show_data  # to show data

data = ['data\\shutdown',
        'data\\data',
        'data\\random_genrator',
        'data\\app',
        'data\\clock']  # location of scripts open i want to run for certain words (NOTE : name of data,py file need to same )

# data processing here to dir so i can organise the data properly
data = list(map(lambda x: {f'{x.split(os.sep)[-1]}': show_data(x).split(',')}, data))

# this are location of the scripts which will see the condition
py_data = [
    ['scripts\\bool', 'say_hi()', 'scripts\\tryshit.py']]  # taking py file name and func name which will return bool

# debugging stuff
print(py_data)
print(data)

# input from mic which will be a fuco
real_text = open(r'input.txt', 'w')
real_text.write(talk())
real_text.close()

text = show_data('input')
# this is the place where processing happens

# first we will se if we want to run a scripts on the basic of keywords

for i in data:  # looping through data
    name = ''  # var
    for m in i:  # going through data
        name = m

    if keywords(text, i[m]):  # seeing if keyword match what we want
        subprocess.call(f'python scripts\\{m + ".py"}', shell=True)

# here we see if we want to run py file with certain py file , which will take a boolean to see if it wants to run it
for i in py_data:  # lopping through data
    exec(f'from {i[0].split(os.sep)[0]}.{i[0].split(os.sep)[-1]} import {i[1][:-2]} ')  # importing script that we want to see the bool
    func = eval(f'{i[1]}')

    if func:
        subprocess.call(f'python {i[-1]}', shell=True)

