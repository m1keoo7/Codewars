def open_or_senior(data):
    a = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            a.append("Senior")
        else:
            a.append("Open")
    return a


print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
