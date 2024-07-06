def find(lst):
    time = 0
    for i, items in enumerate(lst):
        time += 3
    print(time - 1)

lst = list(map(str, input("Enter colour: ").split()))
find(lst)
