import sys

sys.stdin = open("_괄호짝짓기.txt")
t = 10

for p in range(1,t+1):
    n = int(input())
    g = list(input())
    bin = []
    for i in range(n):
        cnt =0
        if g[i] == '(':
            bin.append(g[i])
        elif g[i] == '[':
            bin.append(g[i])
        elif g[i] == '{':
            bin.append(g[i])
        elif g[i] == '<':
            bin.append(g[i])
        elif (g[i] == ')' and '(' not in bin) or (g[i] ==']' and '[' not in bin ) or (g[i] =='}' and '{' not in bin ) or (g[i] =='>' and '<' not in bin):
            s = 0
        
    print(bin)

        
        

            
