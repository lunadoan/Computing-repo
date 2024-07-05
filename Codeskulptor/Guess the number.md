Hello! 

In "Guess the number" game, you'll play with computer.

Computer picks a secret number in a predefined range (range from 0 to 100 or range from 0 to 1000) and you'll guess what the number is. For each guess, computer will respond whether the number is higher, lower to the guess. If you guess the number right, you win, and new game will automatically start.

If you run out of guesses yet still not find the number, game is over. A new game will also automatically start.

[Play game here](https://py3.codeskulptor.org/#user309_p2lFVLUeqL_0.py)

If does not work, try open it from Chrome browser.

*Note*:
Strategy to guess the number: mimic the computer's "binary search" algorithm. Try to narrow the range each guess. With this strategy, you'll always find the number after n guess where 2^n >= the range.
