from datetime import date, datetime, timedelta


def calculate_days_left(end_date: str, today=None):
    today = date.today() if today is None else today
    future = datetime.strptime(end_date, '%Y-%m-%d')
    return (future - today).days


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
    if date.today() == datetime.strptime(data["target_date"], '%Y-%m-%d'):
        return data, f"{data['tweep']} {data['action']} today!"
    else:
        message = f"{data['days_left']} more till {data['tweep']} {data['action']}"
        data["days_left"] -= 1
        return data, message