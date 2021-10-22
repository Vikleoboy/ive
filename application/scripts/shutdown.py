import time # importing time module
# import sys
# sys.path.append('../')
from application.voice import say
say('computer is gone shutdown in ')
print('computer is gone shutdown in ')

time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
print('shutdown')
# subprocess.call('/sbin/shutdown -r now',shell=True)