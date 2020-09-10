import sys
import os
from PIL import Image


def check_folders(folder1, folder2):
    """check whether folder 1,2 exists, if 2 doesn't, create a new one"""
    if not os.path.isdir(f'.\{current_folder}'):
        print('Folder where images are stored not found')

    if not os.path.isdir(f'.\{new_folder}'):
        os.mkdir('.\\new')


# using sys grab first and second arguments
# enter folder names like this: folder\ new\
current_folder = sys.argv[1]
new_folder = sys.argv[2]

# use os to grab path, check if new\ folder exists, if not, create it
# path = os.getcwd()
# os.getcwd() gets full path, but if folder is in current project folder, just use .\ for path

check_folders(current_folder, new_folder)

try:
    pass

except:
    pass

with open(f'.{current_folder}',mode='r') as my_folder:
    test = Image.open('.\Pikachu.jpg')

# loop through pokedex folder
# for images in current_folder:
#
#     img = images.open(f'.\{current_folder}.jpg')
#     img.show()

# convert to png
# save to the new folder
