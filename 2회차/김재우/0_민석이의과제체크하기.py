import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())            

for tc in range(1, T + 1):  
    C, N = map(int, input().split())            
    clear_list = list(map(int, input().split()))
    my_list = []                                    # 클리어 하지 못한 과제가 적혀지는 리스트
    for i in range(1, C+1):                         # 과제 번호를 전부 불러온다
        if i not in clear_list:                     # 만약 그 과제 번호가 clear_list에 없다면!               
            my_list.append(i)                       # my_list에 append (임시)

    print(f'#{tc}', end = ' ')                      # 출력부분. 
    print(*my_list)
