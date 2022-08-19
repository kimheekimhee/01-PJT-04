import collections
import sys

sys.stdin = open("_암호생성기.txt")

from collections import deque #콜렉션즈에 큐가 있다. 불러오기
cnt = 0
while cnt < 10: #입력이 끝나면 탈출하는 while문이 있었던가 같은데 ???
    T = int(input())
    cnt += 1
    number = list(map(int,input().split()))
    subt = 0
    while number[7] > 0: #마지막자리에0이 나올떄까지 무한뺑이
        subt += 1 #뺼 숫자
        if subt > 5:
            subt = 1
        popnumber = number.pop(0) #pop으로 첫자리숫자를 꺼내어 연산후 append로 마지막자리에 넣어준다.
        popnumber = popnumber - subt
        if popnumber < 0 :
            popnumber = 0            
        number.append(popnumber)

    print(f'#{T}',*number)