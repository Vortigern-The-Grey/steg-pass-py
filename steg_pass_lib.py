# import external libraries
from steganon import Image, LSB_WS


def encrypt(seed, message, cover):
    """
    Takes a seed (string), a message (string), and file name of png (string), and encrypts the message in the image using the string.
    It then writes this to a file named {cover}-secret.png
    """
    cover_image = Image.open(f"{cover}.png")  # Open targeted Image
    seed = bytes(seed, "utf-8")
    lsb_ws = LSB_WS(
        cover_image, seed
    )  # HACK: This code throws an lsp error, ignore as false positive.

    message = bytes(message, "utf-8")  # Convert message to be hidden into bytes
    lsb_ws.hide(message)  # Write secret message to image pixels
    cover_image.save(f"{cover}-secret.png")  # Save altered image with secret data


def decrypt(image, seed):
    """
    Opens a png file and uses a supplied seed to extract the hidden message.
    """
    target_image = Image.open(f"{image}.png")  # Open Image with hidden data
    lsb_ws = LSB_WS(
        target_image, seed
    )  # HACK: This code throws an lsp error, ignore as false positive.

    output_bytes = lsb_ws.extract()
    output = output_bytes.decode("utf-8")
    return output
