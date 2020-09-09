#created by banti Narvariya
#This is a password generater


import string
import random

# s1 is list of digits

s1 = string.digits

# s2 is list of uppercse letters

s2 = string.ascii_uppercase

# s3 is list of lowercase letters

s3 = string.ascii_lowercase

# s4 is list of special charecters

s4 = string.punctuation

# User input for length of password
passlen = int(input("Enter the size of password\n"))

# excliding all the lists in ls

ls = []  
ls.extend(s1)
ls.extend(s2)
ls.extend(s3)
ls.extend(s4)

# Shuffling ls and printing it

random.shuffle(ls)
print("The password generated is ", end="➡️ ")

print("".join(ls[0:passlen]))
print("IF YOU LIKE IT PLEASE GIVE ME STAR ⭐⭐")

  
