string1 = '(this was a (triumph), I am making a note here huge success!)'
string2 = ';A[aa]B[22];'


def find_closing_bracket(input_string, starting_index):
    if input_string[starting_index] != '(':
        raise ValueError('not an opening bracket')
    
    sum = 1
    current_index = starting_index + 1
    while sum != 0:
        if input_string[current_index] == '(':
            sum += 1
        elif input_string[current_index] == ')':
            sum -= 1
        current_index += 1
    return current_index - 1

if __name__=='__main__':
    string_length = len(string1)
    closing_bracket_index = find_closing_bracket(string1, 12) 
    print(string_length, closing_bracket_index)