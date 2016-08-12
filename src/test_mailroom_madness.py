# -*- coding: utf-8 -*-
"""File tests a mailroom helper function.

Attributes:
    TEST_INTS (TYPE): Description
    TEST_NAMES (TYPE): Description
"""
import pytest

TEST_INTS = [
    (u'13', 13),
    (u'49', 49),
    (u'35', 35)
]
TEST_NAMES = [
    u'Jennifer Lange',
    u'Foo Bar',
    u'Hello World'
]
TEST_MAX_SIZE = [
    ([u'string', 6, 34, u'taco'], 6),
    ([873, u'Bob Saget', 387263743], 9)
]


def test_prompt_donor_name():
    """Function tests prompt_donor_name with test data."""
    import mailroom_madness
    mailroom_madness.input = lambda _: u'Jennifer White'
    d = {}
    assert mailroom_madness.prompt_donor_name(d) == u'Jennifer White'
    assert d[u'Jennifer White'] == []


@pytest.mark.parametrize('user_input, function_output', TEST_INTS)
def test_get_int(user_input, function_output):
    """Function tests get_int with simulated inputs.

    Args:
        user_input (str)
        function_output (int)
    """
    import mailroom_madness
    mailroom_madness.input = lambda _: user_input
    assert mailroom_madness.get_int() == function_output


@pytest.mark.parametrize('user_input', TEST_NAMES)
def test_get_name(user_input):
    """Function tests get_name function with test data.

    Args:
        user_input (str)
    """
    import mailroom_madness
    mailroom_madness.input = lambda _: user_input
    assert mailroom_madness.get_name({}) == user_input


def test_list_donor_names():
    """Function tests list_donor_names with TEST_NAMES."""
    from mailroom_madness import list_donor_names
    from io import StringIO
    out = StringIO()
    list_donor_names(TEST_NAMES, out)
    result = u"""
Donors:
* Foo Bar
* Hello World
* Jennifer Lange"""
    assert out.getvalue().strip() == result.strip()


def test_log_thank_you():
    """Function tests log_thank_you with test data."""
    import mailroom_madness
    from io import StringIO
    out = StringIO()
    mailroom_madness.input = lambda _: u'53'
    d = {u'Bob Barker': []}
    mailroom_madness.log_thank_you(u'Bob Barker', 53, d, out)
    assert d == {u'Bob Barker': [53]}
    out_text = u'Thank you Bob Barker for your generous donation of 53 dollars.'
    assert out.getvalue().strip() == out_text


def test_send_thank_you():
    """Not sure if we should test this."""
    pass


@pytest.mark.parametrize('user_input, correct_output', TEST_MAX_SIZE)
def test_max_size(user_input, correct_output):
    """Function tests max_size with test data.

    Args:
        user_input (list): List of donor data
        correct_output (int): Int that is length of longest input
    """
    from mailroom_madness import max_size
    assert max_size(user_input) == correct_output


def test_get_paddings():
    """Function tests test_get_paddings with test data."""
    from mailroom_madness import get_paddings
    rows = [
        (u'Stephen Brown', 145, 3, 48.33),
        (u'Larry Page', 121, 3, 40.33),
        (u'Jennifer White', 99, 3, 33.0)
    ]
    assert get_paddings(rows) == [14, 3, 1, 5]


def test_print_row():
    """Function tests pring_row with test data."""
    from mailroom_madness import print_row
    from io import StringIO
    out = StringIO()
    row = (u'Stephen Brown', 145, 3, 48.33)
    padding = [14, 5, 3, 6]
    compare = u'Stephen Brown   145    3    48.33   '
    print_row(row, padding, out)
    assert out.getvalue().strip() == compare.strip()


def test_print_donations():
    """Function tests pring_row with test data."""
    from mailroom_madness import print_donations
    from io import StringIO
    out = StringIO()

    test_data = {
        u'Jennifer White': [1, 2, 3],
        u'Larry Page': [4, 5, 6],
    }

    print_donations(test_data, out)
    expected_output = u'''
Donor Name:     Total Donated:  Number of Donations:  Average Donation Amount:  
Larry Page      15              3                     5.0                       
Jennifer White  6               3                     2.0'''
    assert out.getvalue().strip() == expected_output.strip()


# def test_log_thank_you():
#     """Function tests log_thank_you with test data."""
#     import mailroom_madness
#     from io import StringIO
#     out = StringIO()
#     mailroom_madness.raw_input = lambda _: '53'
#     d = {'Bob Barker': []}
#     mailroom_madness.log_thank_you('Bob Barker', 53, d, out)
#     assert d == {'Bob Barker': [53]}
#     out_text = 'Thank you Bob Barker for your generous donation of 53 dollars.'
#     assert out.getvalue().strip() == out_text
