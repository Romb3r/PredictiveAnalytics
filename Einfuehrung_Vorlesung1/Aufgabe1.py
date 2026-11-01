import numpy as np

list = [1, 2.2, "drei"]
np_list = np.array(list, dtype=object)              #dtype=object damit die Typen erhalten bleiben, jedes element würde sonst zu typ string werden

for i, elem in enumerate(np_list):        
    print(f"Index: {i} | Typ: {type(elem)} | Wert: {elem}")

