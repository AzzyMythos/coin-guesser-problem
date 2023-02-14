import random

# Guesser base class
class Guesser():
    def __init__(self, name):
        self.name = name
        self.guesses = 0
        self.correct_guesses = 0

    def guess(self, answer):
        pass

    def print_stats(self):
        if self.guesses > 0:
            print("{0} stats\nGuesses: {1}\nCorrect guesses: {2}\nCorrect ratio: {3}\n".format(self.name, self.guesses, self.correct_guesses, (self.correct_guesses/self.guesses)))

# Only ever guesses heads
class HeadsGuesser(Guesser):
    def __init__(self, name):
        if (name == ""):
            name = "Heads Guesser"
        super().__init__(name)

    def guess(self, answer):
        self.guesses += 1
        if (answer == 1):
            self.correct_guesses += 1

# Only ever guesses tails
class TailsGuesser(Guesser):
    def __init__(self, name):
        if (name == ""):
            name = "Tails Guesser"
        super().__init__(name)

    def guess(self, answer):
        self.guesses += 1
        if (answer == 0):
            self.correct_guesses += 1

# Guesses heads or tails 50/50
class FairGuesser(Guesser):
    def __init__(self, name):
        if (name == ""):
            name = "Equal Guesser"
        super().__init__(name)

    def guess(self, answer):
        self.guesses += 1
        guess = random.randrange(0,2)
        if (answer == guess):
            self.correct_guesses += 1

# Can adjust ratio of guessing heads to tails
class BiasedGuesser(Guesser):
    def __init__(self, name, heads_probability, tails_probability):
        if (name == ""):
            name = "Biased Guesser"
        super().__init__(name)
        self.total_probability = heads_probability + tails_probability
        self.hp = heads_probability
        self.tp = tails_probability

    def guess(self, answer):
        self.guesses += 1
        guess = random.randrange(0, self.total_probability)
        if (guess < self.hp):
            actual_guess = 1
        else:
            actual_guess = 0
        if (answer == actual_guess):
            self.correct_guesses += 1
