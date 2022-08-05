import sys

sys.stdin = open("_조교의성적매기기.txt")
'''
접근방법
 
 1~n 번 학생의 점수의 평균을 구한다음 [평균, 번호]의 형식으로 리스트에서
 점수로 내림차순으로 정리한다.
 그리고 번호 : 평균 으로 딕셔너를 만들면 자동으로 평균점수로 내림차순으로 딕셔너리가
 만들어지고 키값들을 리스트로 n//10 구간으로 학점을 넣어준다. 그리고 키값이 곧 학생
 번호이므로 키값으로 벨류를 찾아 출력
'''

tc = int(input())
for tc in range(tc):
    n, p = map(int, input().split())
    dict_ = dict()
    temp = []

    for i in range(n):
        list_ = []
        list_ = list(map(int, input().split()))

        avg = 0.35*list_[0] + 0.45*list_[1] + 0.2*list_[2]
        temp.append([avg, i+1])

    temp.sort(reverse=True)

    for i in temp:
        dict_[i[1]] = i[0]

    a = n//10

    for i in range(1,n+1):
        
        if list(dict_.keys()).index(i) < a: 
            dict_[i] = 'A+'
        if a <= list(dict_.keys()).index(i) < 2*a: 
            dict_[i] = 'A0'
        if 2*a <= list(dict_.keys()).index(i) < 3*a:
            dict_[i] = 'A-'
        if 3*a <= list(dict_.keys()).index(i) < 4*a:
            dict_[i] = 'B+'
        if 4*a <= list(dict_.keys()).index(i) < 5*a:
            dict_[i] = 'B0'
        if 5*a <= list(dict_.keys()).index(i) < 6*a:
            dict_[i] = 'B-'
        if 6*a <= list(dict_.keys()).index(i) < 7*a:
            dict_[i] = 'C+'
        if 7*a <= list(dict_.keys()).index(i) < 8*a:
            dict_[i] = 'C0'
        if 8*a <= list(dict_.keys()).index(i) < 9*a:
            dict_[i] = 'C-'
        if 9*a <= list(dict_.keys()).index(i) < 10*a:
            dict_[i] = 'D0'

    print(f'#{tc+1}',dict_.get(p))