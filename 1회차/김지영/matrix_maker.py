from pprint import pprint
n,m = map(int,input().split())
result = []
for _ in range(n):
    temp = list(map(int,input().split()))
    result.append(temp)

pprint(result)
