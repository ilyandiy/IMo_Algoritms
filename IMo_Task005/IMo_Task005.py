organizer = input("Введите ваше имя: ").strip()
print(f"Здравствуйте, {organizer}! Открываем зрительское голосование")

movies_set = {"дюна", "аватар", "матрица", "интерстеллар", "шрек"}
print("Фильмы в программе фестиваля:", ", ".join(movies_set))
print()

votes_count = {movie: 0 for movie in movies_set}
voted_viewers = set()
liked_by_all = None

while True:
    voter_name = input('Имя зрителя (или "стоп", чтобы закончить): ').strip()
    
    if voter_name.lower() == "стоп":
        break

    if voter_name.lower() in voted_viewers:
        print(f"{voter_name}, вы уже голосовали, второй голос не засчитан\n")
        continue

    voted_viewers.add(voter_name.lower())
    liked_movies = input("Какие фильмы вам понравились (через запятую): ")
    viewer_valid_votes = set()
    
    for item in liked_movies.split(","):
        movie = item.strip().lower()
        if not movie:
            continue
        
        if movie in movies_set:
            viewer_valid_votes.add(movie)
        else:
            print(f"Фильма «{movie}» нет в программе, голос не засчитан")

    for movie in viewer_valid_votes:
        votes_count[movie] += 1

    if liked_by_all is None:
        liked_by_all = viewer_valid_votes.copy()
    else:
        liked_by_all &= viewer_valid_votes

    print(f"Спасибо, {voter_name}! Засчитано голосов: {len(viewer_valid_votes)}\n")

print("Итоги голосования")
total_viewers = len(voted_viewers)
print(f"Проголосовало зрителей: {total_viewers}")

for movie, count in votes_count.items():
    print(f"{movie} - {count}")

max_votes = max(votes_count.values())
if total_viewers > 0 and max_votes > 0:
    winners = [movie for movie, count in votes_count.items() if count == max_votes]
    print(f"Победитель: {', '.join(winners)} ({max_votes})")
else:
    print("Победитель: голосование не состоялось (0 голосов)")

if total_viewers > 0 and liked_by_all:
    print(f"Понравились всем: {', '.join(liked_by_all)}")
else:
    print("Понравились всем: таких нет")

voted_any_set = {movie for movie, count in votes_count.items() if count > 0}
no_votes_set = movies_set - voted_any_set

if no_votes_set:
    print(f"Не выбрал никто: {', '.join(no_votes_set)}\n")
else:
    print("Не выбрал никто: таких нет\n")

print(f"До свидания, {organizer}!")