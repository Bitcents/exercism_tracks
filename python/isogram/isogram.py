def is_isogram(string) -> bool:
    # storing the letters in a dictionary
    # can help us to quickly identify 
    # letters that have been encountered before
    letters = {}
    # We need to be case-insensitive; hence the lower method
    for letter in string.lower():
        if letter == '-' or letter == ' ':
            continue
        if not letter in letters:
            letters[letter] = 1
        else:
            return False
    # reaching this stage means no repeating
    # letters have been found; the word is an isogram
    return True
