# import sys

# sys.stdin = open("_어디에단어가들어갈수있을까.txt")
# #
# lists = []

# size,length = map(int,(input().split()))

# for i in range(size):
#     z = list(int,input().split())

lists = [[0 ,0 ,1 ,1 ,1],
         [1 ,1 ,0 ,1 ,1],
         [1 ,0 ,1 ,1 ,1],
         [0 ,1 ,1 ,0 ,1],
         [0 ,1 ,1 ,1 ,0],]
#세로
length_result = 0
for x in range(5):
    counts = 0
    for y in range(5):
        if lists[x][y] == 1:
            counts += 1
        if lists[x][y] == 0:
            counts = 0
        if counts == 3:
            length_result += 1 
        if counts > 3:
            length_result -= 1
            counts = 0
#가로
width_result = 0
for x in range(5):
    counts = 0
    for y in range(5):
        if lists[y][x] == 1:
            counts += 1
        if lists[y][x] == 0:
            counts = 0
        if counts == 3:
            width_result += 1 
        if counts > 3:
            width_result -= 1
            counts = 0

print(width_result+length_result)


