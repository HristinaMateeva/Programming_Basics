def smallest_number(num_1, num_2, num_3):
    result = min(num_1, num_2, num_3)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(smallest_number(first_num, second_num, third_num))
