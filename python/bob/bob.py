import re

def response(hey_bob):
    
    if hey_bob == "":
        return 'Fine. Be that way!'

    ignore_character = re.compile(r'[./-_,?!\s]')
    is_question = False
    is_all_capitalized = True

    # check if the prompt is a question
    if hey_bob[-1] == '?':
        is_question = True
    
    # check if all the letters are capitalized
    for letter in hey_bob:

        if ignore_character.match(letter):
            continue
        if letter.islower():
            is_all_capitalized = False