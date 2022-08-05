import sys

sys.stdin = open("_암호생성기.txt")

def pass_(p_list): # 좀 더 깔끔하게 진행하기 위해서 함수를 만든다.
    while True:    
        for i in range(1, 6): #아래 append까지의 작업을 5번 반복한 것이 1사이클
            n = p_list.pop(0) 
            p_list.append(n - i)
            if p_list[-1] <= 0: #리스트의 맨 끝의 숫자가 0이하인 경우
                p_list[-1] = 0 # 숫자를 0으로 바꾼다.
                return p_list

for _ in range(1, 11):
    t = int(input())
    p = list(map(int, input().split()))
    answer = pass_(p)
    
    print(f'#{t}', *answer)