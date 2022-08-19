# 수강생들은 1번에서 N번까지 번호가 매겨져 있고
# 어떤 번호의 사람이 제출했는지에 대한 목록
# 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력

# 첫번째 줄에 테스트 케이스의 수 T가 주어진다
# 각 테스트 케이스의 첫번째 줄에는 수강생의 수를 나타내는 정수 N과
# 과제를 제출한 사람의 수를 나타내는 정수 K가 공백으로 구분되어 주어진다
# 두번째 줄에는 과제를 제출한 사람의 번호 K개가 공백으로 구분되어 주어진다
# 같은 번호가 두 번 이상 주어지는 경우는 없다

#출력 예시
#1 1 4
#2 1 2 3 5 7

import sys
sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())
for _ in range(1, T + 1):
    n, k = map(int, input().split())
    Homework = list(map(int, input().split()))
    notHomework = []

    for i in range(1, n + 1):
        if i not in Homework:
            notHomework.append(i)
            result = ' '.join(map(str, notHomework))
    print('#{} {}'.format(_, result))