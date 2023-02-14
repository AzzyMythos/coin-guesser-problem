This is a coin flipping simulator to simulate the problem described by Veritasium's video: https://www.youtube.com/watch?v=XeSu9fBJ2sI

This program currently only supports adjustments to be made in the code before being ran.

Variables:
flips - Number of times the coin is flipped
coin - Creates a coin object with varying ratios of heads to tails. (i.e. Coin(50, 50) for a fair coin, Coin(85, 25) will land heads 85/110 times and tails 25/110 times)
num_head_guesses - Number of times to pick from pool of guessers when coin lands on heads
num_tail_guesses - Number of times to pick from pool of guessers when coin lands on tails
guessers - List of guessers. Append as many as you like.
Types of guessers
- HeadsGuesser - Only guesses heads
- TailsGuesser - Only guesses tails
- FairGuesser - Guesses heads or tails 50/50
- BiasedGuesser - Can be adjusted to guess heads or tails in different ratios, similar to coin. (i.e. A guesser BiasedGuesser("Name", 80, 20) will guess heads 80/100 times and tails 20/100 times.)

