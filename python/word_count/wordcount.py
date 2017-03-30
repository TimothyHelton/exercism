#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
.. moduleauthor:: Timothy Helton

"""

import string
from collections import Counter

__version__ = '0.0.1'
script_name = 'Word Count'
title = '{}: version {}'.format(script_name, __version__)


class Phrase():
    """
    Class will collect attributes related to phrases.

    :attributes:

        * **phrase**: string of words
    """
    def __init__(self, phrase):
        self.phrase = phrase

    def word_count(self):
        """
        Display the words in a phrase and number of times each word is used.

        :return: dictionary of words and the number of times they occur in \
            phrase
        :rtype: dict
        """
        filter_phrase = self.phrase.translate([string.punctuation,
                                               string.whitespace])

        return Counter(filter_phrase.split())


if __name__ == '__main__':
    print(Phrase('rah rah ah ah ah\nroma roma ma\nga ga oh la la\nwant your '
                 'bad romance').word_count())

    profile_statement = ''
    timing = False
    benchmarking, repeat, number = False, 3, 1E6
    setup = None
    # setup = '\n'.join(('from __main__ import <EnterFuncVarOrClassHere>',
    #                      'from __main__ import <EnterFuncVarOrClassHere>'))

    if timing:
        import cProfile
        import subprocess

        filename = '{0}.profile'.format(__file__.rstrip('.py'))
        cProfile.run(profile_statement, filename=filename)
        subprocess.call(['snakeviz', filename])

    if benchmarking:
        import timeit

        t_b = timeit.Timer(stmt=profile_statement, setup=setup)
        r_b = int(repeat)
        n_b = int(number)
        timing_info = t_b.repeat(repeat=r_b, number=n_b)
        timing_result = [x_b / n_b for x_b in timing_info]

        print('Average Execution Time: {0}'.format(min(timing_result)))