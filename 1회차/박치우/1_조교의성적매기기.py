import sys

sys.stdin = open("_조교의성적매기기.txt")
dic = {0.1:'A+', 0.2:'A0', 0.3:'A-',0.4:'B+',0.5:'B0',0.6:'B-',0.7:'C+',0.8:'C0',0.9:'C-',1:'D0'}
test_case = int(input())
for i in range(test_case):
    member ,k = map(int,input().split())
    rank = []
    for j in range(1,1+member):
        mid, last, hw = map(int,input().split())
        rank.append(mid * 0.35 + last * 0.45 + hw * 0.2)
        if j == k:
            k = mid * 0.35 + last * 0.45 + hw * 0.2
    rank.sort(reverse=True)
    print(dic[round(rank.index(k)/len(rank),1)])



        
    



