import sys

sys.stdin = open("_암호생성기.txt")
# 첫번째 cycle이라는 빈 리스트 생성
first_cycle = []
second_cycle = []
# 주어진 수의 range를 list화 
queue = list(range(input()))

# queue의 인덱스를 모두 순회
for idx in queue:
    # (idx)-((idx+1))이 queue의 길이와 같으면
    if len(queue) == (idx) - ((idx)+1):
        # idx가 4 이하이면
        if idx <= 4:
            first_cycle.append() # first_cycle에 추가
        else:
            second_cycle.append()
# queue의 길이가 0보다 클때까지 실행
while (len(queue)) > 0:
    print(queue.pop()) # queue에서 숫자를 뺌
    queue.append() # queue에 추가

print(queue, "\n")
