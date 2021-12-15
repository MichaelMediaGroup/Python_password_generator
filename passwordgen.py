
#import needed
import random

#welcome user
print("Welcome to a password generator!")

#List of things that will be in passowrd
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

#get num of passwords
number = input("number of passwords")
number = int(number)

#get lenght
length = input("password lenght")
length = int(length)

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)


k=input("press to close")
