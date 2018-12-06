from PIL import Image
import os




#Encodes user selected image with the message that they input
def encode(image, message):
    message_length = len(message)
    if message_length > 255:
        print("Your message is too long. 256 characters or less")
        return None

    #Creates a copy of the image to encode
    encoded_image = image.copy()

    #assigns the height and width to the size of the image
    width, height = image.size
    i = 0

    #iterates through the rows and columns of pixels and assigns the rgba values to the values found in the pixel
    #it then replaces the red pixel value with the unicode value of a single character from the message
    for row in range(height):
        for col in range(width):
            r, g, b = image.getpixel((col, row))
            if row == 0 and col == 0 and i < message_length:
                asc = message_length
            elif i <= message_length:
                c = message[i -1]
                asc = ord(c)
            else:
                asc = r
            encoded_image.putpixel((col, row), (asc, g, b))
            i += 1
    return encoded_image

def decode(image):
    width, height = image.size
    decoded_message = ""
    i = 0
    for row in range(height):
        for col in range(width):
            r, g, b = image.getpixel((col, row))

            if row == 0 and col == 0:
                length = r
            elif i <= length:
                decoded_message += chr(r)
            i += 1
    return(decoded_message)

os.chdir("C:\\Users\\dhorg\\Downloads\\Encrypted_email_screenshots")
#folder_path = input("Enter the full path of the folder containing the file that you want to hide.\nYou must use either double backslashes or forward slashes in place of backslashes")
#os.chdir(folder_path)
#Changes the working directory to that of the folder that the desired image is kept in
image_file = "Screenshot (4396).png"
#image_file = input("Enter the name of the image. Must be a png")
#if image_file[-4:] != ".png":
#    print("The file type must be .png")

image = Image.open(image_file)
if image.mode != 'RGB':
    image.convert('RGB')
#Opens the original image and converts it to RGB if it is not

original_message = input("Enter a message to be hidden in the image. Must be 256 characters or less")
if len(original_message) > 255:
    print("Message is too long! Must be 256 or less characters")

encoded_file = "enc_" + image_file
encoded_image = encode(image, original_message)
encoded_image.save(encoded_file)
decoding_image = Image.open(encoded_file)
decoded_message = decode(decoding_image)
print(decoded_message)
