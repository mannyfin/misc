import numpy as np
import matplotlib.pyplot as plt

def f(n,s):
    if n == 1:
        yield (s,)
    else:
        for i in range(s + 1):
            for j in f(n - 1,s - i):
                yield (i,) + j

numba = 10
L = list(f(numba,100))
print('total permutations:', len(L))

# First and last 10 of list
# for i in L[:10] + L[-10:]:
#     print(i)

L = np.array(L, dtype='int')
np.savetxt('L_'+str(numba)+'.txt', L, delimiter=',')
# print(L)
n_rows = np.shape(L)[0]
compare = L*np.array([1, 2, 3])
# compare[1]
cp = np.zeros(np.shape(L))
res = np.zeros((n_rows,numba))
less_res = np.zeros((n_rows,numba))
for y in range(n_rows): #for row to pick
    for i in range(n_rows): # for row to compare
        for idx, value in enumerate(L[i]): # for idx, value in row of comparison
            if L[i][idx] < L[y][idx]:
                if compare[i][idx] < L[y][idx]:
                    cp[i][idx] = True
                    # print('True')
                else:
                    # cp[0][idx] = False
                    cp[i][idx] = False
    # res[y] = len(np.where(cp.sum(axis=1) > 1)[0])
    for num in np.arange(numba):
        res[y][num] = len(np.where(cp.sum(axis=1) > num)[0])
        less_res[y][num] = len(np.where(cp.sum(axis=1) == num)[0])
    cp = np.zeros(np.shape(L)) # reinitialize cp for next iteration
location = np.where(res[:, numba-1] == res[:, numba-1].max())[0][0]
np.savetxt('results'+str(numba)+'.txt', res, delimiter=',')
print(L[location])
plt.plot(res[:, 1])
print('hi')
print(res)