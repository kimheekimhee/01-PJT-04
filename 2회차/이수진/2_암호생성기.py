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


