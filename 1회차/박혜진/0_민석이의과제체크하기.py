import sys

sys.stdin = open("_민석이의과제체크하기.txt")

n = int(input())

for num in range(1, n+1) :
  all, yes = map(int, input().split())
  yes_s = set(map(int, input().split()))

  all_s = set()

  for i in range(1, all+1) :
    all_s.add(i)

  no_s = all_s - yes_s

  print(f'#{num}', *no_s)
