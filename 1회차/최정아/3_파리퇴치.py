import sys

sys.stdin = open("_파리퇴치.txt")

# 테스트 케이스의 개수 T가 주어짐
T = int(input())
# int로 형변환해서 쪼갠 숫자를 n, m 변수에 저장
n, m = map(int, input().split())
# 빈 리스트 생성
matrix = []

# m을 모두 순회
for i in range(m):
    line = list(map(int, input().split()))
    matrix.append(line) # matrix에 추가

print(matrix, end=" ")