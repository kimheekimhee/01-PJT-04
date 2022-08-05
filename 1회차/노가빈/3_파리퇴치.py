# tc = int(input())
# for x in range(tc):
n,m = map(int,input().split(' '))
nlist = []
for i in range(n):
    nlist.append(list(map(int,input().split(' '))))

numlist = []
for i in range(n-m+1):
    for j in range(n-m+1):
        num = nlist[j][i]+nlist[j][i+1]+nlist[j+1][i]+nlist[j+1][i+1]
        numlist.append(num)
print(f'#{1}',max(numlist))