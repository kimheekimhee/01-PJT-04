import sys

sys.stdin = open("_민석이의과제체크하기.txt")

t = int(input())

 #제출하지 않은 학생들의 리스트

for j in range(t) : #test case만큼 반복
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    not_h = []  #빈 리스트를 안에 넣어야함 (계속 바깥에 빼놔서 14, 1412357 이렇게 나옴)

    for i in range(1, n+1) : #0을 넣으면 0번도 포함되므로 1부터 n+1까지
        if i not in num :  #변수가 num 리스트에 없다면
            not_h.append(i) #not_h 리스트에 값 추가
    
    print(f'#{j+1}', *not_h) # *리스트이름 을 통해 리스트 요소만 출력
  