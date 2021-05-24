import re

def is_pangram(sentence: str) -> bool:
    letters = dict()
    pattern = re.compile(r"[a-z]")
    for l in sentence:
        d = l.lower()
        if pattern.match(d):
            if d in letters:
                continue
            else:
                letters[d] = True
    
    if len(letters) == 26:
        return True
    
    return False


