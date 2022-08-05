
# 8자리 숫자
# 첫번째 수에서 1...5를 뺀 뒤 맨 뒤로 보내는 사이클
# 만약 어떤 수가 0이 되면 그 수를 뒤로 보낸 뒤 프로그램 종료.

# import sys
# sys.stdin = open("_암호생성기.txt")
# test_case = int(input())
# pw_num = list(map(int,input().split()))
test_case = 1
pw_num = [9550 ,9556 ,9550 ,9553 ,9558 ,9551 ,9551, 9551]

while pw_num[-1] != 0:
    for i in range(1,5):
        if pw_num[0] - i < 0:
            pw_num[0] = 0
            pw_num.append(pw_num[0])
            del pw_num[0]
            break
        pw_num[0] = pw_num[0] - i
        pw_num.append(pw_num[0])
        del pw_num[0]
        # 위치가 안바뀝니다..ㅠ

    print(pw_num)
        
# result = pw_num

# print(f'#{test_case} ',result)