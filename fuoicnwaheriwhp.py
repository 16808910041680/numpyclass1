import numpy as np
import random
import time
import sys
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
key_shuffle = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince']
print("Original list:")
print(key_shuffle)
print ("Correct Key:")
key = random.choice(key_shuffle)
print (key)
time.sleep (5)
print ("Shuffling!")
def delete_last_line():
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    sys.stdout.flush()

for i in range (50):
    random.shuffle(key_shuffle)
    print (key_shuffle) 
    time.sleep(0.2)
    delete_last_line()
    delete_last_line()


print ("Final shuffled list! Find the key!")
print (key_shuffle)
time.sleep (3)
delete_last_line()
delete_last_line()

keyguess = input ("Tell me where is the key in the string? Number from 1 to 15:")
print("You selected:", keyguess)
index = key_shuffle.index(key)
keyguess = int(keyguess)
index = int(index)
index = index + 1



if keyguess == index:
    print("Correct! You found the key in spot ", index)
else:
    print("Wrong! The correct key was in spot", index)