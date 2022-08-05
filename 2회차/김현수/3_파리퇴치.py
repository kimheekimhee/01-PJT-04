import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for _ in range(T): #테이스케이스의 수를 입력 받고 그수만큼 반복할거다
    N, M = map(int,input().split()) #N:배열의 크기, M:파리체크기
    #배열을 받고. 파리채크기만큼 잘랐을떄 합을 비교하는 반복문을 만들자

    NN = [list(map(int,input().split())) for i in range(N) ]  #NN배열 생성
    #print(NN)
    sum_ = 0
    result_ = 0
    for x in range(N-(M-1)): #파리채의크기가 커지만 그만큼 반복문을 적게 실행함.
        for y in range(N-(M-1)): #전체를 훑으는 반복문 -> 파리채를 들고 전체를 훑는다
            if result_ < sum_ :
                result_ = sum_
            sum_ = 0
            for m in range(x,x+M):#파리체 함수, 주어진좌표과 파리체크기를 고려하여 작성
                for n in range(y,y+M):
                    sum_ += NN[m][n] #파리체에 걸린얘들 다 더해주기
    print(f'#{_+1} {result_}')