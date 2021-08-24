# Draft Acceptance Test
If the draft is started from the main menu, the first prompt the user will see is:
> "Would you like to start the Draft? Y/N: "

If the user chooses "Y" then the draft will start normally.  If an "N" is entered, then the user will have to restart the program.

When prompted by the console to enter a players name for your team.  
As a User, you would want to type in the name of the player in which you would like
to draft to your team.  For example, the prompt would say:
> "Enter the QB's name you would like to draft (Case Sensitive): "

As an example you would type in "Tom Brady" and if that player is not taken, then he would be added to your team.
If the player is taken already by another user or bot, or the user spells the name wrong, you will get the following message:
> "That player is not a QB or was spelled wrong! Enter another QB's name you would like to draft (Case Sensitive): "

The same will be asked for your other positions that you need for a full team.
Once that is completed, the console should print out a list of players that you have in your team, then the bot teams will be randomly generated.
# Output
For example: Your team consists of: {'QB': 'Tom Brady', 'RB': 'James Conner', 'WR': 'Damion Ratley', 'TE': 'Zach Ertz', 'K': 'Wil Lutz', 'LB': 'Nate Gerry', 'DB': 'Lano Hill'}
