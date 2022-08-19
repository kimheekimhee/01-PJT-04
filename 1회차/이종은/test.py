# n = int(input())

# list1 = []

# for i in range(n):
#     list1.append(i+1)


# print(list1)

# n, m = map(int, input().split())


# a = list(map(int, input().split()))


# print(a)

# t = 5

# for tc in range(1, t+1):
#     a = 4
#     print(a)

# # for tc in range(t):
# #     a = 4
# #     print(a)


t = int(input())

result = []

for i in range(t):
    n, m = map(int, input().split())
    for j in range(n):
        a, b, c = map(int, input().split())
        sum1 = a*0.35 + b*0.45 + c*0.2
        result.append(sum1)

    result1 = sorted(result)

    print(result1[m-1])