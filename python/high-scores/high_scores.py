import sys


def latest(scores):
    # simple enough, return the last element
    return scores[-1]


def personal_best(scores):
    # itearte through list and return the highest score

    # We set max score to a very low number
    # This is not necessary if negative scores are not allowed
    max_score = -1*sys.maxsize 
    for score in scores:
        max_score = max(score, max_score)
    return max_score

def personal_top_three(scores):
    # There are several ways to implement this
    # I decided to perform a sort first
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[:3]

