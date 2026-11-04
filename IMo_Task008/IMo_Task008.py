
def total(*scores):
    return sum(scores)


def parse_line(line):
    name, *parts = line.split()

    if not parts:
        raise ValueError("нет очков")

    scores = [int(x) for x in parts]
    return name, scores


def make_rating(totals):
    return sorted(totals.items(), key=lambda x: (-x[1], x[0]))


def print_rating(rating):
    for place, (name, score) in enumerate(rating, 1):
        print(f"{place}. {name} — {score}")


players = {}

print("Вводите результаты: имя и очки через пробел. Чтобы закончить, введите «стоп».")

while True:
    line = input("> ")

    if line.strip().lower() == "стоп":
        break

    try:
        name, scores = parse_line(line)
        players[name] = scores
    except ValueError as e:
        print("Строка пропущена:", e)


totals = {}

for name, scores in players.items():
    totals[name] = total(*scores)

rating = make_rating(totals)

print("\n--- Рейтинг ---")
print_rating(rating)


ten_players = []

for name, scores in players.items():
    if 10 in scores:
        ten_players.append(name)

ten_players.sort()

print("\nНабирали 10 очков:", ", ".join(ten_players))


if rating:
    while True:
        try:
            n = int(input(f"\nСколько лучших показать (1-{len(rating)}): "))

            if n < 1 or n > len(rating):
                raise ValueError(f"нужно число от 1 до {len(rating)}")

            break

        except ValueError as e:
            print("Ошибка:", e)

    print(f"\n--- Топ-{n} ---")
    print_rating(rating[:n])
else:
    print("\nНет игроков для отображения топа.")
