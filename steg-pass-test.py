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


test_seed = "seed_1"
test_message = input(">>> ")
test_image = "test"
result_image = "test-secret"

encrypt(test_seed, test_message, test_image)
output_message = decrypt(result_image, test_seed)
print(f"{output_message} decrypted from {result_image}.png")
