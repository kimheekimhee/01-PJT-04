import sys

sys.stdin = open("_민석이의과제체크하기.txt")

# 과제를 제출한 사람을 input().split()으로 받아오고, range(총수강생) 해서 for문을 사용하고, 리스트화 해서 제출한 사람을 리스트화 하고 총수강생 - 제출한 사람 해서 sort 하면 될거같다?
# 리스트끼리 뺄수가 없었다... 생각해보니 set으로 바꿔야 되나보다 누더기 옷을 만드는 것 처럼 주먹구구 식으로 코딩을 하는 거 같아 불안하다
# 계속 set으로 푸니까 되질 않아서 다시 생각해 다른 방법으로 풀었더니 pass 되었다. 왜 안됐는지 모르겠는걸 보면 아직도 먼거같다.
# 처음엔 b가 0인 경우를 신경 안써서 그렇구나! 했는데 범위가 1 이상이라 그럴일 없었다... 왜 아래는 안되고 위는 패스였을까 풀어도 슬픈 날이다

T = int(input())


for test_case in range(1, T + 1):
    all_students = []
    result = []
    a , b = map(int , input().split())
    c = list(map(int,input().split()))
    for i in range(1 , a + 1):
        if i not in c:
            result.append(i)


    print(f'#{test_case}', *result )
    


    # for test_case in range(1, T + 1):
    # a , b = map(int , input().split())
    # c = set(map(int,input().split()))
    # for i in range(1 , a + 1):
    #     all_students.append(i)

    #     if b == 0:
    #         result.append(all_students)

    # print(f'#{test_case}', * sorted(set(all_students) - c))
    
