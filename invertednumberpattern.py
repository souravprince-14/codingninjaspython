n=int(input())
i=1
k=n
while i<=n:
    j=1
    while (j>=1 and j<=(n+1-i)):
        print(k,end='')
        j+=1
    print()
    k-=1
    i+=1