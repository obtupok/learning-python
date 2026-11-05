score = int(input("Баллы: "))
if score > 100 or score < 0:
    print("ошибка: баллы должны быть от 0 до 100")
elif score >= 90:
    print("отлично")
elif score >= 75:
    print("хорошо")
elif score >= 60:
    print("удовлетворительно")
else:
    print("не сдал")