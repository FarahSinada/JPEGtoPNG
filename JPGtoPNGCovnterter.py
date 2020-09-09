import sys
import os
from PIL import Image

# using sys grab first and second arguments
# enter folder names like this: folder\ new\
current_folder = sys.argv[1]
new_folder = sys.argv[2]

print(current_folder)
print(new_folder)
# use os to grab path, check if new\ folder exists, if not, create it

try:
    pass

except:
    pass

# loop through pokedex folder
# convert to png
# save to the new folder