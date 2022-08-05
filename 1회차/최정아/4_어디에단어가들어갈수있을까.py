import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")


T = int(input()) 
K = [] # 빈 리스트 생성
white = (255, 255, 255) # 하얀색 (r, g, b)

# n의 range를 모두 순회
for _ in range(n):
    line = list(map(int, input().split()))
    # line의 길이가 하얀색이면
    if len(line) == (255, 255, 255):
        K.append(1) # K에 1 추가
    else:
        K.append(0)
# 테스트 케이스 t에 대한 결과 출력   
print(K, end=" ")