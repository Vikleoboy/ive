from application.data_base import show_data
from application.voiceinput import keywords
import os
import subprocess
import webbrowser


sec_path = os.getcwd()
path = '\\'.join(os.getcwd().split(os.sep)[:-1]) + '\\application\\input'
got_it = False
text = show_data(path)

data = ['\\scripts\\appdata\\code', '\\scripts\\appdata\\file explorer', '\\scripts\\appdata\\chrome',
        '\\scripts\\appdata\\yt']
data = ['\\'.join(sec_path.split(os.sep)) + x for x in data]

something = [text.split()[text.split().index(x) + 1] for x in text.split() if x == 'open']

print(text, something)
for i in data:  # looping through data
    key = show_data(i).split(',')
    print(text, show_data(i).split(',')[:-1])
    if keywords(text, show_data(i).split(',')[:-1]):  # seeing if keyword match what we want
        got_it = True
        print('ya done')
        subprocess.call(key[-1], shell=True)

        if 'http' in key[-1].split(':') or 'https' in key[-1].split(':'):
            webbrowser.open(key[-1])
    else:
        got_it = False

try:
    if not got_it:
        subprocess.call(something, shell=True)

except:
    print('not gone open')
