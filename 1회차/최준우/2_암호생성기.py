import sys

sys.stdin = open("_암호생성기.txt")

T = 10 # 총 테스트케이스 10개

for test_case in range(T):
    t_num = int(input()) # 몇번째 케이스인지 저장할 변수
    data_list = list(map(int, input().split())) # 줄마다 리스트로 저장
    
    cnt = 0
    while data_list[-1] != 0:
        cnt += 1
        if cnt > 5: # 감소시킬 cnt변수 5초과면 다시 1로 만들어주기
            cnt -= 5
        data_list[0] = data_list[0] - cnt # 0번째 인덱스 수 - cnt
        if data_list[0] <= 0: # 만약 0이하면 0으로 고정
            data_list[0] = 0

        data_list.append(data_list[0]) # 뒤에 붙여주고
        data_list.pop(0) # 지워준다
    print(f'#{t_num}', end = ' ') # 출력 형식
    for i in data_list:
        print(i, end = ' ') # 출력
    print()