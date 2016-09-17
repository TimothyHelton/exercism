#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module contains function to greet user.

.. moduleauthor:: Timothy Helton
"""


def hello(name=''):
    """Return user greeting if name is provided else state Hello World!

    :param str name: user's name
    """
    if name:
        output = 'Hello, {}!'.format(name.capitalize())
    else:
        output = 'Hello, world!'

    return output
