def fibComprhension(n):
    series=[1,1]
    [series.append(series[k-1]+series[k-2]) for k in range(2,n)]
    return series[-1]

print (fibComprhension(36))