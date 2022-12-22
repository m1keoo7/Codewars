def queue_time(customers, n):
    t = [0]*n
    for elem in customers:
      t[0] += elem
      t.sort()
    return max(t)

print(queue_time([2,2,3,3,4,4], 2))