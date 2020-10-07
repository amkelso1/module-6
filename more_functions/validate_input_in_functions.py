"""
author: a;ex kelso
program: validate_input_in_functions.py

prompts user for name and score, prints values to console
"""


def score_input(test_name, test_score=0, invalid_message='invalid test score, please try again'):
    """
    function that accepts params and returns a string....
    :param test_name: the name of a test/exam
    :param test_score: a value between 0 and 100 representing a test score
    :param invalid_message: message displayed when an invalid score is provided
    :return: formatted string with test name and test score
    """
    try:
        if 0 <= test_score <= 100:
            #print(f'{test_name}: {test_score}')
            return f'{test_name}: {test_score}'
        else:
            return invalid_message
    except TypeError:
        raise TypeError


if __name__ == '__main__':
    try:
        print(score_input('test1', '45'))
    except TypeError:
        print('Not a valid score.')
