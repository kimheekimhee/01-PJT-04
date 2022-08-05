import sys

sys.stdin = open("_괄호짝짓기.txt")

left = ['(', '[', '{', '<']
right = [')', ']', '}', '>']


for T in range(1, 11):
    N = int(input())
    Test_case = input()
    total = [0] * 4
    for a in Test_case:
        if -1 in total:
            break
        else:
            if a in left:
                total[left.index(a)] += 1
            elif a in right:
                total[right.index(a)] -= 1
    if total.count(0) == 4:
        print(f'#{T} 1')
    else:
        print(f'#{T} 0')