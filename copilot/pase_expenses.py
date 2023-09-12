import datetime

def parse_expenses(expenses_string):
    """Parse the list of expenses and return the list of triples (date, value, currency). 
    Ignore lines starting with #
    Parse the date using datetime."""

    expenses = []
    for line in expenses_string.splitlines():
        if line.startswith("#"):
            continue
        date, value, currency = line.split()
        expenses.append((datetime.datetime.strptime(date, "%Y-%m-%d").date(), float(value), currency))
    return expenses