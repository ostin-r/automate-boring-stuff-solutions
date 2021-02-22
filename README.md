# automate-boring-stuff-solutions
My solutions to problems posed in "Automate The Boring Stuff with Python"

After a bunch of self directed projects, I think it is about time that I started following a book on the important components of coding in python.  This was prompted by my overzealous attempt to take on multiple projects that were too big for me to handle.  This file will be used as a short description of each project, bonus features that I may have added, and notes about what I learned from each project.

**Chapter 3: Functions**

- Project 1:  [collatz.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%203/collatz.py)  
  - Used the collatz sequence to make a function that takes any positive integer as an argument and prints the collatz sequence (which always converges to 1, eventually).  
  - My first time learning about and using 'try' and 'except' statements.  
  - ***Bonus feature***:  I made it so the user can continue to test sequence with different integers and quit the program by typing in 'q' and pressing enter.

**Chapter 4: Lists**

- Project 1: [comma-code.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%204/comma-code.py)  
  - A simple program that turns a list into a string with commas in between each item and ', and' before the last item.  This was mostly review and a nice warm up to using lists.

- Project 2: [coin-flip-streaks.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%204/coin-flip-streaks.py)  
  - This program will count the amount of streaks of either heads or tails >= 6 in a list of 100 randomly generated "coin flips".  This is performed 10,000 times to get a stastical idea of how often streaks occur.  Another fun project with lists.

- Project 3: [character-picture-grid.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%204/character-picture-grid.py)  
  - Simply printing an image with characters and the list data type in a 2x2 format.  This problem was quite mind bending at first, but once I wrapped my head around how the loop was working with the list I got it down.  Working with multi-dimensional systems can be difficult at first.
  
  
**Chapter 5: Dictionaries & Structuring Data**

- Project 1: [chess-dictionary-validator.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%205/chess-dictionary-validator.py)
  - Checks a dictionary of locations (keys) and piece types (items) of a chess board in a dictionary and returns "True" if the board is valid
  - First time learning about and using dictionaries.  This project was very challenging at first, but proved to be another great coding experience.
  - ***Bonus feature***: I noticed the author of ATBS overlooked one criteria of validity for a chess board!  Bishops are the only pieces that cannot exist on the same color.  This was a pretty difficult feature to implement and it probably doubled my project time (worth it, though!).  I made it so the function can detect if you have placed both of your bishops on white or both on black spaces.  I also added a feature that prints a message to the user stating why the board is invalid, and simply states "Pass" if it is valid.
  
- Project 2: [fantasy-inventory.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%205/fantasy-inventory.py)
  - A basic dictionary exercise, more use of .items(), .setdefault(), and other basic dictionary functions.  This project was very short as the templates were provided.
  
**Chapter 6: Manipulating Strings**
  
- Project 1: [print-table.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%206/print-table.py)
  - Takes a list of lists and prints them in a neat right-justified format
  - Learned some important methods to be used with strings and user input validation
  - ***Bonus feature*** I added the ability for the function to put a title above the table in the format '-----title-----' (to the correct width of the table)
  
- Project 2: [myzombie.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%206/myzombie.py)
  - I had way too much fun with this project.  The author implemented a simulator for the game "zombie dice" and made it so you can make a bot and run it in tournaments against other bots.
  - This project was my first time dealing with classes & methods directly, and although they are outside of the scope of this textbook I still ended up having to make my own method and learn a little bit about them.
  - ***My Bot Bonus Feature:*** I started off by creating a bot that did the same thing as the "Stop at 2 shotguns bot" as it was consistently winning tournaments.  I added a feature that takes into account the color of the die that have already been rolled and will roll again, even if the zombie has already been hit by two shotguns.  Specifically, if all three of the red die (risky die) have already been rolled, my bot will take a chance on one more roll since only green and yellow die are in the cup.  This intuition, however, did not beat the "stop at 2 shotguns" bot.  I ran 10 tournaments of 1000 games and my bot came out on top 40% of the time with "stop at 2 shotguns" beating me out the other times.  I don't know how Al's "zombiedice" package works, and if it doesn't actually reset the cup then my extra code doesn't do anything except make my bot do worse.  I could look more into this later but I'm happy with calling this project complete.

**Chapter 7: Pattern Matching with Regular Expressions**

- Follow along project: [email-phone-extractor.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/follow-along/email-phone-extractor.py)
  - ***Bonus feature:*** I don't talk about the follow along projects unless I add something outside what is already given, so here it is.  This program takes text from the clipboard and checks for emails and phone numbers.  I added a feature (which probably could've just been a separate program) that detects different formats of dates and puts them all in the format of either mm/dd/yy or m/d/yy.  I could go further and refine it to only do dd/mm/yy, but i'm okay with how far i've taken this feature since I had to wrestle with re.sub(), .findall(), and .search() plenty already.

- Project 1: [date-detection.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%207/date-detection.py)
  - Turns out my bonus feature from the follow along project was a good warm up.  This program detects dates from text provided by the clipboard.
  - I made it so it can detect multiple dates with .findall() and then checks wether those dates are valid (assuming the author's assumption that the dates are in the format dd/mm/yyyy and only span years 1000 to 2999).  It seems like the author wanted it to be a bit simpler and only detect one date, but I think making it detect all dates made it a fun challenge.
  - Learned about list comprehension in order to delete invalid values.  I did this in a bit of a roundabout way where I just replaced invalid dates with "0" while in the loop, then used list comprehension to delete any 0s.  If I went deeper into this I would probably figure out how to use del, .remove() or .pop(), but I had the added complexity of having three lists that needed to correspond to eachother.  So if I wanted to delete an invalid day I needed to figure out it's index and delete the corresponding "month".  That being said, learning about list comprehension was pretty fun.

- Project 2: [detect-password-strength.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%207/detect-password-strength.py)
  - A quick exercise with more regular expression fun
  - Tests a password for 8 characters, one lower case letter, one upper case letter, and one number.  Returns 'strong' if it passes all of these tests.

- Project 3: [regex-strip.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%207/regex-strip.py)
  - A function that mimics the .strip() method for strings by using regular expressions
  - learned how to insert a variable into a regex statement.  This proved to be more difficult than expected and I ended up taking a few steps back and learning about strings in regex.
  - **Limitations:** The function I wrote cannot strip a specific string in order.  For example, 'bananas-austin-abanasab' will still strip to '-austin-' if 'bananas' is passed as the strip argument, because regex is matching any character in 'bananas'.  I think this could be fixed by making a loop that generates a regex expression such as 'b.*a.*n.*a.*....' and uses this in the regex before continuing with the rest of the function.

**Chapter 8: Input Validation with PyInputPlus**
- Project 1: [sandwich-maker.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%208/sandwich-maker.py)
  - A really fun introduction to pyinputplus by making a program that asks users for sandwich preferences and then gives them a final cost
  - Learned about the importance of data validation and how to use PyInputPlus to take a lot of weight off of my own code writing
  - It was difficult getting a final cost together at the end, because all of the sandwich componenets were stored in different variables.  If I were to start this project again, I would make a list where all of the ingredients are located.  This would make the get_cost() function much easier & quicker to use.

- Project 2: [minimal-multiply-quiz](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/Chapter%208/minimal-multiply-quiz.py)
  - This project is paired with the follow along project [multiply-quiz.py](https://github.com/ostin-r/automate-boring-stuff-solutions/blob/main/follow-along/multiplication-quiz.py)
  - minimal-multiply-quiz.py does the same thing as the follow along project, but without using pyinputplus (spoiler alert: pyinputplus does a lot of work for you in the background)
  - The thing that I missed the most from pyinputplus was the "timeout" key word argument.  Implementing timeout functionality took most of the development time while I wrapped my head around how to fit it into the loops.
