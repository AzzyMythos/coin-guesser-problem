import random
import time
from guessers import *
from coin import Coin

def main():
    start_time = time.time()
    flips = 1000000
    coin = Coin(80, 20)
    num_of_heads_guesses = 1
    num_of_tails_guesses = 5
    experiment(flips, coin, num_of_heads_guesses, num_of_tails_guesses)
    print("Run time {0}".format(time.time() - start_time))
    return

def experiment(flips, coin, h, t):
    guessers = []
    guessers.append(FairGuesser("Equal Only"))
    guessers.append(BiasedGuesser("Biased Only", 80, 20))
    guessers.append(BiasedGuesser("Biased Only", 20, 80))
    guessers.append(HeadsGuesser("Heads Only"))
    guessers.append(TailsGuesser("Tails Only"))

    for x in range(flips):
        answer = coin.flip()
        # If coin is heads (1), pick h number of people to guess heads or tails
        if (answer == 1):
            guess(guessers, h, answer)
        else:
        # If coin is tails (0), pick t number of people to guess heads or tails
            guess(guessers, t, answer)

    coin.print_stats()
    for x in range(len(guessers)):
        guessers[x].print_stats()


# Runs through x number of guesses each time picking a guesser from pool of guessers
def guess(guessers, num_tries, answer):
    num_of_guessers = len(guessers)
    for x in range(num_tries):
        picker = random.randrange(0, num_of_guessers)
        guessers[picker].guess(answer)


if __name__ == "__main__":
    main()
