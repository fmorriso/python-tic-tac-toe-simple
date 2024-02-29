# Tic-Tac-Toe Game - Simple
A simple Tic-Tac-Toe game with no GUI other than what the built-in print() statement provides.

## Developer Notes
* Extensive use of Enum, IntEnum and StrEnum to reduce/eliminate "magic strings" in favor or strongly typed enumerations. 
* [Article: Eliminating Python "Code Smells"](https://www.arjancodes.com/blog/best-practices-for-eliminating-python-code-smells)
  I am particularly fond of tip #4, "magic numbers" because it also applies to "magic strings" 
  such as "X" and "O" in tic-tac-toe as well as game status/outcomes such as
  "X is the winner" or "it's a tie".
  I use several enumerations in this project to overcome this specific "code smell"
## Change Log
* 2024-02-28 - (Firewalled Replit only) Refactored enumerations to use inherit from Enum instead of IntEnum and StrEnum, the later two being
new as of python 3.11.
* 2024-02-20 - Refined logic to spot hopelessly tied game earlier.
* 2024-02-19 - Add more logic to determining winner, tie, in progress
* 2024-02-14 - Initial start of coding
* 2024-02-15 - moved play again method inside the game and changed BoardLocation to inherit from IntEnum
* 2024-02-16 - begin to design
## Tools
* Python 3.12.2 (minimum required level is 3.10 due to use of match statement)
* PyCharm Community 2023.3.3
* VSCode 1.86.1