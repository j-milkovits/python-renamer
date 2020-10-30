from pathlib import Path
import os

# Initialize variables
absPath = str(Path().absolute())
filelist = os.listdir(absPath)
count = 1

# Read input variables
prefix = input("Input prefix:")
postfix = input("Input postfix:")
print("y: Create folders and move them")
print("s: Folders are already there, move files")
print("n: Only rename files")
createFolders = input("Create folders?(y/s/n)")

for filename in filelist:
    tempPath = absPath + "\\" + filename
    
    # If file is the python program, skip it
    if filename == "rename.py":
        continue

    # If file is a directory, skip it
    if not(os.path.isfile(tempPath)):
        continue

    # ALways get a two digit number
    if count < 10:
        number = str(0) + str(count)
    else:
        number = str(count)

    # Create folders and move files
    if createFolders == "y":
        os.mkdir(absPath + "\\" + prefix + number)
        dst = absPath + "\\" + prefix + number + "\\" + prefix + number + postfix
    # Folders are already there and files should be moved
    elif createFolders == "s":
        dst = absPath + "\\" + prefix + number + "\\" + prefix + number + postfix
    # Only rename files
    else:
        dst = absPath + "\\" + prefix + number + postfix

    # Rename / Move the file
    os.rename(tempPath, dst)

    count = count + 1