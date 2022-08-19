testcase = int(input())

for j in range(testcase):
    people,homeworkpeople = map(int,input().split(' ')) # 총 사람 수와, 숙제를 한 사람 수 받기
    templist = list(range(1,people+1)) # 총 사람 수만큼 임시 리스트 만들기
    homeworklist = list(map(int,input().split(' '))) # 숙제를 한 사람 번호 받기
    for i in range(homeworkpeople):
        templist.remove(homeworklist[i])#숙제한 사람은 임시리스트에서 지워줌, 숙제 안 한 사람만 임시리스트에 남게 됨
    print(f'#{j+1}', *templist) # 임시리스트 출력