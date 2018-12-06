from PIL import Image
import os


#Takes input of a user selected image and message and outputs an image with up to 255 pixels with red channels modified to store ascii characters
def encode(image, message):
    message_length = len(message)
    if message_length > 255:
        print("The message is too long. 256 characters or less")
        return None

    #Creates a copy of the image to encode
    encoded_image = image.copy()

    #assigns the height and width to the size of the image
    width, height = image.size
    i = 0

    #iterates through the rows and columns of pixels and assigns the rgb values to the values found in the pixel
    #it then replaces the red pixel value with the unicode value of a single character from the message
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            #neccessary in order to determine the length of the message, without it, garbage characters are attached to the end of the file
            if y == 0 and x == 0 and i < message_length:
                asc = message_length
                #If it is not in the first position, then it converts the character in the i - 1 index to an ascii value
            elif i <= message_length:
                character = message[i -1]
                #The ord function is used to convert characters to their ascii values
                asc = ord(character)
                #if neither of the above conditions are met (The message is over) then the rest of the 8 bit red values of the image are kept the same
            else:
                asc = r
            #replaces the 8 bit value of the red color in the pixel in position x, y with the ascii value of the character at index i of the message
            encoded_image.putpixel((x, y), (asc, g, b))
            i += 1
    return encoded_image

#Takes the encoded image and uses the inverse function to convert ascii values to characters which are added to a string, which is then output
def decode(image):
    width, height = image.size
    decoded_msg = ""
    i = 0
    for y in range(height):
        for x in range(width):
            #assigns the 8 bit color values of a pixel at position x, y to the variables r, g, and b
            r, g, b = image.getpixel((x, y))

            if y == 0 and x == 0:
                length = r
            elif i <= length:
                #The chr() function is the inverse of ord() and converts ascii values into their corresponding characters
                decoded_msg += chr(r)
            i += 1
    return decoded_msg

#Changes the working directory to that of the folder that the desired image is kept in
folder_path = input("Enter the full path of the folder containing the file that you want to hide.\nYou must use either double backslashes or forward slashes in place of backslashes")
while not os.path.isdir(folder_path):
        print("That is not an existing folder, enter another path name")
        folder_path = input()
os.chdir(folder_path)

image_file = input("Enter the name of the image. Must be a png")
while not os.path.isfile(image_file) or image_file[-4:] != ".png":
    print("That is not an existing .png file, enter another file name")
    image_file = input()



image = Image.open(image_file)
if image.mode != 'RGB':
    image = image.convert('RGB')
#Opens the original image and converts it to RGB if it is not


original_message = input("Enter a message to be hidden in the image. Must be 256 characters or less")
while len(original_message) > 255:
    print("Message is too long! Must be 256 or less characters")
    original_message = input("Enter a message to be hidden in the image. Must be 256 characters or less")

while len(original_message) == 0:
    print("You didn't write a message...........")
    original_message = input("Enter a message to be hidden in the image. Must be 256 characters or less")



#Calls the encode function to encode the original image and message specified by the user
encoded_image = encode(image, original_message)
#Creates a new string with the name of the original file preceded by the word encoded
encoded_file = "encoded " + image_file
#Saves the encoded image with the name of the newly made string
encoded_image.save(encoded_file)
#Opens the encoded image file and stores the image in a new variable to be used for decoding
decoding_image = Image.open(encoded_file)
#Sets the variable decoded message to the output of the decode function
decoded_message = decode(decoding_image)
#opens the original image
os.startfile(image_file)
#opens the encoded image
os.startfile(encoded_file)
#Prints the message stored in the encoded image
print(decoded_message)


