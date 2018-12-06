#if it exists then check if it contains png
#if it does not exist then make the user input it again

import os
i = 0


def png(path):
    contains_png = False
    while os.path.isdir(path) == False:
        path = input("Enter folder3")
    for file in os.listdir(path):
        if file.endswith(".png") == True:
            return True
    return False

folder_path = input("Enter folder1")
while os.path.isdir(folder_path) == False:
    folder_path = input("Enter folder2")

for file in os.listdir(folder_path):
    if file.endswith(".png") == True:
        print("Hey it works")
        i = 1
    else:
        i = 0

while i != 1:
    if png(input("Enter a new folder")) == False:
        print("Nah nah nah")
    else:
        print("Hey your thing works")
        i = 1
