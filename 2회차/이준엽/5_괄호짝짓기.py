for _ in range(1,11):
    n = int(input())
    braket = input()
    jud = 0
    for i in range(n):
        if '()' in braket:
            braket = braket.replace('()','')
        if '[]' in braket:
            braket = braket.replace('[]','')
        if '{'+'}' in braket:
            braket = braket.replace('{'+'}','')
        if '<>' in braket:
            braket = braket.replace('<>','')
        if len(braket) == 0:
            jud = 1
            break
    print(f'#{_}',jud)