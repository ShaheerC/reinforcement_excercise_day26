def generate_dict():
    num_dict = {}
    for num in range(1, 51):
        if num % 2 == 0 and num % 7 == 0:
            num_dict[num] = num*2
        elif num % 2 == 0:
            num_dict[num] = num + 1
        elif num % 7 == 0:
            num_dict[num] = num - 1
        else:
            num_dict[num] = num
    return num_dict

print(generate_dict())