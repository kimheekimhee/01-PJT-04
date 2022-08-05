import sys

sys.stdin = open("_괄호짝짓기.txt")

for test_case in range(1, 11):                  # 10개의 테스트케이스
    pair = {'()':0, '[]':0, '{}':0, '<>':0}     # 괄호 별 짝 확인 딕셔너리
    length = int(input())                       # 문자열 길이
    word = input()                              # 괄호 문자열
    possible = 1                                # 유효성 초기값 1(유효함)
 
    for c in word:                              # 문자열 처음부터 끝까지
        for key, value in pair.items():         # 키:값 - 괄호 종류:짝 상태
            if c in '([{<' and c in key:        # 해당 괄호가 왼쪽 괄호이면
                pair[key] += 1                  # 괄호 종류에 맞는 키의 값을 +1
            elif c in ')]}>' and c in key:      # 해당 괄호가 오른쪽 괄호이면
                pair[key] -= 1                  # 괄호 종류에 맞는 키의 값을 -1
         
    for key, value in pair.items():             # 괄호 종류:짝 상태 확인
        if value != 0:                          # 상태가 0이 아니면 짝이 안맞음
            possible = 0                        # 유효성 0(유효하지 않음)
             
    print(f'#{test_case} {possible}')           # 유효성 여부 출력