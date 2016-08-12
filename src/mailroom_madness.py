# -*- coding: utf-8 -*-
"""File contains a mailroom helper function."""
from __future__ import division
import sys


# backwards compatible input
try:
    input = raw_input
except NameError:
    pass


def prompt_donor_name(donor_data):
    """Function gets name from stdin.

    If name is list, list donor_data.
    If name is not in donor_data, enter it with [] value.
    Returns name.

    Args:
        donor_data (dict)
    """
    name = get_name(donor_data)
    if not name:
        return False
    donor_data.setdefault(name, [])
    return name


def get_name(donor_data, out=sys.stdout):
    """Get a name from the user.

    Return the amount or false if the
    user wishes to return to the main prompt.

    Args:
        donor_data (dict)
        out (file, optional)
    """
    prompt = u'Enter a donor name, "list", or "cancel" > '
    while True:
        name = input(prompt)
        if name == u'list':
            list_donor_names(donor_data.keys(), out)
        elif name == u'cancel':
            return False
        elif name:
            return name
        else:
            out.write('Please give a name.')


def list_donor_names(names, out=sys.stdout):
    """Print a list of donor names.

    Args:
        names (list): List of donor names.
        out (file, optional)
    """
    out.write(u'Donors:\n')
    for name in sorted(names):
        out.write(u'* {}\n'.format(name))


def get_donation_amount(out=sys.stdout):
    """Get an donation amount from the user.

    Return the amount or
    false if the user wishes to return to the main prompt.

    Args:
        out (file, optional): Description
    """
    prompt = u'Enter a donation amount or "cancel"> '
    failure = u"That's not a positive integer."
    while True:
        user_input = input(prompt)
        if user_input == u'cancel':
            return False
        elif validate_donation_amount(user_input):
            return int(user_input)
        else:
            out.write(u'{}\n'.format(failure))


def validate_donation_amount(user_input):
    """Take user input, returns boolean."""
    try:
        return int(user_input) > 0
    except ValueError:
        return False


def send_thank_you(donor_data):
    """Prompt user for a name and donation amount and records them.

    Args:
        donor_data (dict)
    """
    name = prompt_donor_name(donor_data)
    if name is False:
        return

    amount = get_donation_amount()
    if amount is False:
        return

    log_thank_you(name, amount, donor_data)


def log_thank_you(name, num, donor_data, out=sys.stdout):
    """Record new donation and prints a report.

    Args:
        name (str)
        num (int)
        donor_data (dict)
        out (file, optional)
    """
    donor_data[name].append(num)
    message = u'Thanks {} for your generous donation of {} dollars.\n'
    out.write(message.format(name, num))


def align_cell(value, padding):
    """Align a single value using padding.

    Args:
        value (str or int)
        padding (int)
    """
    whitespace = u' ' * (padding - len(str(value)) + 2)
    return u'{}{}'.format(value, whitespace)


def max_size(t):
    """Return largest value from t by its string representation.

    Args:
        t (list): A list of values to be process.
    """
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
    out.write(u'\n')


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
    average = total / (donation_count or 1)
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
        u'Donor Name:',
        u'Total Donated:',
        u'Number of Donations:',
        u'Average Donation Amount:'
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


def main():
    """Main function.

    This function impelements our main prompt and gives the user options.
    """
    donor_data = {
        u'Jennifer White': [50, 32, 17],
        u'Larry Page': [83, 26, 12],
        u'Stephen Brown': [87, 35, 23],
        u'Dennis Ritchie': [30, 40, 50],
        u'John McCarthy': [100, 100, 100]
    }

    while True:
        print(u"Please select an option:")
        print(u"  1. Send a thank you")
        print(u"  2. Create a report")
        print(u"  3. Exit")

        option = input(u'Enter a number > ')

        if option == u'1':
            send_thank_you(donor_data)
        elif option == u'2':
            print_donations(donor_data)
        elif option == u'3':
            print(u'Bye!')
            exit()
        else:
            print(u"That's not an option")


if __name__ == '__main__':
    main()
