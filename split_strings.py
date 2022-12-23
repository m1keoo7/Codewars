def solution(s):
    a=[]
    ans=''
    if len(s)%2!=0:
        s+='_'
    for i in range(0, len(s), 2):
        ans = s[i]+s[i+1]
        a.append(ans)
    return a
print(solution('abcdef'))