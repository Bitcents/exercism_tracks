def create_histogram(word):
    # this function basically creates
    # a frequency chart of the different
    # letters in the word
    histogram = {}
    for letter in word:
        if not letter in histogram:
            histogram[letter] = 1
        else:
            histogram[letter] += 1
    return histogram

def find_anagrams(word, candidates):
    normalized = word.lower()
    base_histogram = create_histogram(normalized)
    anagrams = []
    # compare the base histogram with 
    # histograms of candidates
    for candidate in candidates:
        normalized_candidate = candidate.lower()
        if normalized_candidate == normalized:
            continue
        if base_histogram == create_histogram(normalized_candidate):
            anagrams.append(candidate)
    
    return anagrams