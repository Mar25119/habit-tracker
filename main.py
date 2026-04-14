from habit import Habit
from storage import Storage
from datetime import datetime


def show_menu():
    print("\n=== ТРЕКЕР ПРИВЫЧЕК ===")
    print("1. Показать все привычки")
    print("2. Добавить привычку")
    print("3. Отметить выполнение")
    print("4. Удалить привычку")
    print("5. Статистика")
    print("6. Поиск привычки")
    print("0. Выход")
    return input("Выберите пункт: ")


def show_all_habits(storage):
    habits = storage.get_all_habits()
    if not habits:
        print("\nНет привычек. Добавьте первую!")
        return

    print("\n=== ВАШИ ПРИВЫЧКИ ===")
    for i, habit in enumerate(habits, 1):
        print(f"{i}. {habit}")


def add_habit(storage):
    name = input("\nНазвание привычки: ")
    if storage.get_habit(name):
        print("Привычка с таким названием уже существует!")
        return

    description = input("Описание (необязательно): ")
    habit = Habit(name, description)
    storage.add_habit(habit)
    print(f"Привычка '{name}' добавлена!")


def mark_completed(storage):
    name = input("\nНазвание привычки: ")
    habit = storage.get_habit(name)

    if not habit:
        print("Привычка не найдена!")
        return

    date_str = input("Дата (YYYY-MM-DD) или Enter для сегодня: ")
    date = None if not date_str else date_str

    if habit.mark_completed(date):
        print(f"Привычка '{habit.name}' отмечена!")
    else:
        print("Уже отмечено за эту дату!")


def remove_habit(storage):
    name = input("\nНазвание привычки для удаления: ")
    habit = storage.get_habit(name)

    if not habit:
        print("Привычка не найдена!")
        return

    confirm = input(f"Удалить '{name}'? (да/нет): ")
    if confirm.lower() == 'да':
        storage.remove_habit(name)
        print("Привычка удалена!")


def show_statistics(storage):
    habits = storage.get_all_habits()
    if not habits:
        print("\nНет привычек для статистики!")
        return

    print("\n" + "=" * 40)
    print("           СТАТИСТИКА")
    print("=" * 40)

    total = len(habits)
    today = datetime.now().strftime("%Y-%m-%d")
    completed_today = sum(1 for h in habits if today in h.completed_dates)

    print(f"\n Всего привычек: {total}")
    print(f" Выполнено сегодня: {completed_today} из {total}")

    if total > 0:
        percentage = (completed_today / total) * 100
        print(f"📈 Процент выполнения: {percentage:.1f}%")

    print("\n📋 Список привычек:")
    for habit in habits:
        streak = habit.get_streak()
        completed_count = len(habit.completed_dates)
        print(f"  • {habit.name}")
        print(f"     Серия: {streak} дней")
        print(f"    ✓ Всего выполнений: {completed_count}")

    print("\n Лучшая серия:")
    if habits:
        best = max(habits, key=lambda h: h.get_streak())
        print(f"   {best.name} - {best.get_streak()} дней!")

    print("=" * 40)


def search_habit(storage):
    query = input("\nВведите название для поиска: ").lower()
    habits = storage.get_all_habits()
    found = [h for h in habits if query in h.name.lower()]

    if found:
        print("\nНайдено привычек:", len(found))
        for h in found:
            print(f"  - {h}")
    else:
        print("Ничего не найдено!")


def main():
    storage = Storage()

    while True:
        choice = show_menu()

        if choice == "1":
            show_all_habits(storage)
        elif choice == "2":
            add_habit(storage)
        elif choice == "3":
            mark_completed(storage)
        elif choice == "4":
            remove_habit(storage)
        elif choice == "5":
            show_statistics(storage)
        elif choice == "6":
            search_habit(storage)
        elif choice == "0":
            print("\nДо свидания!")
            break
        else:
            print("\nНеверный выбор!")


if __name__ == "__main__":
    main()