class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    # we try to handle trivial cases first
    # empty string is not a valid input 
    # the cases given here are not exhaustive
    # a better way of handling almost all such cases
    # would be to use a regular expression 
    # we will ignore that for now 
    if input_string == '':
        raise ValueError('empty string is not a valid input')
    # opening and closing brackets only 
    # is not a valid input
    if input_string == '()':
        raise ValueError('SGF tree has no nodes')  
    # semi-colon only is not a valid input
    if input_string == ';':
        raise ValueError('SGF node has no associated tree')
    if input_string == "(;)":
        return SgfTree()

    # the parser will have a different flow
    # if there are variations included 
    # the 'has_variations' variable will track this
    has_variations = False
    # the first thing to do would be to 
    # get the variations in the SGF tree
    get_variation_children(input_string)

    # the next step would be to 
    # get the children if no variations exist
    get_children(input_string)

    # then we parse the properties of the SGF tree
    parse_properties(input_string)
    

def find_closing_bracket(input_string, starting_index):
    sum = 1
    current_index = starting_index + 1
    while sum != 0:
        if input_string[current_index] == '(':
            sum += 1
        elif input_string[current_index] == ')':
            sum -= 1
        current_index += 1
    return current_index - 1

def get_variation_children(input_string):
    pass

def get_children(input_string):
    pass

def parse_properties(input_string):
    pass 