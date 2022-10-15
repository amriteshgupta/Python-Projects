a=[9,5,7,1,90,3,6,13,11]
print("Given list is[9,5,7,1,90,3,6,13,11]")
l=len(a)
for i in range(0,l):
    for j in range(0,l-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print()
print(a)
