# -*- coding: utf-8 -*-
"""File contains a mailroom helper function."""
import io
import sys


donor_data = {
    'Jennifer White': [50, 32, 17],
    'Larry Page': [83, 26, 12],
    'Stephen Brown': [87, 35, 23]
}


def prompt_donor_name(donor_data):
    """Function gets name from stdin.

    If name is list, list donor_data.
    If name is not in donor_data, enter it with [] value.
    Returns name.
    """
    name = get_name(donor_data)
    donor_data.setdefault(name, [])
    return name


def get_name(donor_data, out=sys.stdout):
    """Get a name from the user, prompt """
    prompt = 'Enter a donor name or "list" for all donor names> '
    while True:
        name = raw_input(prompt)
        if name == 'list':
            list_donor_names(donor_data.keys(), out)
        else:
            return name


def list_donor_names(names, out=sys.stdout):
    """Print a list of donor names."""
    out.write('Donors:\n')
    for name in names:
        out.write('* {}\n'.format(name))


def get_int(out=sys.stdout):
    """Get an donation amount from the user."""
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
    """
    donor_data[name].append(num)
    message = 'Thank you {} for your generous donation of {} dollars.\n'
    out.write(message.format(name, num))


def send_thank_you(donor_data):
    """Prompts the user for a name and donation amount, then reports a
    message and records the donation into donor_data.
    """
    name = prompt_donor_name(donor_data)
    amount = get_int()
    log_thank_you(name, amount, donor_data)


def align_cell(value, padding):
    """Align a single value using padding."""
    whitespace = ' ' * (padding - len(str(value)) + 2)
    return '{}{}'.format(value, whitespace)


def max_size(t):
    ''' Return the size of largest sized value from t by its string
    representation '''
    return max(map(lambda x: len(str(x)), t))


def get_paddings(rows):
    """Get the whitespace padding amount per column."""
    return [max_size(map(lambda t: t[i], rows)) for i in range(len(rows[0]))]


def print_row(row, padding):
    for value, padding in zip(row, padding):
        sys.stdout.write(align_cell(value, padding))
    sys.stdout.write('\n')


def print_table(rows):
    paddings = get_paddings(rows)
    for row in rows:
        print_row(row, paddings)


def generate_row(name, donations):
    total = sum(donations)
    donation_count = len(donations)
    average = total/donation_count
    return (name, total, donation_count, average)


def generate_rows(donor_data):
    t = list(map(lambda k: generate_row(k, donor_data[k]), donor_data.keys()))
    t.sort(key=lambda x: x[1], reverse=True)
    return t
