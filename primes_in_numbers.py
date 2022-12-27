def prime_factors(n):
    a = primfacs(n)
    dict={}
    s=''
    for elem in a:
        dict[elem]=a.count(elem)
    for i in dict:
        if dict[i]!=1:
            s+=f"({i}**{dict[i]})"
        else:
            s+=f"({i})"
    return s

def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    primfac[-1]=int(primfac[-1])
    return primfac


print(prime_factors(5151515))