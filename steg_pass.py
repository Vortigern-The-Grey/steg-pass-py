"""
steg-pass-py - A WIP cli password manager that stores your secrets in images!
steg-pass-py utilises steganon heavily. In many ways, it's a steganon wrapper.

By Vortigern
"""

from steg_pass_lib import encrypt, decrypt


def main():
    menu_loop = True
    while menu_loop is True:
        seed_loop = True
        message_loop = True
        file_loop = True

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

        elif menu_choice == 2:
            prev_seed = input("Enter the seed previously used to hide the data >>>")
            prev_file = input(
                "Enter the name of the file in which the data is hidden (Must be png and in same dir) >>>"
            )
            print("Decrypting data now...")
            prev_message = decrypt(prev_file, prev_seed)
            print("Data:")
            print(prev_message)

        elif menu_choice == 3:
            menu_loop = False


if __name__ == "__main__":
    main()
