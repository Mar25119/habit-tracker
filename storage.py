import json
from habit import Habit
from datetime import datetime


class Storage:
    def __init__(self, filename="habits.json"):
        self.filename = filename
        self.habits = []
        self.load()

    def add_habit(self, habit):
        self.habits.append(habit)
        self.save()

    def remove_habit(self, habit_name):
        self.habits = [h for h in self.habits if h.name != habit_name]
        self.save()

    def get_habit(self, habit_name):
        for habit in self.habits:
            if habit.name == habit_name:
                return habit
        return None

    def get_all_habits(self):
        return self.habits

    def save(self):
        data = []
        for habit in self.habits:
            data.append({
                'name': habit.name,
                'description': habit.description,
                'created_at': habit.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                'completed_dates': habit.completed_dates
            })

        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    habit = Habit(item['name'], item['description'])
                    habit.created_at = datetime.strptime(item['created_at'], "%Y-%m-%d %H:%M:%S")
                    habit.completed_dates = item['completed_dates']
                    self.habits.append(habit)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass