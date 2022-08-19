import sys

sys.stdin = open("민석이.txt")

T = int(input())

for tc in range(1,T+1):
    n, k = map(int,input().split())
    k_num = list(map(int,input().split())) #제출한사람 리스트로 변환해서 받기
    people = []  #제출안한사람넣을 리스트

    for i in range(1,n+1): #전체사람중에
        if i not in k_num: #제출한사람리스트에 없으면
            people.append(i) #제출안한사람리스트에 추가하기
    print(f'#{tc}',*people) #리시트를 문자열모양으로 바ㅏ꿔서 추출(*)
