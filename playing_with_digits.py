def dig_pow(n, p):
    a = []
    n = str(n)
    ans=0
    for i in range(0, len(n)):
        a.append(n[i])
    for i in a:
        ans+=int(i)**int(p)
        p+=1
    return ans//int(n) if ans%int(n)==0 else -1

print(dig_pow(89, 1))