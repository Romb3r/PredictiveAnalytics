import numpy as np

random_np_array = np.random.random(20)

print(random_np_array)
print(f"Max: {random_np_array.max()}")
print(f"Min: {random_np_array.min()}")
print(f"Avg: {random_np_array.mean()}")     #Mittelwert
print(f"Std: {random_np_array.std()}")      #Standardabweichung

np_array_a = np.empty(5, dtype=float)
np_array_b = np.empty(15, dtype=float)

for i in range(20):
    if i < 5:
        np_array_a[i] = random_np_array[i]
    else:
        np_array_b[i - 5] = random_np_array[i]

#Alternativ
# A = werte[:5]
# B = werte[5:]
print(f"Array A: {np_array_a}")
print(f"Array B: {np_array_b}")