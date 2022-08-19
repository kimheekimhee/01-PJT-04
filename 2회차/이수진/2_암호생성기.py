import sys

sys.stdin = open("_암호생성기.txt")

def cycle(nums):
    n=1
    while True :
        if n < 6 :
            if nums[0] > n :
                nums.append(nums.pop(0)-n)
                n+=1
            else :
                nums.pop(0)
                nums.append(0)
                break      
        else:
            n=1
    return nums

for _ in range(10):
    tc=input()
    nums=list(map(int, input().split()))
    k=min(nums)//300
    for i in range(8):
        nums[i]=nums[i]%(300*k)
    print(f'#{tc}', *cycle(nums))

# 사이클이 5번 돌면 모든 숫자가 15씩 감소함
# 사이클이 100번 돌면 모든 숫자가 300 감소함
# 주어진 암호문 내의 가장 작은 숫자를 300으로 나눠보고, 그 몫인 k 만큼 모든 값에서 300*k만큼 빼줌
# 이후 사이클 함수로 암호문 처리
