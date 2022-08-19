# deque하면 정렬해버리는구나..queue사용합시다.
# 8자리 숫자
# 첫번째 수에서 1...5를 뺀 뒤 맨 뒤로 보내는 사이클
# 만약 어떤 수가 0이 되면 그 수를 뒤로 보낸 뒤 프로그램 종료.

import sys
sys.stdin = open("_암호생성기.txt")

# pw_num = [50 ,56 ,50 ,53 ,58 ,51 ,51, 51]
# pw_num[0] = pw_num[0] - 10        
# pw_num.append(pw_num.pop(0))
# print(pw_num)
# 이게 되는데...
for t in range(10):
    test_case = int(input())
    pw_num = map(int,input().split())
    pw_num = list(pw_num)

    while True:
        # print(pw_num)
        for i in range(1,6): # 범위!!!!!!!!!!!!!!!!!!!!!!
            if pw_num[0] - i <= 0:
                pw_num[0] = 0
                pw_num.append(pw_num.pop(0))
                break
            else :
                pw_num[0] = pw_num[0] - i
                pw_num.append(pw_num.pop(0))
        # print(pw_num)
        if pw_num[-1] == 0:
            break
    pw_num = map(str,pw_num)
    result = ' '.join(pw_num)
    print(f'#{test_case}',result)