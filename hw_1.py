import datetime

def get_days_from_today(date: str):
    try:
        given_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.date.today()
        return (given_date - today).days
    except ValueError:
        return None 


if __name__ == "__main__":
    while True:
        date_str = input("Enter a date (YYYY-MM-DD): ")

        days = get_days_from_today(date_str)

        if days is None:
            print("❌ Невірний формат або неіснуюча дата. Спробуй ще раз.")
        else:
            print(f"📅 Різниця в днях: {days}")
            break