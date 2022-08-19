import sys

sys.stdin = open("_조교의성적매기기2.txt")

#문제를 읽었을떄, 이게 뭔소리인가 싶다.
#학생의 수는 항상 10의 곱이니, 평점은 다 10분의1 만큼 나올것
#일단 총점부터 구하는게 우선인거 같다. 점수에 35퍼 , 45퍼, 20퍼이니 0.35 , 0.45, 0.2 를 곱하고 더하면 총점이 나올것
# 어렴풋 하게 이차원 리스트를 사용해야 한다는것은 알수 있을꺼 같다
# a  b  c를 먼저 받아오고 이차원 리스트로 만들려고 했는데 , a b c가 먼저 인풋을 먹어서 , all_student_list라는 이차원 리스트가 한칸씩 밀리는 현상이 발생했다. all_student_list[x][y] 같은것을 이용해서 리스트에 접근 해야할듯 하다
# 어떻게든 총점의 합을 구하는데 성공한것 같다. 근데 이제 이걸 상위 10퍼 20퍼 식으로 나눠야 할것 같은데 어떻게 해야할까? sorted를 사용해서 index?를 사용해야하나? 잘 모르겠다.
# 10을 기준으로 해서 출력하는건 성공 한거같다. 근데 이제 20명일때 30명일때 어떻게 해야할지 구해야 하겠다. 이미 완전히 잘못 온거같기도 하지만.. 풀수 있을때 까진 풀어야겠다
# 샘플 10개중 2개가 틀렸다. 2번과 4번 결과가 틀렸다. 다시 한번 인풋값을 확인후 왜 틀렸는지 보아야겠다
# 동점자가 있다! 컴퓨터는 인간과 달라서 소수점이 아무문제가 없다. 소수점을 없에려 int 를 나누기할때 사용한게 문제였다! 지우고 제출하니 깔끔하게 패스가 나온다. 총점이 중요한게 아니라 총점의 높고 낮음이 중요한 거였다.
# 너무 시간을 많이 썼다..ㅠ
T = int(input())
for test_case in range(1, T + 1):
    rankalpha = ['A+' , 'A0' , 'A-' , 'B+' , 'B0' , 'B-' , 'C+' , 'C0' , 'C-' , 'D0']
    result = []
    all_student , number = map(int , input().split())
    #a , b , c = map(int , input().split())
    all_student_list = []
    more = int(all_student / 10)
    
    #print(all_student)
    #print(number,type(1))
    #print(a, b , c ,type('1'))
    for _ in range(  all_student):
        line = list(map(int , input().split()))
        all_student_list.append(line)
    for i in range(all_student):
        for y in range(2):
            continue
        #print(all_student_list[i][0])
        all_student_list[i][0] = all_student_list[i][0] * 0.35
        all_student_list[i][1] = all_student_list[i][1] * 0.45
        all_student_list[i][2] = all_student_list[i][2] * 0.2
        #print(sum(all_student_list[i]))
        result.append(sum(all_student_list[i]))
    print(result[number - 1] , '1')
    y = sorted(result)
    print(y)
    best = y[::-1].index(result[number - 1])
    
    print(f'#{test_case} {rankalpha[int(best / more)]}')
       #print(int(all_student_list[i][1] * 0.45))
        #print(int(all_student_list[i][2] * 0.2))
            



