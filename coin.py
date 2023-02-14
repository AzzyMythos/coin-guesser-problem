import random

# Coin that can be adjusted with different heads to tails probabilities
class Coin():
    def __init__(self, heads_probability, tails_probability):
        self.total_probability = heads_probability + tails_probability
        self.hp = heads_probability
        self.tp = tails_probability
        self.flips = 0
        self.landed_heads = 0
        self.landed_tails = 0

    def flip(self): # Heads is 1, tails is 0
        self.flips += 1
        answer = random.randrange(0, self.total_probability)
        if (answer < self.hp):
            self.landed_heads += 1
            return 1
        else:
            self.landed_tails += 1
            return 0

    def print_stats(self):
        if (self.flips > 0):
            print("Coins flipped: {0}\nHeads: {1}\nTails: {2}\nHeads Ratio: {3}\nTails Ratio: {4}\n".format(self.flips, self.landed_heads, self.landed_tails, (self.landed_heads/self.flips), (self.landed_tails/self.flips)))
