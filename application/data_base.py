# This script is for data handling stuff

def show_data(name):    # function to show things in txt file
    name = name + '.txt'
    try:
        file = open(r'{shit}'.format(shit=name), 'r')
        file_text = file.read()
        return file_text
    except:
        print('there is no such file ')
