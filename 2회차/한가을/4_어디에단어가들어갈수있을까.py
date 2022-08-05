# N x N 크기의 단어 퍼즐을 만들려고 한다
# 입력으로 단어 퍼즐의 모양이 주어짐
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가
# 들어갈 수 있는 자리의 수를 출력

# 첫 줄에 총 테스트 케이스의 개수 T가 온다
# 다음 줄부터 각 테스트 케이스가 주어진다
# 테스트 케이스의 첫번째 줄에는
# 단어 퍼즐의 가로, 세로 길이 N과 단어의 길이 K가 주어진다
# 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다
# 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0

# 출력 예시
#1 2
#2 6
#3 6
#4 0
#5 14
#6 2
#7 45
#8 0
#9 98
#10 7
import sys
sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
board = []

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board.append(list(map(int, input().split())))