def distance(strand_a, strand_b):
    # the provided strands should be of the same length
    # an error is raised if the lenghts are different
    if len(strand_a) != len(strand_b):
        raise ValueError('strands are not of the same length')
    
    distance = 0
    # Using the zip method provides for a cleaner solution
    # atleast in my opinion, but if there is a better
    # way to go about this, please let me know
    for x, y in zip(strand_a, strand_b):
        if x != y:
            distance += 1
    return distance
