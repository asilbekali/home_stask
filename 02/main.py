dct = {"Asilbek": "", "Joha": "", "Vali": "", "Sanjar": ""}
zero = 0
one = 0

for key in dct.keys():
    dct[key] = input(f"{key} uchun faqat 0 yoki 1 kiriting: ")
    if dct[key] == '1':
        one += 1
    else:
        zero += 1

if zero > one:
    print("\n\n")
    for key, value in dct.items():
        if value == '0':
            print(f"{key}: {value}")
elif zero == one:
    print("\n\n")
    for key, value in dct.items():
        print(f"{key}: {value}")

else:
    print("\n\n")
    for key, value in dct.items():
        if value == '1':
            print(f"{key}: {value}")
