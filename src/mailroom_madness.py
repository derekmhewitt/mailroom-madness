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
    prompt = 'Enter a donor name or "list" for all donor names.'
    while True:
        name = raw_input(prompt)
        if name == 'list':
            print(donor_data.keys())
        else:
            break
    # TODO: validate name here
    donor_data.setdefault(name, [])
    return name


def get_int(prompt, failure, out=sys.stdout):
    """Function does stuff."""
    while True:
        try:
            return int(raw_input(prompt))
        except ValueError:
            out.write(failure)


def send_thank_you(name, num, donor_data, out=sys.stdout):
    """docstring."""
    donor_data[name].append(num)
    out.write('Thank you {} for your generous donation of {} dollars.'.format(name, num))
