import sys

sys.stdin = open("_암호생성기.txt")

# 10개의 테스트케이스 처리
for i in range(1, 11):

    # 테스트케이스 번호 담는 변수 선언
    test_case = int(input())

    # 8개 숫자 담을 리스트 선언
    cipher_list = list(map(int, input().split()))

    # 리스트 내 0이 없을 때 까지 반복
    while 0 not in cipher_list:
        # 1사이클 돌리기
        for j in range(1, 6):
            # 만약 이동하는 숫자가 0보다 작으면 0을 담고 for문 탈출
            if cipher_list[0] - j <= 0:
                tmp = 0
                cipher_list.pop(0)
                cipher_list.append(tmp)
                break
            # 이동하는 숫자가 0보다 크면 계속 사이클 돌리기
            else:
                tmp = cipher_list[0] - j
                cipher_list.pop(0)
                cipher_list.append(tmp)
    
    # 결과값 출력
    print(f"#{i}", end=' ')
    for k in cipher_list:
        print(k, end=' ')
    print("")