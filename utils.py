from pytz import timezone

def ist_to_timezone(dt, tz_str):
    ist = timezone('Asia/Kolkata')
    target = timezone(tz_str)
    return ist.localize(dt).astimezone(target)
