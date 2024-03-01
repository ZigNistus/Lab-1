"""
Восьмиричные числа не превышающие 2048 в 10. Выводит на экран нечетные числа, использующие не менее К разных цифр.
Список используемых цифр выводится отдельно прописью.
"""
def count_number(num):
    return len(str(num))
def oct_odd(numbers):
    oct_mass = []
    for i in numbers:
        if i % 2 != 0 and i <= 2048:
            if i >= 0:
                oct_mass.append(oct(i)[2:])
            else:
                oct_mass.append(oct(i)[:1]+oct(i)[3:])

    return oct_mass

def mass_filter(mass, k):
    result = []
    for i in mass:
        if count_number(abs(int(i))) >= k:
            result.append(i)
    return result

def used_num(filtred, numerals):
    unique_list = set()
    for i in filtred:
        unique_list.update(set(str(abs(int(i)))))
    print(f"Нечетные числа с не менее чем {k} цифр в них в 8-ой степени: {filtred}")
    print(f"\nСписок использованных уникальных цифр: ", end='')
    for i in unique_list:
        print(f"[{numerals.get(int(i))}]", end=' ')

def read_file():
    numbers = []
    while True:
        try:
            with open("text.txt", 'r') as file:
                symbol = file.read(1)
                str_num = ''
                count = 0
                while symbol:
                    str_num += symbol
                    if str_num == '-':
                        count += 1
                    if str_num.isdigit():
                        count += 2
                    if not str_num.lstrip("-").isdigit():
                        if count > 1:
                            str_num = str_num[:-1]
                            numbers.append(str_num)
                            str_num = ''
                            count = 0
                        elif count == 1:
                            count += 1
                        else:
                            str_num = ''
                    symbol = file.read(1)
            print(f"Список всех распознанных 10-ых чисел: {numbers}")
            return list(map(int, numbers))
        except FileNotFoundError:
            print('Файла text.txt пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий!')
            return False

if __name__ == "__main__":
    numerals = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    con = True
    while con:
        numbers = read_file()
        if not numbers:
            break
        while True:
            try:
                k = int(input("\nВведите число k выводящее не менее k цифр в числе: "))
                break
            except ValueError:
                print("\tВведено не число. Попробуйте ещё раз!")
        oct_mass = oct_odd(numbers)
        filtred = mass_filter(oct_mass, k)
        used_num(filtred, numerals)
        while True:
            try:
                val = int(input("\n\nХотите выполнить программу ещё раз?\n1. Да \n2. Нет \nОтвет: "))
                if val == 1:
                    break
                elif val == 2:
                    con = False
                    break
            except ValueError:
                print("\tВведено не число. Попробуйте ещё раз!")
