def count_number(num):
    return len(str(num))
def oct_odd(limit):
    oct_mass = []
    for i in range(1, limit):
        oct_num = oct(i)[2:]
        if int(oct_num) % 2 != 0:
            oct_mass.append(oct_num)
    return oct_mass

def mass_filter(mass, k):
    result = []
    for i in mass:
        if count_number(i) >= k:
            result.append(i)
    return result

def used_num(filtred):
    unique_list = set()
    for i in filtred:
        unique_list.update(set(str(i)))
    return unique_list

if __name__ == "__main__":
    k = int(input("Введите число из-за которого будут выводиться числа, содержащие не менее цифр этого числа: "))
    limit = 2048
    mass = oct_odd(limit)
    filtred = mass_filter(mass, k)
    unique_list = used_num(filtred)
    print(f"Нечетные числа с не менее чем {k} цифр в них:")
    for i in filtred:
        print(i)

    print(f"\nСписок использованных уникальных цифр: {unique_list}")