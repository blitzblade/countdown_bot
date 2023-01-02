from datetime import date, datetime, timedelta

from logger_tool import Logger


def calculate_days_left(end_date: str, today=None):
    today = date.today() if today is None else today
    future = datetime.strptime(end_date, '%Y-%m-%d')
    days = (future.date() - today).days

    print("Days: ", days)
    return days


def calculate_target_date(days: int, today=None):
    today = date.today() if today is None else today
    future = today + timedelta(days=days)
    return future.strftime("%Y-%m-%d")


def clean_data(data, today=None):
    if (data.get("days_left") == None or data.get("days_left") == "") and (data.get("target_date") == None or data.get("target_date") == ""):
        raise RuntimeError(
            "You cannot have empty values for both days and target date")

    if data["days_left"] == None or data["days_left"] == "":
        data["days_left"] = calculate_days_left(
            data["target_date"], today=today)
    elif data["target_date"] == None or data["target_date"] == "":
        data["target_date"] = calculate_target_date(
            data["days_left"], today=today)
    return data


def count_down(data, today=None):
    data = clean_data(data, today=today)
    Logger.info(data)

    today = date.today() if today is None else today

    if data["days_left"] < 0:
        message = None
    elif data["days_left"] == 0:
        message = f"{data['tweep']} {data['action']} today!"
    else:
        days = "days" if data["days_left"] > 1 else "day"
        message = f"{data['days_left']} {days} more till {data['tweep']} {data['action']}"

    data["days_left"] = data["days_left"] - 1
    return data, message
