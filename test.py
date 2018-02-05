month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def valid_month(month):
    if month < 1 or month > 12:
        return False
    elif isinstance(month, float):
        return False
    return True

def name_of_month(month):
    if valid_month(month):
        return month_names[month]
    return 'Error'


print(name_of_month(2))