X = [15,12,8,8,7,7,7,6,5,3]
Y = [10,25,17,11,13,17,20,13,9,15]

xmean = sum(X)/len(X)
ymean = sum(Y)/len(Y)
xstd = (sum([(x-xmean)**2 for x in X])/len(X))**0.5
ystd = (sum([(y-ymean)**2 for y in Y])/len(Y))**0.5

cov = sum([(X[i]-xmean)*(Y[i]-ymean) for i in range(len(X))])/len(X)
print(round(cov/(xstd*ystd), 3))
