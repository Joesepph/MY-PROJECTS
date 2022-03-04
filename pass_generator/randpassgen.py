import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

string = lower + upper + numbers + symbols

print("How long do you want password to be? (give a number)")
length = int(input())

password = "".join(random.sample(string,length))

print("\nYour new password is: " + password)


