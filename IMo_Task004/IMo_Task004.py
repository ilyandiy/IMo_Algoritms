surname = input("Введите вашу фамилию: ")
first_name = input("Введите ваше имя: ")
print(f"Добро пожаловать, {first_name}! Начинаем принимать зачёт\n")

students_count = int(input("Сколько спортсменов сдают зачёт: "))
tries_count = int(input("Сколько подходов делает каждый: "))

students_list = []
results_list = []
passed_count = 0

for i in range(students_count):
    student_num = i + 1
    print(f"\n--- Спортсмен {student_num} ---")
    student_surname = input("Фамилия спортсмена: ")
    
    student_sum = 0
    
    for j in range(tries_count):
        try_num = j + 1
        pull_up = int(input(f"Подход {try_num}: "))
        student_sum += pull_up
    
    students_list.append(student_surname)
    results_list.append(student_sum)
    
    if student_sum >= 30:
        print(f"{student_surname}: всего {student_sum} — норматив выполнен")
        passed_count += 1
    else:
        print(f"{surname}: всего {student_sum} — норматив не выполнен")

print("\nИтоговая таблица:")
for index in range(len(students_list)):
    position = index + 1
    print(f"{position}. {students_list[index]} — {results_list[index]}")

print(f"\nНорматив выполнили: {passed_count} из {students_count}")
print(f"Всего подтягиваний группы: {sum(results_list)}\n")
print(f"До свидания, {first_name}!")