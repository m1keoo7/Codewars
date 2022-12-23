def rot13(message):
    a = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans=''
    for elem in message:
        if elem in a:
            ans+=a[a.find(elem)+13]
        elif elem in b:
            ans+=b[b.find(elem)+13]
        else:
            ans+=elem
    return ans

print(rot13('aA bB zZ 1234 *!?%'))