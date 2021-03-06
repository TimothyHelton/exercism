#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. moduleauthor:: Timothy Helton

"""

__version__ = '0.0.2'
script_name = 'DNA'
title = '{}: version {}'.format(script_name, __version__)


def to_rna(strand):
    """
    Function will convert DNA sequences to RNA sequences

    :param str strand: string of DNA nucleotides
    :return: string of RNA nucleotides
    :rtype: str
    """
    dna = 'ACGT'
    rna = 'UGCA'

    return strand.translate(str.maketrans(dna, rna))


if __name__ == '__main__':
    print(to_rna('G'))

    profile_statement = ''
    timing = False
    benchmarking, repeat, number = False, 3, 1E6
    setup = None
    # setup = '\n'.join(('from __main__ import <EnterFuncVarOrClassHere>',
    #                    'from __main__ import <EnterFuncVarOrClassHere>'))

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