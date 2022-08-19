# import sys

# sys.stdin = open("_괄호짝짓기.txt")

# 풀었던문제라 충분히 풀수있을것 같은데 시간이 없음 (파리랑 암호에서 시간을 너무많이썼음)

T = int(input())

test = input()

list_ = list(test)

list_dic = {
    '(' = 0
    ')' = 0
    '{' = 0
    '}' = 0
    '<' = 0
    '>' = 0
    '[' = 0
    ']' = 0
}
for i in range(T):
    if list_[i] in list_dic:
        list_dic[list_[i]] += 1
    if list_dic[')'] > list_dic['('] or list_dic['}'] > list_dic['{']


#대충 위에서 닫히는 괄호의 딕셔ㄹ너리 밸류값이 높으면 불가능으로 출력하고 다음테스트케이스로 넘어가고
#하여튼 대충 하다보면 풀릴것같음 시간부족