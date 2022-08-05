
# aplha_score = {}
# m_score, e_score, h_work = map(int, input().split())
# aplha_score[1] = ((m_score*0.35)+(e_score*0.45)+(h_work*0.2))
# print(aplha_score)


# se_code = list(map(int, input().split()))
# while True:
#     for i in range(1,6):
#         # print(i)
#         a = se_code.pop(0)
#         # print(a)
#         if a-i > 0:
#             se_code.append(a-i)
#         else:
#             se_code.append(0)
#             break
#     if 0 in se_code:
#         print(se_code)
#         break


import sys

sys.stdin = open("_암호생성기.txt")

# 8개 숫자 => 1번수-1하여 맨뒤로 => 1번수-2하여 맨뒤로 => ...=> 1번수-5 맨뒤로  1싸이클
# 감소후 0이되면 종료, 현재 8자리수가 암호문 !!제약(암호는 모두 한 자리 숫자)
# 출력:#t 암호문값 출력, 공백으로

t = 10
for i in range(1, t+1):
    test_case = int(input())
    se_code = list(map(int, input().split()))
    while 0 not in se_code:
        for i in range(1,6):
            a = se_code.pop(0)
            if (a-i) > 0:
                se_code.append(a-i)
            else:
                se_code.append(0)
                break
        
    print('#',test_case, *se_code)
