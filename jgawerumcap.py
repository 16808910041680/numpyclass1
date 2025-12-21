import numpy as np
import random
import time
import sys

data = [('name', 'S15'), ('class', int), ('height', float)]

student_det = [('John Doe', 5, 64.4),
('Jane Smith', 6, 49.5),
('Jim Brown', 4, 28.7)]
students = np.array (student_det, dtype=data)
print(students)
print ("Sort by height:")
print (np.sort(students, order='height'))
print ("reverse")
print (np.sort(students, order='height')[::-1])
print ("Sort by alphabetical order:")
print (np.sort(students, order='name'))
print ("Reverse alphabetical order:")
print (np.sort(students, order='name')[::-1])
print ("Completely random order!")
for i in range (50):
    random_indices = np.random.permutation(len(students))
    print (students[random_indices])
    sys.stdout.write("\033[F\033[K") 
    time.sleep(0.2)
print (students[random_indices])