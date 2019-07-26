# Calculating the average of all grades and the avg of grades in each column and row

import numpy as np

grades = np.random.randint(60, 101, 12).reshape(3, 4)

print(grades)
print('\n')
print(grades.mean())
print(grades.mean(axis=0))
print(grades.mean(axis=1))
