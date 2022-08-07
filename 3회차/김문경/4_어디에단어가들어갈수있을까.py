import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for test_case in range(T):
    cnt_tot = 0
    N, K = map(int, input().split())
    wordlist = []
    for i in range(N):
        x = list(input().split())
        wordlist.append(x)

    for i in wordlist:
        cnt_good = 0
        linelist = []
        # 리스트를 하나의 문자열로 체크
        x = ''.join(i)
        # 문자 하나하나 기준 순회하면서 1이 있으면 cnt_good을 1 증가
        # 만약 0이 들어오면 cnt_good를 초기화하면서 cnt_good을 linelist에 저장
        for char in x:
            if char == '1':
                cnt_good += 1
            else:
                linelist.append(cnt_good)
                cnt_good = 0
        # 마지막이 0으로 끝나면 저장을하지만 1로 끝나면 그렇지 않기 때문에 한 번 더 append시킴
        # 0으로 끝났으면 어차피 cnt_good = 0 이므로 리스트에 추가해도 결과에 큰 상관 안 미침 (우리는 길이가 K인것만 세기를 원하기 때문)
        linelist.append(cnt_good)

        # 한 줄 안에 cnt_good이 여러개 존재할 수 있는데
        # 그 중에서 K 길이 인것만 카운트 -> cnt_tot
        cnt_tot += linelist.count(K)

    # 이번엔 세로로 체크하기 위해 열 기준으로 전체 리스트를 바꿈
    new_wordlist = []
    for j in range(N):
        col = []
        for i in range(N):
            col.append(wordlist[i][j])
        new_wordlist.append(col)
        
    # 위에서 했던 체크 과정 반복
    for i in new_wordlist:
        cnt_good = 0
        x = ''.join(i)
        linelist = []
        for char in x:
            if char == '1':
                cnt_good += 1
            else:
                linelist.append(cnt_good)
                cnt_good = 0
        linelist.append(cnt_good)
        cnt_tot += linelist.count(K)
    print(f'#{test_case + 1}', cnt_tot)