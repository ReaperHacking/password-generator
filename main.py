#Random Password Generator!
import random

regenerate = 'Y'

while regenerate == 'Y':
    print("Random Password Generator!\n")

    chars = "abcdefghjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().;:<>?/\+=-`~{}[]'1234567890"
    num = int(input("Amount of passwords: "))
    len = int(input("Length of passwords: "))

    print("Here are your passwords: \n")

#Loops through chars sequence and adds chars to newely declared 'password' variable.
    for passwords in range(num):
        passwords = ''
        for char in range(len):
            passwords += random.choice(chars)
        print(passwords)

    regenerate = input("Do you want to regenerate more passwords? (Y/N): ").upper()
    if regenerate == 'N':
        break











