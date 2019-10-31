
import numpy as np

for i in range(1000):
    with open("data.txt", "a") as f:
        data = np.random.randint(1, 10, size=(10))
        for ele in data:
            ele = str(ele) + " "
            f.write(ele)
        f.write("\n")

