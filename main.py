import os
from time import sleep

print('Current Directory: ' + os.path.expanduser('~'))
wanted_directory = input('Enter Folder Path (relative to current directory): ')
folder = os.path.expanduser('~') + wanted_directory + '/'
print('This is your working folder: ' + folder)

event = input('Enter New File Names:')
count = 1



for file_name in os.listdir(folder):
    
    split_path = os.path.splitext(str(file_name))
    file_extensions = str(split_path[1])
    source = folder + file_name
    destination = folder + str(event) + '_' + str(count) + file_extensions

    os.rename(source, destination)
    count += 1

sleep(1)
print('\nAll your files have been renamed')
print('Your new names are: ' + str(os.listdir(folder)))