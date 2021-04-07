"""
Just to make sure Python is installed correctly
"""
from random import randint

message = "hello world"

for i in range(0,5):
    __temp_message = list(message)
    which_letter = randint(0, len(message) - 1)

    __temp_message[which_letter] = __temp_message[which_letter].upper()
    print("".join(__temp_message))

