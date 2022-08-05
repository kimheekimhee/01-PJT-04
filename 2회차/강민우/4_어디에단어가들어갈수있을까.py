import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    total = 0
    for a in range(N):
        count1 = 1
        count_list1 = []
        count2 = 1
        count_list2 = []
        for b in range(N-K+1):
            if puzzle[a][b] == 1:
                if puzzle[a][b] == puzzle[a][b+1]:
                    count1 += 1
                    count_list1.append(count1)
            if puzzle[a][b] == 0:
                count1 =0
                count_list1.append(count1)
        if max(count_list1) == K:
            total += count_list1.count(K)
        
        for c in range(N-1):
            if puzzle[c][a] == 1:
                if puzzle[c][a] == puzzle[c+1][a]:
                    count2 += 1
                    count_list2.append(count2)
            if puzzle[c][a] == 0:
                count2 =0
                count_list2.append(count2)
        if max(count_list2) == K:
            total += count_list2.count(K) 

    print(total)
            


