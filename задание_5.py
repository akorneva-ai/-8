s = 'ututututfddfs'
t = 'otiyryjhgf'
r = 'nmcvbniigjh'
k = []
for i in s + t + r:
    if s.count(i) > 0 and (t + r).count(i) == 0:
        k.append(i)
    elif t.count(i) > 0 and (r + s).count(i) == 0:
        k.append(i)
    elif (s + t).count(i) == 0 and r.count(i) > 0:
        k.append(i)
print(set(k))