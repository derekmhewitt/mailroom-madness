# -*- coding: utf-8 -*-
"""File contains a mailroom helper function."""
import sys


donor_data = {
    'Jennifer White': [50, 32, 17],
    'Larry Page': [83, 26, 12],
    'Stephen Brown': [87, 35, 23],
    'Dennis Ritchie': [30, 40, 50],
    'John McCarthy': [100, 100, 100]
}


def prompt_donor_name(donor_data):
    """Function gets name from stdin.

    If name is list, list donor_data.
    If name is not in donor_data, enter it with [] value.
    Returns name.

    Args:
        donor_data (dict)
    """
    name = get_name(donor_data)
    donor_data.setdefault(name, [])
    return name


def get_name(donor_data, out=sys.stdout):
    """Get a name from the user, prompt.

    Args:
        donor_data (dict)
        out (file, optional)
    """
    prompt = 'Enter a donor name or "list" for all donor names> '
    while True:
        name = raw_input(prompt)
        if name == 'list':
            list_donor_names(donor_data.keys(), out)
        else:
            return name


def list_donor_names(names, out=sys.stdout):
    """Print a list of donor names.

    Args:
        names (list): List of donor names.
        out (file, optional)
    """
    out.write('Donors:\n')
    for name in sorted(names):
        out.write('* {}\n'.format(name))


def get_int(out=sys.stdout):
    """Get an donation amount from the user.

    Args:
        out (file, optional): Description
    """
    prompt = 'Enter a donation amount>'
    failure = "That's not an integer."
    while True:
        try:
            return int(raw_input(prompt))
        except ValueError:
            out.write('{}\n'.format(failure))


def log_thank_you(name, num, donor_data, out=sys.stdout):
    """Records the new donation into donor_data and prints a report of
    the donation to the user.

    Args:
        name (str)
        num (int)
        donor_data (dict)
        out (file, optional)
    """
    donor_data[name].append(num)
    message = 'Thank you {} for your generous donation of {} dollars.\n'
    out.write(message.format(name, num))


def send_thank_you(donor_data):
    """Prompts the user for a name and donation amount, then reports a
    message and records the donation into donor_data.

    Args:
        donor_data (dict)
    """
    name = prompt_donor_name(donor_data)
    amount = get_int()
    log_thank_you(name, amount, donor_data)


def align_cell(value, padding):
    """Align a single value using padding.

    Args:
        value (str or int)
        padding (int)
    """
    whitespace = ' ' * (padding - len(str(value)) + 2)
    return '{}{}'.format(value, whitespace)


def max_size(t):
    '''Return the size of largest sized value from t by its string
    representation

    Args:
        t (list): A list of values to be process.
    '''
    return max(map(lambda x: len(str(x)), t))


def get_paddings(rows):
    """Get the whitespace padding amount per column.

    Args:
        rows (list)
    """
    return [max_size(map(lambda row: row[i], rows))
            for i in range(len(rows[0]))]


def print_row(row, padding, out=sys.stdout):
    """Print row to out with supplied padding.

    Args:
        row (tuple)
        padding (int)
        out (file, optional): The file to print to.

    Returns:
        TYPE: Description
    """
    for value, padding in zip(row, padding):
        out.write(align_cell(value, padding))
    out.write('\n')


def print_table(rows, out=sys.stdout):
    """Print an entire table to the console.

    Args:
        rows (list): The table as a list of rows
        out (file, optional): The file to print to.

    Returns:
        TYPE: Description
    """
    paddings = get_paddings(rows)
    for row in rows:
        print_row(row, paddings, out=out)


def generate_row(name, donations):
    """Generate a single row from name and donations.

    Args:
        name (str): The name of the donor
        donations (list): A list of donations

    Returns:
        tuple
    """
    total = sum(donations)
    donation_count = len(donations)
    average = total/donation_count
    return (name, total, donation_count, average)


def generate_rows(donor_data):
    """Generate rows from donor_data.
    Args:
        donor_data (dict): The data to generate a table from

    Returns:
        list: A list of tuples, which represent rows
    """
    t = list(map(lambda k: generate_row(k, donor_data[k]), donor_data.keys()))
    t.sort(key=lambda x: x[1], reverse=True)
    headers = [(
        'Donor Name:',
        'Total Donated:',
        'Number of Donations:',
        'Average Donation Amount:'
    )]
    return headers + t


def print_donations(donor_data, out=sys.stdout):
    """Generate and print a table of donor_data to out.
    Args:
        donor_data (dict): The data to generate and print a table
        from.
        out (file, optional): The file to print to.
    """
    print_table(generate_rows(donor_data), out=out)

print_donations(donor_data)
