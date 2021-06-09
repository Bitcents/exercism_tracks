class Allergies:

    def __init__(self, score) -> None:
        self.score = score

    def allergic_to(self, item) -> bool:
        return item in self.lst

    @property
    def lst(self):
        possbile_allergies = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }
        return [k for k,v in possbile_allergies.items() if self.score & v > 0]
