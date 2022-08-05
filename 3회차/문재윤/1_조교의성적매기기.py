import sys

sys.stdin = open("_조교의성적매기기.txt")
n = int(input())
for j in range(1,n+1):
    a, b = map(int,input().split())
    list_ = []
    for i in range(a):
        y, x ,z = map(int,input().split())
        score = 35*y +45*x + 20*z
        list_ += str(score).split()
    score = list_[b-1]
    print(score)
   
    print(len(list_))
    list_ = list(map(int,list_))
    list_.sort()
    print(list_)

    coun = 0
    for i in list_:
        coun += 1
        if score == i:
            break
    print(coun)
    print(f'#{j}',end=' ')
    per = a/10
    if coun >= a + 1 - 1*per :
        print('A+')
    elif coun >= a +1 - 2*per:
        print('A0')
    elif coun >= a + 1- 3*per:
        print('A-')
    elif coun >= a + 1- 4*per:
        print('B+')
    elif coun >= a + 1- 5*per:
        print('B0')
    elif coun >= a + 1- 6*per:
        print('B-')
    elif coun >= a + 1- 7*per:
        print('C+')
    elif coun >= a + 1- 8*per:
        print('C0')
    elif coun >= a + 1- 9*per:
        print('C-')
    else:
        print('D0')
    