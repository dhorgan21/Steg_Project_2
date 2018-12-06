import os

def contains_png(fold_path):
    png_present = False
    folder = fold_path
    for file in os.listdir(folder):
        if file.endswith(".png"):
            png_present = True
    if png_present == True and os.path.isdir(folder) == True:
        return folder
    else:
        folder = input("Enter folder path3")
        while not os.path.isdir(folder):
            folder = input("Enter folder path4")
            return None





i = 0
folder_path = input("Enter folder path1")
while not os.path.isdir(folder_path):
    folder_path = input("Enter folder path2")
while contains_png(folder_path) == None:
    i += 1
print(contains_png(folder_path))


