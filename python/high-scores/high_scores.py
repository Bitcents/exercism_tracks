import sys


def latest(scores):
    # simple enough, return the last element
    return scores[-1]


def personal_best(scores):
    # use built-in max function
    return max(scores)

def personal_top_three(scores):
    # There are several ways to implement this
    # I decided to perform a sort first
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[:3]

