last_name = input("Введите вашу фамилию: ")
first_name = input("Введите ваше имя: ")
print(f"Добро пожаловать, {first_name}! Начинаем приём заявок\n")

total_abitur = 0
admitted_abitur = 0

while True:
    abitur = input('Фамилия абитуриента (или "завершить", чтобы закончить приём): ')
    
    if abitur.lower() == "завершить":
        break
    
    points = int(input("Балл абитуриента: "))
    diplom = input("Есть ли диплом олимпиады? (да/нет): ").lower()
    
    total_abitur += 1
    
    if points >= 220 or (diplom == "да" and points >= 180):
        print(f"{abitur}: заявка одобрена\n")
        admitted_abitur += 1
    else:
        print(f"{abitur}: заявка отклонена\n")

print(f"\nРассмотрено абитуриентов: {total_abitur}")
print(f"Зачислено: {admitted_abitur}\n")
print(f"До свидания, {first_name}!")