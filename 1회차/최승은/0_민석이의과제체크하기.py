T = int(input()) # 테스트 케이스의 수 
for i in range(1, T+1):
    n, k = map(int, input().split()) # n = 수강생의 수, k = 과제제출 수강생 수
    submit = list(map(int, input().split())) # 제출한 사람 
    none_submit = [] # 제출안한 사람 
    for i_ in range(1, n+1):
        if i_ not in submit:
            none_submit.append(i_)
     # print(f"#{i} {*none_submit}")
    print("#{}".format(i),*none_submit)