def slices(series, length):
  
    if len(series) < length:
        raise ValueError('series is too short')
    if length <= 0:
        raise ValueError('sequences must be of positive length')
    if series == "":
        raise ValueError('series is empty') 
    if len(series) == length:
        return [series]

    sequences = []
    for i in range(len(series) - length + 1):
        sequence = ''
        for j in range(length):
            sequence += series[i+j]
        sequences.append(sequence)
    
    return sequences
    
