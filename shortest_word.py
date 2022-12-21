def find_short(s):
    a = s.split()
    ans = len(a[0])
    for i in a:
        if len(i)<ans:
            ans = len(i)
    return ans


print(find_short("turns out random test cases are easier than writing out basic ones"))
