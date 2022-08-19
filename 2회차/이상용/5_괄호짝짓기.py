# BOJ_9012 괄호랑 유사해보임

# 테스트 케이스는 10개
T = 10
for tc in range(1, T+1):
  N = int(input())
  arr = input()

  stack1 = []
  result = 1
  # 왼쪽괄호들을 다 스택에 저장하고 오른쪽 괄호를 만난다면 pop해서 비교
  # 유효할 경우 1 반환, 유효하지 않을 경우 0 반환
  for i in range(N):
    if arr[i] == '(' or arr[i] == '{' or arr[i] == '[' or arr[i] == '<':
      stack1.append(arr[i])

    if arr[i] == ')':
      if len(stack1) > 0 and stack1.pop() != '(':
        result = 0
        break
    if arr[i] == '}':
      if len(stack1) > 0 and stack1.pop() != '{':
        result = 0
        break
    if arr[i] == ']':
      if len(stack1) > 0 and stack1.pop() != '[':
        result = 0
        break
    if arr[i] == '>':
      if len(stack1) > 0 and stack1.pop() != '<':
        result = 0
        break

print("#{} {}".format(tc, result))