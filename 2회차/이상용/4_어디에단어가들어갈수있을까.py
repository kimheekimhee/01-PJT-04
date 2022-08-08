# 누워서 잘 수 있는 곳 찾는거랑 유사해보임- BOJ_1652

t = int(input())
 
for tc in range(1, t + 1) :
  n, k = map(int, input().split())
  data = [list(map(int, input().split())) for _ in range(n)]

  result = 0
  # 행, 단어 들어갈 수 있는 곳 확인
  for i in range(n) :
    cnt = 0
    for j in range(n) :
      if data[i][j] == 1 :
        cnt += 1
      if data[i][j] == 0 or j == n -1 :
        if cnt == k :
          result += 1
        if data[i][j] == 0 :
          cnt = 0

  # 열, 단어 들어갈 수 있는 곳 확인
  for i in range(n) :
    cnt = 0
    for j in range(n) :
      if data[j][i] == 1 :
        cnt += 1
      if data[j][i] == 0 or j == n - 1 :
        if cnt == k :
          result += 1
        if data[j][i] == 0 :
          cnt = 0

# 케이스 별로 결과값 출력
print('#%d %d' % (tc, result))