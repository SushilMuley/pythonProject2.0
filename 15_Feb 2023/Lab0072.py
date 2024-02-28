def sq_of_number(num):
    return num**2

numbers = [2,4,6,8,10]
sq_numbers = list(map(sq_of_number,numbers))


print(sq_numbers)