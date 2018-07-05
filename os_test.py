import os
from datetime import datetime

# Show all of the Attribute and Methods
# print(dir(os))
# print(help(os.device_encoding()))

# Get the current Directory
print(os.getcwd())

path = "D:/Python/"

# Change the directory to the Path
os.chdir(path)

# print(os.getcwd())

# get All files and folder in the current working directory

# print(os.listdir())

# Create a folder on Current working directory
# folder_name = 'TestFolder'

# os.mkdir(folder_name)

# if you want to make directory few level deep the use makedirs
folder ='TestDir/SubDr/SubSubDir'
# os.mkdir(folder) # Will Fail
# os.makedirs(folder) # will Pass

# Deleting Folder user 2 Methods rmdir and removedirs
# os.rmdir('TestDir') # is fail Because Folders are few level deep
try:
    os.removedirs(folder) # will pass

except:
    pass

# Renaming

# os.rename('New Text Document.txt','test.txt')

# all the information about file
# print(os.stat('test.txt').st_size)
# print(os.stat('test.txt').st_atime)
# print(os.stat('test.txt').st_ctime)
# print(os.stat('test.txt').st_mtime)
# print(os.stat('test.txt'))

# mod_time = os.stat('test.txt').st_mtime

# print(datetime.fromtimestamp(mod_time))



# print(os.listdir())

# Traversing the Directory Tree

# for dirpath,dirnames,filenames in os.walk(path):
#     print('CurrentPath: ',dirpath)
#     print('Directories: ',dirnames)
#     print('Files: ',filenames)
#     print()

# Enviornment Variable
# print(os.environ.get('HOME'))
# print(os.environ.get('USERNAME'))
# print(os.environ.get('USERPROFILE'))

# Create a Test File in the Home Directory
file_name='test.txt'

file_path = os.path.join(os.environ.get('HOME'),file_name)

print(file_path)

# Useful Function of os.path module
# print(os.path.basename(file_path))
# print(os.path.dirname(file_path))
# print(os.path.split(file_path))

print(os.path.exists(file_path))


