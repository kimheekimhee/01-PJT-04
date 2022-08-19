import sys

sys.stdin = open("_괄호짝짓기.txt")

T = 10
for t in range(1, T+1):
    n = int(input())
    g = input()
    dict = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>'
    }
    l = [] # 스택으로 쓸 리스트
    result = 1 # 결과값 기본 설정

    # 괄호를 반복문에 돌리기
    for i in g:
        # 만약 i가 딕셔너리 키값과 같다면(왼쪽 괄호라면)
        if i in dict.keys():
            # 리스트에 추가
            l.append(i)

        # 오른쪽 괄호일 경우    
        else:
            # 만약 i가 리스트 최근 값(왼쪽 괄호)을 키로 가진(왼쪽 짝이 있으면서)
            # 딕셔너리의 밸류값과 같다면(오른쪽 괄호라면)
            if i == dict[l[-1]]:
                # 리스트에서 빼기
                l.pop()

            # 그외에 바로 오른쪽 괄호가 나오는 경우
            else:
                # 결과값 0으로 바꾸기 (유효하지 않음)
                result = 0
                break
    print(f'#{t}', result)

 
  