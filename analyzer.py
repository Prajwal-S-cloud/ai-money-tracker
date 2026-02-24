import re

def extract_data(message):

    amount = re.findall(r'\d+', message)
    amount = int(amount[0]) if amount else 0

    message = message.lower()

    if "swiggy" in message or "restaurant" in message:
        category = "Food"

    elif "amazon" in message:
        category = "Shopping"

    elif "metro" in message:
        category = "Transport"

    elif "recharge" in message:
        category = "Bills"

    else:
        category = "Other"

    return amount, category