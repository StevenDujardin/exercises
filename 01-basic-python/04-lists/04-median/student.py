# Write your code here
def median(ns):
    ns2 = sorted(ns)
    i = len(ns)//2
    if len(ns2) % 2 == 0:
        return (ns2[i-1] + ns2[i]) / 2
    else:
        return ns2[i]
