# Ezrhael R. Sicat
# BSCpE 1-5
# 04/02/2023
# Program 2 - Decryption

import colorama
import pyfiglet

print (colorama.Fore.GREEN + "=" * 100)
font = pyfiglet.figlet_format("Code Decryption", font = "big" )
print(colorama.Fore.BLUE + font)

# Introduction to the program
print (colorama.Fore.GREEN + "=" * 100)
Name=input(colorama.Fore.BLUE + "Enter your username: ")
print (colorama.Fore.GREEN + "=" * 100)
print (colorama.Fore.YELLOW + "Hello!", Name,)
print ("Today, we are going to decrypt a code")

moredata = True
while moredata:

    # Ask the user for input 
    print (colorama.Fore.GREEN + "=" * 100)
    user_text = input(colorama.Fore.WHITE + "Input your message to decrypt: ")

    # Time Delay
    print (colorama.Fore.GREEN + "=" * 100)
    print (colorama.Fore.WHITE + "Processing...")
    import time
    time.sleep(5)

    # Replace the character to its corresponding value
    decrypted_string = user_text.replace("*", "a").replace("&", "e").replace("#", "i").replace("+", "o").replace("!", "u")

    # Print Output
    print (colorama.Fore.GREEN + "=" * 100)
    print (colorama.Fore.RED + "Original Message : ", colorama.Fore.WHITE + user_text)
    print (colorama.Fore.RED + "Decrypted Message: ", colorama.Fore.WHITE + decrypted_string)
    print (colorama.Fore.GREEN + "=" * 100)

    while True:
        repeat = input(colorama.Fore.WHITE + "Do you want to try again? (Yes/No): ")
        if repeat.lower() == "yes":
            break
        elif repeat.lower() == "no":
            moredata = False
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

print (colorama.Fore.GREEN + "=" * 100)
print (colorama.Fore.YELLOW + "Thank you for using this program.")
print (colorama.Fore.GREEN + "=" * 100)
