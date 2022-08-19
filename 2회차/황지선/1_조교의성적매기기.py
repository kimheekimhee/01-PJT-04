# 테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.
# 총점 = 중간 35% + 기말 45% + 과제 20%

import copy

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
T = int(input())

for t in range(1, T+1):
    # 테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K 가 주어진다.
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    for x in range(N):
        # 총점 리스트(등수 안 먹인 것!)
        matrix[x] = matrix[x][0] * 0.35 + matrix[x][1] * 0.45 + matrix[x][2] * 0.2

    # 총점 리스트 만들어서 소트한 다음에 저장해두고
    sum_list = sorted(copy.deepcopy(matrix))
    sum_list.reverse()

    # sum_list로 가서 총점 넣고 해당 인덱스 불러오고
    # 인덱스에 공식 만들어서 대입해야하는데 머리가 안돌아가서 계산을 못하겠다..!
    # 였는데 학생수 // 10 으로 나누기만 하면 됐다... (예상했던대로)
    res_index = sum_list.index(matrix[K-1]) // (N//10)

    print(f'#{t} {grade[res_index]}')