import math
P = [15,12,8,8,7,7,7,6,5,3] 
H = [10,25,17,11,13,17,20,13,9,15]

n = len(P)

x_y = sum([p*h for (p,h) in zip(P,H)])
x = sum(P)
y = sum(H)
x_x = sum([p**2 for p in P])

slope = (n*x_y - x*y) / (n*x_x - x*x)

print(round(slope,3))
