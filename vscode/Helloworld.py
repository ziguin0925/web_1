import sys
input = sys.stdin.readline
i = int(input().rstrip())

for _ in range(i):
    k=0
    a = input().rstrip()
    for x in range(len(a)):
        if a[x]=='(':
            k+=1
        else:
            k-=1
            if k<0:
                print('NO')
                break
    if k==0:
        print('Yes')
    elif k>0:
        print('No')
    else:
        print('No')