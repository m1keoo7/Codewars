def find_it(seq):
    b=[]
    for i in seq:
        if type(i)==int:
            b.append(i)
    for i in b:
        if b.count(i)%2==1:
            return i