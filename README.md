# automate-boring-stuff-solutions
My solutions to problems posed in "Automate The Boring Stuff with Python"

After a bunch of self directed projects, I think it is about time that I started following a book on the important components of coding in python.  This was prompted by my overzealous attempt to take on multiple projects that were too big for me to handle.  This file will be used as a short description of each project, bonus features that I may have added, and notes about what I learned from each project.

**Chapter 3:**

- Project 1:  [collatz.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%203/collatz.py)  
  - Used the collatz sequence to make a function that takes any positive integer as an argument and prints the collatz sequence (which always converges to 1, eventually).  
  - My first time learning about and using 'try' and 'except' statements.  
  - ***Bonus feature***:  I made it so the user can continue to test sequence with different integers and quit the program by typing in 'q' and pressing enter.

**Chapter 4:**

- Project 1: [comma-code.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%204/comma-code.py)  
  - A simple program that turns a list into a string with commas in between each item and ', and' before the last item.  This was mostly review and a nice warm up to using lists.

- Project 2: [coin-flip-streaks.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%204/coin-flip-streaks.py)  
  - This program will count the amount of streaks of either heads or tails >= 6 in a list of 100 randomly generated "coin flips".  This is performed 10,000 times to get a stastical idea of how often streaks occur.  Another fun project with lists.

- Project 3: [character-picture-grid.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%204/character-picture-grid.py)  
  - Simply printing an image with characters and the list data type in a 2x2 format.  This problem was quite mind bending at first, but once I wrapped my head around how the loop was working with the list I got it down.  Working with multi-dimensional systems can be difficult at first.
  
  
**Chapter 5:**

- Project 1: [chess-dictionary-validator.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%205/chess-dictionary-validator.py)
  - Checks a dictionary of locations (keys) and piece types (items) of a chess board in a dictionary and returns "True" if the board is valid
  - First time learning about and using dictionaries.  This project was very challenging at first, but proved to be another great coding experience.
  - ***Bonus feature***: I noticed the author of ATBS overlooked one criteria of validity for a chess board!  Bishops are the only pieces that cannot exist on the same color.  This was a pretty difficult feature to implement and it probably doubled my project time (worth it, though!).  I made it so the function can detect if you have placed both of your bishops on white or both on black spaces.  I also added a feature that prints a message to the user stating why the board is invalid, and simply states "Pass" if it is valid.
  
- Project 2: [fantasy-inventory.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%205/fantasy-inventory.py)
  - A basic dictionary exercise, more use of .items(), .setdefault(), and other basic dictionary functions.  This project was very short as the templates were provided.
  
  **Chapter 6:**
  
- Project 1: [print-table.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%206/print-table.py)
  - Takes a list of lists and prints them in a neat right-justified format
  - Learned some important methods to be used with strings and user input validation
  - ***Bonus feature*** I added the ability for the function to put a title above the table in the format '-----title-----' (to the correct width of the table)
