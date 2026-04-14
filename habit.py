from datetime import datetime


class Habit:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.completed_dates = []

    def mark_completed(self, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        if date not in self.completed_dates:
            self.completed_dates.append(date)
            return True
        return False

    def get_streak(self):
        if not self.completed_dates:
            return 0

        sorted_dates = sorted(self.completed_dates, reverse=True)
        streak = 1

        today = datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.now().timestamp() - 86400)
        yesterday_str = datetime.fromtimestamp(yesterday).strftime("%Y-%m-%d")

        if sorted_dates[0] != today and sorted_dates[0] != yesterday_str:
            return 0

        for i in range(1, len(sorted_dates)):
            curr_date = datetime.strptime(sorted_dates[i - 1], "%Y-%m-%d")
            prev_date = datetime.strptime(sorted_dates[i], "%Y-%m-%d")
            diff = (curr_date - prev_date).days

            if diff == 1:
                streak += 1
            elif diff > 1:
                break

        return streak

    def __str__(self):
        return f"{self.name} (серия: {self.get_streak()} дней)"