print("Введите ваше ФИО (через пробел):")
fio = input().split()

print("Привет, " + fio[1] + "!")

item1 = input("Введите первый товар: ")
item2 = input("Введите второй товар: ")
item3 = input("Введите третий товар: ")

shopping_list = [item1, item2, item3]

print("Ваш список: " + str(shopping_list))
print("Товаров в списке: " + str(len(shopping_list)))

shopping_list.append("стакан")
print("Список после добавления подарка: " + str(shopping_list))

shopping_list.sort(key=str.lower)
print("Отсортированный список: " + str(shopping_list))

print("До свидания, " + fio[1][0] + "." + fio[2][0] + ". " + fio[0] + "!")