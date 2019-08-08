import numpy as np
from scipy import stats
n=int(input())
arr = list(map(int,input().split()))
mean   = round(np.mean(arr),1)
median = round(np.median(arr),1)
mode   = round(stats.mode(arr)[0][0],0)
std    = round(np.std(arr),1)
low    = round(np.mean(arr)-1.960*(np.std(arr)/(n**0.5)),1)
upp    = round(np.mean(arr)+1.960*(np.std(arr)/(n**0.5)),1)

print(mean)
print(median)
print(mode)
print(std)
print(low,upp)
