import random
import time
import sys
key = ""
key_shuffle = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince']
print("Original list:")
print(key_shuffle)
print ("Correct Key:")
def pick_random_fruit(keys):
    key = random.choice(keys)
    return key
print(pick_random_fruit(key_shuffle))
print ("Shuffling!")

for i in range (50):
    random.shuffle(key_shuffle)
    print (key_shuffle)
    sys.stdout.write("\033[F\033[K") 
    time.sleep(0.2)


print ("Final shuffled list! Find the key!")
time.sleep (2)

sys.stdout.write("\033[F\033[K") 
input ("Tell me where is the key in the string? Number from 1 to 15:")
print("You selected:", key_shuffle[int(input()) - 1])

if input == key:
    print("Correct! You found the key:", key)
else:
    print("Wrong! The correct key was:", key)