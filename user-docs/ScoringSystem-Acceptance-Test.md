# Scoring System Acceptance Test

The scoring system is used to help the user calculate the total points earned in a week from the games their team has played in.

As a user, you will not have to type in anything input wise, as the ScoringSystem.py handles everything.  For example if the user had Tom Brady on their team
and he threw 3 Passing Touchdowns in the first week, then the code snippet:

>if passing_tds >= 1:
>  passing_tds_points = passing_tds * 4
>  offensive_score += passing_tds_points
>else:
>  offensive_score += 0

This code will pass in the 3 touchdowns that Tom Brady threw, then giving the user 12 points towards their weekly score.
The same can be said for the defense and special teams.

# Output

As of right now, there is no output for the scoring system.  The Scoring System does everything in the backend of the program.  Later on, there will be an output that displays to the user how many points their team scored.  As well as the bot teams.

