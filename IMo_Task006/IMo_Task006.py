GOODS = {
    "хлеб": 50,
    "молоко": 90,
    "сыр": 400,
    "яблоки": 120,
    "кофе": 350
}


def print_menu(prices):
    print("Товары в продаже:")
    for product, price in prices.items():
        print(f"  {product} — {price} руб.")


def ask_quantity(product):
    return int(input(f"Сколько «{product}»? ").strip())


def item_cost(price, quantity):
    return price * quantity


def print_receipt(cart):
    print("\n--- Чек ---")
    total = 0
    for idx, (product, amount, cost) in enumerate(cart, start=1):
        print(f"{idx}. {product} × {amount} = {cost} руб.")
        total += cost
    print(f"Сумма: {total} руб.")
    return total


def apply_discount(total, card=False):
    if card:
        discount = (total * 10) // 100
    elif total >= 1000:
        discount = (total * 5) // 100
    else:
        discount = 0

    to_pay = total - discount
    return discount, to_pay


def main():
    seller = input("Введите имя кассира: ").strip()
    print(f"Здравствуйте, {seller}! Касса открыта")
    print_menu(GOODS)
    print()

    cart = []

    while True:
        raw_input = input('Товар (или "оплата", чтобы перейти к оплате): ').strip()

        if raw_input.lower() == "оплата":
            break

        product = raw_input.lower()

        if product not in GOODS:
            print(f"Товара «{product}» нет в продаже\n")
            continue

        amount = ask_quantity(product)

        cost = item_cost(GOODS[product], amount)
        cart.append((product, amount, cost))
        print(f"Добавлено: {product} × {amount} = {cost} руб.\n")

    check_card = input("\nЕсть карта магазина? (да/нет): ").strip().lower()
    has_card = check_card == "да"

    total_price = print_receipt(cart)

    discount, to_pay = apply_discount(total_price, card=has_card)

    different_products = len({item[0] for item in cart})

    print(f"Скидка: {discount} руб.")
    print(f"К оплате: {to_pay} руб.")
    print(f"Разных товаров в чеке: {different_products}\n")
    print(f"Спасибо за работу, {seller}!")


main()