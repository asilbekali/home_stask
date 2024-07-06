lst = list(map(int, input().split()))
new = []
new2 = []
for i in range(len(lst)):
    if lst[i] < 0:
        new.append(lst[i])
    else:
        new2.append(lst[i])

chunks = [new2[i:i + 2] for i in range(0, len(new2), 2)]

print(*new)
for chunk in chunks:
    print(*chunk)
