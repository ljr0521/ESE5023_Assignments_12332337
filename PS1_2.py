import numpy as np
M1 = np.array(np.random.randint(0,51,50)).reshape(5,10)
M2 = np.array(np.random.randint(0,51,50)).reshape(10,5)
print(M1)
print(M2)

def Matrix_multip(a1, a2):
    arr = np.zeros((5,5))
    for i in range(5):
        for j in range(10):
            for k in range(5):
                arr[i,k] += a1[i,j] * a2[j,k]
    print(arr)
Matrix_multip(M1, M2)