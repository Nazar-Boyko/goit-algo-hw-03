import datetime


def get_days_from_today(date):

    today = datetime.date.today()
    delta = date - today
    return delta.days

if __name__ == "__main__":
    date_str = input("Enter a date (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    days = get_days_from_today(date)
    print(f"Number of days from today to {date}: {days}")