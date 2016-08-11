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
