import sys

sys.stdin = open("_조교의성적매기기.txt")

T = int(input())

for test_case in range(1, T + 1):
    rank = []
    rating = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    
    # rating 의 학점 배정은 10% 단위로 나누어진다.
    # rank 안의 학생들이 몇 명이 되던간에 순위에 맞추어 10% 비율로 나누어주려면...
    # 전체 학생 수를 등급의 개수 (여기서는 10개) 로 나누어 주면 몇 명 단위로 끊어야 할지 그 몫이 나온다.
    # 그런데 리스트의 검색은 0 번부터 시작하고, 0 은 자기 자신 혹은 어떤 범위의 시작값이라는 의미이기 때문에 0 번도 포함해야 한다.
    # 기존에 1등 부터 시작했기 때문에 0 번부터 시작하기 위해서는 몫으로 나온 학생 수에 -1 을 해 주면 되고,
    # 그렇다면 0 번부터 -1 한 어떤 번호의 범위 내에 있는 자연수의 개수가
    # 특정 구간을 10% 단위로 나누었을 때 그 범위 안에 속하는 사람들의 순위이자 인원수이다.
    # range 함수를 쓰면 0 부터 범위를 가지기 때문에 따로 -1 을 해 줄 필요는 없다.
    # 총원 30 이라고 가정하고 계산을 해보면,
    # rating 의 i 번째에 해당하는 학점을 받을 수 있는 사람은, ( 0 포함하여 계산 )
    # i 를 30 으로 나눈 값에 10을 곱하고 소수점 부분을 버리면 그것이 rank의 i 등수에 해당하는 학점이다.
    # 그런데 i // N * 10 을 해버리면, i // N 에서 이미 소수점이 버려지므로 몫은 항상 0 이 나오기 때문에,
    # i * 10 // N 와 같이 순서를 바꾸어 써야한다.
    # 이제 식을 구했으니 딕셔너리를 이용한 적절한 처리를 통해 답을 출력하면 된다.
    
    N, K = map(int, input().split())
    
    for _ in range(N):
        m, f, a = map(int, input().split())
        
        total = (m * 0.35) + (f * 0.45) + (a * 0.2)
        rank.append(total)
        
    tmp = sorted(rank, reverse = True)
    tmp_dict = {}
    
    for i in range(len(tmp)):
        tmp[i] = (tmp[i] ,rating[i * 10 // N])
    
    for k, v in tmp:
        tmp_dict[k] = v
    
    for j in range(len(rank)):
        if rank[j] in tmp_dict:
            rank[j] = tmp_dict[rank[j]]
    
    print(f"#{test_case} {rank[K-1]}")
