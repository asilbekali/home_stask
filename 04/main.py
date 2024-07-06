def My_sort(lst):
    if not all(isinstance(x, int) and x > 0 for x in lst):
        raise ValueError("Hama elementlar int tipida bolishi kerak !!!")
    
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))
    
    sorted_lst = sorted(lst, key=sum_of_digits)
    
    return sorted_lst

user1 = list(map(int, input("Enter the first list of numbers: ").split(',')))
user2 = list(map(int, input("Enter the second list of numbers: ").split(',')))

print(My_sort(user1))
print(My_sort(user2))
