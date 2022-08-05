import sys
from collections import Counter

sys.stdin = open("_괄호짝짓기.txt")

for test_case in range(1, 11):
    ans = 1
    N = int(input())
    brackets = list(input().rstrip())
    cnt = Counter(brackets)
    if cnt['('] != cnt[')']:
        ans = 0
    if cnt['['] != cnt[']']:
        ans = 0
    if cnt['{'] != cnt['}']:
        ans = 0
    if cnt['<'] != cnt['>']:
        ans = 0
    print(f'#{test_case} {ans}')