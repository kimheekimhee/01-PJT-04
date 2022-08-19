import sys

sys.stdin = open("_암호생성기.txt")
'''
접근방법
 
끝의 값을 바꿔주고 인덱스를 하나씩 당겨야해서 0번은 계산한다음 zero 변수에 담고
1번부터 7번까지 리스틀 자르고 zero 를 마지막에 append 
'''
tc = 10

for _ in range(tc):
    list_ = []
    k = int(input())
    list_ = list(map(int, input().split()))
    cnt = 0

    while True:
            
        for i in range(1,6):
            zero = list_[0]-i
            temp = list_[1:]
            temp.append(zero)
            list_ = temp
            if list_[7] <= 0:
                list_[7] = 0
                cnt +=1
                break 

        if cnt:
            break
        
    print(f'#{k}', end = ' ')
    for i in temp:
        print(i, end = ' ')
    print()                      