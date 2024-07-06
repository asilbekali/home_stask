def find(data):
    b1 = 0
    b2 = 0 
    b3 = 0
    for i, items in enumerate(data):
        if items[3] > 0:
            if items[-1] == "1-bo'lim":
                b1 += 1
            elif items[-1] == "2-bo'lim":
                b2 += 1
            else:
                b3 += 1
    if b1 > b2 and b1 > b3:
        print("1-bo'lim")
    elif b2 > b1 and b2 > b3:
        print("2-bo'lim")
    else:
        print("3-bo'lim")                              

lst = [
    ["Anvar", "Junior", 500, 100, "1-bo'lim"],
    ["Asror", "Middle", 1500, 500, "2-bo'lim"],
    ["Kamola", "Senior", 2500, -100, "3-bo'lim"],
    ["Vali", "Junior", 500, -100, "1-bo'lim"],
    ["Davron", "Middle", 1500, 100, "2-bo'lim"],
    ["Bahodir", "Senior", 2500, -100, "3-bo'lim"],
    ["Farrux", "Junior", 500, 100, "1-bo'lim"],
    ["Jamila", "Middle", 1500, 200, "2-bo'lim"],
    ["Jasur", "Senior", 2500, 500, "3-bo'lim"],
    ["Komila", "Junior", 500, -100, "1-bo'lim"]
]

find(lst)
