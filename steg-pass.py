"""
steg-pass-py - A WIP cli password manager that stores your secrets in images!
steg-pass-py utilises steganon heavily. In many ways, it's a steganon wrapper.

By Vortigern
"""

# import external libraries
from steganon import Image, LSB_WS


def encrypt(seed, message, cover):
    cover_image = Image.open(f"{cover}.png")  # Open targeted Image
    seed = bytes(seed, "utf-8")
    lsb_ws = LSB_WS(
        cover_image, seed
    )  # HACK: This code throws an lsp error, ignore as false positive.

    message = bytes(message, "utf-8")  # Convert message to be hidden into bytes
    lsb_ws.hide(message)  # Write secret message to image pixels
    cover_image.save(f"{cover}-secret.png")  # Save altered image with secret data


def decrypt(image, seed):
    target_image = Image.open(f"{image}.png")  # Open Image with hidden data
    lsb_ws = LSB_WS(
        target_image, seed
    )  # HACK: This code throws an lsp error, ignore as false positive.

    output_bytes = lsb_ws.extract()
    output = output_bytes.decode("utf-8")
    return output


menu_loop = True
seed_loop = True
message_loop = True
file_loop = True
while menu_loop is True:
    menu_choice = 0
    print("------------")
    print("steg-pass-py")
    print("------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")
    menu_choice = int(input(">>>"))
    if menu_choice < 1 or menu_choice > 3:
        print("Please enter a number between 1 - 3")
    elif menu_choice == 1:
        user_seed = input("Enter the seed to use to hide the data >>>")
        user_message = input("Enter the data to hide >>>")
        user_file = input(
            "Enter the file name of the image to hide the data in (Must be png and in same dir) >>>"
        )
        encrypt(user_seed, user_message, user_file)
    print("Please enter a seed by which to hide your data:")
    user_seed = input(">>>")
