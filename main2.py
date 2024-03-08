"""
Восьмиричные числа не превышающие 2048 в 10. Выводит на экран нечетные числа, использующие не менее 2 цифр.
Список используемых цифр выводится отдельно прописью. Используя регулярные выражения
"""
import re

def fun():
    numerals = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    unique_list = set()
    oct_mass = []
    while True:
        try:
            with open("text.txt", 'r') as file:
                symbol = file.read()
                res = re.findall(r"-?\d{1,3}[13579]\s", symbol)
                res = [int(num) for num in res if int(num) < 2048]
                for i in res:
                    if i >= 0:
                        oct_mass.append(oct(i)[2:])
                    else:
                        oct_mass.append(oct(i)[:1] + oct(i)[3:])
                for i in oct_mass:
                    unique_list.update(set(str(abs(int(i)))))
            print(f"Список 8-ых нечетных чисел не превышающих 2048 в 10-ой: {oct_mass}")
            print(f"\nСписок использованных уникальных цифр: ", end='')
            for i in unique_list:
                print(f"[{numerals.get(int(i))}]", end=' ')
            break
        except FileNotFoundError:
            print('Файла text.txt пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий!')
            return False

if __name__ == "__main__":
    fun()
