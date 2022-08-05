import sys

sys.stdin = open("sample_input.txt")

 # [1,2,3,4,5]
list1 = []
list2 = []

t = int(input()) # tc 받음

for tc in range(1, t+1): # 1~t 기간 횟수까지 반복
    n, m = map(int, input().split()) # 5, 3 입력

    a = list(map(int, input().split())) # 2, 5, 3 입력

    result = [] # 결과 값 담을 빈 리스트 생성

    for i in range(1, n+1): # 1~5 반복
        if i not in a: # 1이 a 리스트에 포함되어있지 않다면 
            result.append(i) # 결과 리스트에 출력 


    
    print(f"#{tc}", *result)

    






