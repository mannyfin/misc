import numpy as np
# import matplotlib.pyplot as plt

def f(n,s):
    if n == 1:
        yield (s,)
    else:
        for i in range(s + 1):
            for j in f(n - 1,s - i):
                yield (i,) + j

numba = 5
L = list(f(numba,100))
print('total permutations:', len(L))

# First and last 10 of list
# for i in L[:10] + L[-10:]:
#     print(i)

L = np.array(L, dtype='int')
np.savetxt('L_'+str(numba)+'.txt', L, delimiter=',')