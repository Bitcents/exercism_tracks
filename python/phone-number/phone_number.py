class PhoneNumber:
    def __init__(self, number: str):
        import re
        pattern1 = re.compile(r"(\+?1)?(\()?\d\d\d(\))?[-.\s]\d\d\d[-.\s]\d\d\d\d")
        pattern2 = re.compile(r"\d\d\d\d\d\d\d\d\d\d")
        if pattern1.match(number) or pattern2.match(number):
            self.number = number.translate({ord(i): None for i in '-(). '})[-10:]
        else:
            raise ValueError('input is not valid')
        if len(self.number) > 11:
            raise ValueError('number too long')
    
    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'