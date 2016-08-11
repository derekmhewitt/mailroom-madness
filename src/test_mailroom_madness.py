# -*- coding: utf-8 -*-
"""File tests a mailroom helper function."""
import pytest
import io

TEST_INTS = [
    ('13', 13),
    ('49', 49),
    ('35', 35)
]

TEST_NAMES = [
    'Jennifer Lange',
    'Foo Bar',
    'Hello World'
]


def test_prompt_donor_name():
    """Function tests prompt_donor_name with test data."""
    import mailroom_madness
    mailroom_madness.raw_input = lambda _: 'Jennifer White'
    d = {}
    assert mailroom_madness.prompt_donor_name(d) == 'Jennifer White'
    assert d['Jennifer White'] == []


# def test_prompt_donor_name_two():
#     """Function tests prompt_donor_name with 'list'."""
#     import mailroom_madness
#     mailroom_madness.raw_input = lambda _: 'list'
#     asssert stdout = #list value
# we will come back to this test (probably)


@pytest.mark.parametrize('user_input, function_output', TEST_INTS)
def test_get_int(user_input, function_output):
    """docstring."""
    import mailroom_madness
    mailroom_madness.raw_input = lambda _: user_input
    assert mailroom_madness.get_int() == function_output


@pytest.mark.parametrize('user_input', TEST_NAMES)
def test_get_name(user_input):
    import mailroom_madness
    mailroom_madness.raw_input = lambda _: user_input
    assert mailroom_madness.get_name({}, '') == user_input


def test_log_thank_you():
    """Function tests send_thank_you with test data."""
    import mailroom_madness
    from io import StringIO
    out = StringIO()
    mailroom_madness.raw_input = lambda _: '53'
    d = {'Bob Barker': []}
    mailroom_madness.log_thank_you('Bob Barker', 53, d, out)
    assert d == {'Bob Barker': [53]}
    assert out.getvalue().strip() == 'Thank you Bob Barker for your generous donation of 53 dollars.'
