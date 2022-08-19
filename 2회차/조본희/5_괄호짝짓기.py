import sys
from collections import Counter

sys.stdin = open("_괄호짝짓기.txt")

for test_case in range(1, 11):
    ans = 1
    N = int(input())
    brackets = list(input().rstrip())
    cnt = Counter(brackets)

    if cnt['('] != cnt[')']:    #짝만 맞으면 된다는 조건이기 때문에 그냥 Counter로 편하게 했다.
        ans = 0
    if cnt['['] != cnt[']']:
        ans = 0
    if cnt['{'] != cnt['}']:
        ans = 0
    if cnt['<'] != cnt['>']:
        ans = 0

    print(f'#{test_case} {ans}')