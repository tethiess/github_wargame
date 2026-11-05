ASSIGNMENTS
===========

Card and Deck Classes: Zach & Tyler
Player class and game play: David & Liam


LEVEL #9 ASSIGNMENT
==================

IS 303 – Hilton

Create a Python card game based on the game of War.

This will be a group assignment. Your group will have four students, divided into
two programming pairs. One pair will develop the card and deck portion of the
program. The other pair will develop the player and game portion. The two pairs
will then combine their work into one finished program using GitHub.

The game should use two separate decks of cards, one for each player. The cards
should be shuffled before the game begins.

During each round, both players draw a card. The player with the higher card
wins the round and collects both cards. If the cards have the same value, the
players go to war. Each player should draw another card. The player with the
higher card wins all of the cards played during the war. If the cards have the
same value again, continue the war until there is a winner.

Continue playing until one player has collected all of the cards.

Your program should include:
  - A Card class to represent individual cards
  - A Deck class to represent a deck of cards
  - A Player class to represent each player
  - At least two separate Deck objects
  - At least two Player objects
  - A list containing multiple Card objects
  - Methods that allow the cards, decks, and players to interact
  - A loop to continue playing rounds
  - Appropriate messages showing what happens during the game
  - A final message identifying the winner

Organize your program into at least three Python files. For example:
  main.py
  cards.py
  player.py

One pair should work on the Card and Deck classes. The other pair should work
on the Player class and the game play. Both pairs should contribute to testing
and combining the completed program.

Your output does not need to match the sample session exactly, but it should
provide equivalent information.


SAMPLE SESSION
==============

Welcome to Two-Deck War!
Player 1 drew the 9 of Hearts.
Player 2 drew the 4 of Spades.
Player 1 wins the round!
Player 1 has 53 cards.
Player 2 has 51 cards.
Press Enter to play the next round.

Player 1 drew the Queen of Clubs.
Player 2 drew the Queen of Diamonds.
War!
Player 1 drew the 7 of Hearts.
Player 2 drew the 3 of Clubs.
Player 1 wins the war!
Player 1 has 56 cards.
Player 2 has 48 cards.
...
Player 1 has collected all of the cards.
Player 1 wins the game!


NOTES
=====

  - Use appropriate classes and object instances.
  - Create a separate object for each card, deck, and player.
  - Use meaningful variable, method, and class names.
  - Make sure each pair can explain how its portion of the program works.
  - Use comments where they help explain important parts of the program.
  - Test your program with normal rounds, ties, repeated ties, and the end of
    the game.
  - Your program should run by executing main.py.

Submit your PUBLIC GitHub link via Canvas.
