import sys

sys.stdin = open("_조교의성적매기기.txt")

# A+ A0 A- B+ B0 B- C+ C0 C- D0 평가 개수 10개  
# 100 = m_score(35%) + e_score(45%) + h_work(20%)
# 학생수 10<= n <= 100이고 10배수
# 확인학생번호 1<= k <= n
# 1줄:test_case / 2줄:n k / ~줄:m_score e_score h_work
# 출력:#test_case 학점

t = int(input())
for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    score_dic = {}
    alpha_score = {}
    alpha_ = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for i in range(1, n + 1):
        m_score, e_score, h_work = map(int, input().split())
        score_dic[i] = round((m_score*0.35)+(e_score*0.45)+(h_work*0.2))
    
    # print(score_dic)
    k_score = score_dic[k]
    # print(k_score)
    all_score = list(score_dic.values())
    all_score.sort(reverse=True)
    cnt = all_score.index(k_score)
    # print(cnt)
    