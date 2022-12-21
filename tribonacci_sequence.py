def tribonacci(signature, n):
    result = signature
    a, b, c = signature
    if n<=3:
        return [signature[i] for i in range(0, n)]
    for i in range(4, n+1):
        temp = a+b+c
        a, b, c = b, c, temp
        signature.append(c)
    return signature

print(tribonacci([1, 1, 1], 10))
print(tribonacci([1, 1, 1], 1))
print(tribonacci([104, 110, 56], 2))