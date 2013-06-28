# coding=utf-8
"""Mantra 3: If a function is too long to fit on a screen, it is too long."""
import os


def too_long():
    """A very long function.

    :returns: An number representing the distance across the universe.
    :rtype: int
    """

    if os.name != 'posix':
        # Poor guy is using windows
        string = (
            'We notice you are using windows. Oh shame what a pity to '
            'see you don\'t have unix underlying your system. That means '
            'no sed, grep, awk, cut, paste and all the other good things '
            'Gnu/Linux and OSX users enjoy...'
            'Unfortunately we are not able to calculate the distance accross '
            'the universe on a windows machine...'
            'If you are using Windows 3.1, please insert a floppy disk with '
            'your math card driver before we can continue. If you are using '
            'Windows 8, please look confused and spend some time wishing you '
            'were using windows 3.1 before you continue.'
            'If you are using Windows XP, please run up the hill with green '
            'grass that is displayed on your desktop.'
        )
        print string
        return
    else:
        # Lucky guy has a unix like OS
        string = (
            'Ah - I see you have a unix like OS - congtratulations on  '
            'choosing well my friend. Proceeding to calculate distance across '
            'the universe.')
        print string

    distance = 242342  # light years
    return distance


def windows_message():
    """Poor guy is using windows."""
    string = (
        'We notice you are using windows. Oh shame what a pity to '
        'see you don\'t have unix underlying your system. That means '
        'no sed, grep, awk, cut, paste and all the other good things '
        'Gnu/Linux and OSX users enjoy...'
        'Unfortunately we are not able to calculate the distance accross '
        'the universe on a windows machine...'
    )
    print string
    return


def unix_message():
    """Lucky guy has a unix like OS."""
    string = (
        'Ah - I see you have a unix like OS - congtratulations on  '
        'choosing well my friend. Proceeding to calculate distance across '
        'the universe.')
    print string


def just_fine():
    """A much more managable function.

    :returns: An number representing the distance across the universe.
    :rtype: int
    """

    if os.name != 'posix':
        return windows_message()

    else:
        unix_message()

    distance = 242342  # light years
    return distance
