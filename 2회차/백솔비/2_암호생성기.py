import sys
sys.stdin = open("_암호생성기.txt")

T = 10
for tc in range(1, T+1):
    N = int(input())
    # 앞에서 빼고 뒤로 넣어야하므로 큐로 풀어줍니다.
    queue = list(map(int, input().split()))

    i = 1
    while True:
        # 앞에서 뺸 값에 i 값을 빼고 뒤로 넣어줍니다.
        num = queue.pop(0)
        queue.append(num-i)
        # 차례마다 1에서 5까지 i 값이 바뀌기때문에 i값에 변화를 줍니다.
        i += 1
        # 마지막 값이 0이거나 0보다 작을 경우 0으로 바꿔주고 멈춥니다.
        if queue[-1] <= 0:
            queue[-1] = 0
            break
        # 1~5 까지 순환을 돌기 때문에 5 이상이 되면 다시 1로 i를 바꿔줍니다.
        if i > 5:
            i =1
            
    print(f'#{tc}' ,*queue)
        
    