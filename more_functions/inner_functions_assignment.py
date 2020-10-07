"""
author: alex kelso
date: 10/6/2020
program: inner_functions
"""


def measurements(rect_measure):
    a_value = 0.0
    p_value = 0.0

    def area(a_measure):
        if len(a_measure) == 1:
            return a_measure[0] * a_measure[0]
        elif len(a_measure) == 2:
            return a_measure[0] * a_measure[1]
        else:
            raise IndexError

    def perimeter(p_measure):
        if len(p_measure) == 1:
            return p_measure[0] * 4
        elif len(p_measure) == 2:
            return p_measure[0] * 2 + p_measure[1] * 2
        else:
            raise IndexError
    try:
        a_value = area(rect_measure)
        p_value = perimeter(rect_measure)
    except IndexError:
        raise IndexError
    return f"Perimeter = {p_value} Area = {a_value}"


if __name__ == '__main__':
    try:
        print(measurements([2.1, 3.4]))
    except IndexError:
        print('Enter 1 or 2 measurements')
