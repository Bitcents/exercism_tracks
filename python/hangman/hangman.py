# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.__word = word
        self.remaining_characters = set()
        self.guessed_characters = set()
        for letter in word:
            self.remaining_characters.add(letter)

    def guess(self, char):
        # Check if the game is still going on
        if self.status != STATUS_ONGOING:
            raise ValueError('game is over')
        
        if char in self.remaining_characters:
            self.remaining_characters.remove(char)
            self.guessed_characters.add(char)
            if len(self.remaining_characters) == 0:
                    self.status = STATUS_WIN
        elif char in self.guessed_characters:
            self.remaining_guesses -= 1
        else:
            self.remaining_guesses -= 1
        # Check if there are any guesses left
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
  

    def get_masked_word(self):
        masked_word = ""
        for letter in self.__word:
            if letter in self.remaining_characters:
                masked_word += '_'
            else:
                masked_word += letter
        return masked_word

    def get_status(self):
        return self.status
