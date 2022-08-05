# import sys

# sys.stdin = open("_암호생성기.txt")

# 8개의 숫자를 입력 받는다.
# 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 
# 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 
# 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 
# 그 다음 수는 4, 그 다음 수는 5를 감소한다.
# 1~5까지 감소시킨것이 1사이클, 숫자가 작아직때 0보다 작아지는경우 0으로 유지
# 프로그램은 종료된다.

for t in range(10):
    N = int(input())
    code = list(map(int, input().split()))

    i = 1
    while True:
        a = code.pop(0)-i # 코드 리스트의 첫번째 요소를 가져와 빼내고 -i
        if a <= 0: # a가 0보다 작거나 같아지면 
            code.append(0) # 리스트의 끝에 0을 추가
            break # 반복종료
        code.append(a) # 리스트에 연산한 a값 추가
        i += 1
        if i > 5: # i가 증가하다가 5를 넘어가면
            i = 1 # 1로 초기화
    print("#{} {} {} {} {} {} {} {} {}".format(N, *code))