# word = "Python"
# print(word[0])     # P
# print(word[1])     # y
# print(word[-1])    # n  — минус значит с конца, -1 это последний
# print(len(word))   # 6  — длина строки

# print(word[0:3])   # Pyt
# print(word[2:])    # thon  — от 2 до конца
# print(word[::-1])  # nohtyP — строка задом наперёд (шаг -1)

# s = "  Привет, Мир  "
# print(s.strip())             # "Привет, Мир" — убрать пробелы по краям
# print(s.lower())             # "  привет, мир  " — в нижний регистр
# print(s.upper())             # "  ПРИВЕТ, МИР  "
# print(s.replace("Мир", "Python"))  # заменить слово

# text = "яблоко банан киви"
# print(text.split())          # ['яблоко', 'банан', 'киви'] — разбить на слова

# if "а" in "банан":
#     print("есть буква а")

# for letter in "кот":
#     print(letter)    # к, о, т — каждый с новой строки



# Часть 2. Списки
# fruits = ["яблоко", "банан", "киви"]
# print(fruits[0])        # яблоко
# print(len(fruits))      # 3

# fruits.append("манго")  # добавить в конец
# print(fruits)           # ['яблоко', 'банан', 'киви', 'манго']

# fruits[1] = "груша"     # заменить элемент

# for fruit in fruits:
#     print(f"Я люблю {fruit}")

# nums = [5, 2, 9, 1]
# print(sum(nums))   # 17
# print(max(nums))   # 9
# print(min(nums))   # 1

# names = []
# for i in range(3):
#     name = input("Имя: ")
#     names.append(name)
# print(names)


# text = input("Фраза: ").lower()
# vowels = "аеёиоуыэюя"
# count = 0
# for letter in text:
#     if letter in vowels:
#         count += 1
# print(f"Гласных: {count}")

# text = input("Фраза: ").lower()
# vowels = " "
# count = 0
# for letter in text:
#     if letter in vowels:
#         count += 1
# print(f"Гласных: {count}")

# word = input("Слово: ").lower()
# reverse = word[::-1]

# if word == reverse:
#     print("палиндром")
# else:
#     print("не палиндром")

# items = []
# while True:
#     item = input("Товар (стоп для выхода): ")
#     if item == "стоп":
#         break
#     items.append(item)

# print(f"Твой список ({len(items)} шт.):")
# number = 1
# for item in items:
#     print(f"{number}. {item}")
#     number += 1    

grades = []
while True:
    g = int(input("Оценка (0 для выхода): "))
    if g == 0:
        break
        grades.append(g)
print(f"Оценок: {len(grades)}")
print(f"Сумма: {sum(grades)}")
print(f"Среднее: {sum(grades) / len(grades) :.2f}")
print(f"Лучшая: {max(grades)}")
print(f"Худшая: {min(grades)}")