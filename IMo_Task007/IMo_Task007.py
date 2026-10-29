import os

FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "catalog.txt")

def load_catalog(filename):
    catalog = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                try:
                    parts = line.split(";")

                    if len(parts) != 4:
                        print(f"Предупреждение: неверный формат строки {line_number}.")
                        continue

                    book_id = int(parts[0])
                    title = parts[1]
                    price = int(parts[2])
                    quantity = int(parts[3])

                    if book_id < 1:
                        print(f"Предупреждение: неверный ID в строке {line_number}.")
                        continue

                    if not title or price <= 0 or quantity < 0:
                        print(f"Предупреждение: неверные данные в строке {line_number}.")
                        continue

                    if book_id in catalog:
                        print(f"Предупреждение: повторный ID {book_id}.")
                        continue

                    catalog[book_id] = (title, price, quantity)

                except ValueError:
                    print(f"Предупреждение: ошибка числовых данных в строке {line_number}.")

        return catalog

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return {}

    except OSError as error:
        print(f"Ошибка чтения файла: {error}")
        return {}


def save_catalog(filename, catalog):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for book_id in sorted(catalog):
                title, price, quantity = catalog[book_id]
                file.write(f"{book_id};{title};{price};{quantity}\n")

        print(f"Каталог сохранён в файл {filename}.")

    except OSError as error:
        print(f"Ошибка записи файла: {error}")


def print_catalog(catalog):
    if not catalog:
        print("Каталог пуст.")
        return

    print("\nКаталог:")

    for book_id in sorted(catalog):
        title, price, quantity = catalog[book_id]

        if quantity == 0:
            print(f"{book_id}. {title} — {price} руб., нет в наличии")
        else:
            print(f"{book_id}. {title} — {price} руб., остаток: {quantity}")


def add_book(catalog):
    try:
        book_id = int(input("ID новой книги: "))

        if book_id < 1:
            print("ID должен быть целым числом начиная с 1.")
            return False

        if book_id in catalog:
            print("Книга с таким ID уже существует.")
            return False

        title = input("Название: ").strip()

        if not title or ";" in title:
            print("Название не должно быть пустым или содержать ';'.")
            return False

        price = int(input("Цена: "))

        if price <= 0:
            print("Цена должна быть больше 0.")
            return False

        quantity = int(input("Количество: "))

        if quantity < 0:
            print("Количество не может быть отрицательным.")
            return False

        catalog[book_id] = (title, price, quantity)

        print(f"Книга «{title}» добавлена.")
        return True

    except ValueError:
        print("ID, цена и количество должны быть целыми числами.")
        return False


def delete_book(catalog):
    try:
        book_id = int(input("ID книги: "))

        if book_id not in catalog:
            print("Книга с таким ID не найдена.")
            return False

        title = catalog[book_id][0]
        del catalog[book_id]

        print(f"Книга «{title}» удалена.")
        return True

    except ValueError:
        print("ID должен быть целым числом.")
        return False


def change_price(catalog):
    try:
        book_id = int(input("ID книги: "))

        if book_id not in catalog:
            print("Книга с таким ID не найдена.")
            return False

        new_price = int(input("Новая цена: "))

        if new_price <= 0:
            print("Цена должна быть больше 0.")
            return False

        title, price, quantity = catalog[book_id]
        catalog[book_id] = (title, new_price, quantity)

        print(f"Цена книги «{title}» изменена на {new_price} руб.")
        return True

    except ValueError:
        print("ID и цена должны быть целыми числами.")
        return False


def change_quantity(catalog):
    try:
        book_id = int(input("ID книги: "))

        if book_id not in catalog:
            print("Книга с таким ID не найдена.")
            return False

        new_quantity = int(input("Новое количество: "))

        if new_quantity < 0:
            print("Количество не может быть отрицательным.")
            return False

        title, price, quantity = catalog[book_id]
        catalog[book_id] = (title, price, new_quantity)

        print(f"Количество книги «{title}» изменено на {new_quantity}.")
        return True

    except ValueError:
        print("ID и количество должны быть целыми числами.")
        return False


def main():
    catalog = load_catalog(FILENAME)

    print(f"Файл {FILENAME} загружен. Книг в каталоге: {len(catalog)}")

    while True:
        print("\nМеню:")
        print("1 — показать каталог")
        print("2 — добавить книгу")
        print("3 — удалить книгу")
        print("4 — изменить цену")
        print("5 — изменить количество")
        print("0 — сохранить и выйти")

        try:
            choice = int(input("Выберите пункт: "))
        except ValueError:
            print("Введите номер пункта меню целым числом.")
            continue

        if choice == 1:
            print_catalog(catalog)
        elif choice == 2:
            add_book(catalog)
        elif choice == 3:
            delete_book(catalog)
        elif choice == 4:
            change_price(catalog)
        elif choice == 5:
            change_quantity(catalog)
        elif choice == 0:
            save_catalog(FILENAME, catalog)
            print("До свидания!")
            break
        else:
            print("Такого пункта меню нет.")


main()