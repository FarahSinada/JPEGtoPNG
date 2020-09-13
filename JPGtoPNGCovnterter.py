import sys
import os   # this is used for directory path manipulation
from PIL import Image


def check_folders(folder1, folder2):
    """check whether folder 1,2 exists, if 2 doesn't, create a new one"""
    if not os.path.isdir(f'.\{current_folder}'):
        print('Folder where images are stored not found')

    if not os.path.isdir(f'.\{new_folder}'):
        # \\ to ignore special character \
        os.mkdir('.\\new')


# using sys grab first and second arguments
# enter folder names like this: folder new\
current_folder = sys.argv[1]
new_folder = sys.argv[2]

# use os to grab path, check if new\ folder exists, if not, create it
# path = os.getcwd()
# os.getcwd() gets full path, but if folder is in current project folder, just use .\ for path

check_folders(current_folder, new_folder)

try:
    path_cur = os.path.join('.\\', current_folder)
    path_new = os.path.join(os.getcwd(), new_folder)

    # to access directory use scandir
    with os.scandir(path_cur) as my_folder:
        # loop through pokedex folder for images
        # entry is object of type nt.DirEntry
        for entry in my_folder:
            # is_file() returns true only if path points to file not directory
            if entry.name.endswith(".jpg") and entry.is_file():
                print(entry.name, entry.path)
                # print(type(entry))
                # entry.path is of type str
                img = Image.open(entry.path)

                # print(path_new)

                # convert to png, save to the new folder
                with os.scandir(path_new) as png_folder:
                    # entry.name includes the file ext, splitext splits pathname into a pair(root,ext)
                    new_img = img.save(f'.\\new\\{os.path.splitext(entry.name)[0]}.png')

except PermissionError as err:
    print('Cannot access folder as file')
    print(err)

except FileNotFoundError as err2:
    print('File cannot be found')
    print(err2)
    pass




# with open(f'.\{current_folder}',mode='r') as my_folder:
#     test = Image.open('.\Pikachu.jpg')

#     img.show()

# FileNotFoundError: [Errno 2] No such file or directory: usually when trying to open directory
# can be solved by using with os.scandir(folder path) as my_folder:
