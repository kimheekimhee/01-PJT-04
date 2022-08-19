import sys

sys.stdin = open("_암호생성기.txt")

num = int(input())
code = list(map(int, input().split()))

n = 1

while True :
    
  if n < 5 :
    code.append(code[0] - n)
    n += 1
    code.pop(0)

  else :
    n = 1

  if code[0] - n <= 0 :
    code.pop(0)
    code.append(0)
    break

print(f'#{num}', *code)