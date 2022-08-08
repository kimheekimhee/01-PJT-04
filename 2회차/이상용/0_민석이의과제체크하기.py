# 테스트 케이스 수량 입력
# 수강생 전원, 제출한 인원 입력
# 제출한 인원의 번호 입력
# 테스트 케이스 수량만큼 반복

# 테스트 케이스 수량 입력
t = int(input())

# 테스트 케이스 별로 반복문
for i in range(1, t + 1) :
  # 수강생 전원, 제출한 인원 입력
  n, k = map(int, input().split())
  # 제출한 인원의 번호 입력
  data = list(map(int, input().split()))
  
  # 수강생 전원의 수만큼 반복문을 돌려 
  # 과제를 제출한 인원의 번호가 data내의 없을 경우 
  # result에 해당 값(번호)추가
  result = []
  for j in range(1, n + 1) :
    if j not in data :
      result.append(j)

  print(f'#{i}', *result)
  # f'{}'를 통해 문자와 인수를 같이 출력, *를 통해 리스트형 출력X 