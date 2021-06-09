def sum_of_multiples(limit, multiples) -> int:
    # this looks stupid XD
    return sum(set([i if i%d == 0 else 0 for i in range(limit) for d in multiples if d != 0 ]))

