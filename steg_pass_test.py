"""
steg-pass-py - A WIP cli password manager that stores your secrets in images!
steg-pass-py utilises steganon heavily. In many ways, it's a steganon wrapper.

By Vortigern
"""

from steg_pass_lib import encrypt, decrypt


test_seed = "seed_1"
test_message = input(">>> ")
test_image = "test"
result_image = "test-secret"

encrypt(test_seed, test_message, test_image)
output_message = decrypt(result_image, test_seed)
print(f"{output_message} decrypted from {result_image}.png")
