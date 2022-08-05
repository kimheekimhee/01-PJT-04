# 머리가 안돌아가네요 멘탈도 박살
for tc in range(1, 11):
    length = int(input())
    str_ = input()
    for i in range(length):
        try:
            if str_[i] == '(' and ')' in str_[i:]:
                str_ = str_.replace(str_[i], '')
                str_ = str_[i:].replace(')','')
                
            elif str_[i] == '[' and ']' in str_[i:]:
                str_ = str_.replace(str_[i], '')
                str_ = str_[i:].replace(']','')
                
            elif str_[i] == '{' and '}' in str_[i:]:
                str_ = str_.replace(str_[i], '')
                str_ = str_[i:].replace('}','')
                
            elif str_[i] == '<' and '>' in str_[i:]:
                str_ = str_.replace(str_[i], '')
                str_ = str_[i:].replace('>','')
        except:
            break
            
    if len(str_) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')