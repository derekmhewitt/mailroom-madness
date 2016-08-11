# -*- coding: utf-8 -*-
"""Package implements a mailroom helper function."""
from setuptools import setup

setup(
    name="mailroom-madness",
    description="Package implements a mailroom helper function.",
    version="0.1.0",
    author="Derek Hewitt, Justin Lange",
    author_email="derekmhewitt@gmail.com, well1912@gmail.com",
    license="MIT",
    py_modules=["mailroom-madness"],
    package_dir="{'': 'src'}",
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
)
