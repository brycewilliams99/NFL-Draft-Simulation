
import nflgame
import random
from os import system, name

'''
The Draft class deals with the fantasy league distribution of players to the teams participating.
'''
class Draft:
    '''
    Methods:
        player_pick(): Function that helps the user draft the players they want onto their team.

    Returns:
        user_team (dict): A dictionary that has the users players.
    '''

    def __init__(self):
        '''
        __init__ is used to initialize local variables.
        '''
        self.taken = []
        self.pos_list = ['QB','RB','WR','TE','K','LB','DB']

        self.user_team = {}
        #Dictionary to store users players.
        self.bot_team = {}
        self.bot_team1 = {}
        self.bot_team2 = {}
        self.bot_team3 = {}


    #qb_pos = 'QB'
    #rb_pos = 'RB'      These are just place holders used for reference, will be deleted
    #wr_pos = 'WR'      in the end.
    #te_pos = 'TE'
    #kicker_pos = 'K'
    #def_pos = 'D/SP'


    def player_pick(self, pos, taken, user_team):
        '''
        player_pick is a function that is used to let the user pick and choose who they want on their team.

        Args:

            pos (str):      The first argument is a string that is pre-defined, so the user would not
                            see this variable until they are done with the draft.

            taken (list):   The second argument is a list that stores all of the players that have already
                            been drafted by other users.

            user_team (dict): user_team is a dictionary that stores all of the players that the user has on
                                his/her team.

        Returns:
            dict: function returns a dictionary that holds the users picks.  It is formatted so that it is
                  {pos_name, pos} EX: {Tom Brady: QB}

                  If the name player is already taken, it returns an error message that the player is taken already.
        '''
        player_list = []
        games = nflgame.games(2019, 2, kind='REG')
        players = nflgame.combine_game_stats(games)
        meta = nflgame.players
        print()
        print(pos)
        for player in players:
            if player.player.position in [pos]:
                print(meta[player.playerid].name)
                player_name = meta[player.playerid].name
                player_list.append(player_name)

        print()
        pos_name = input("Enter the " + pos + "'s name you would like to draft from above list (Case Sensitive): ")
        print()

        hit = False
        while hit == False:
            #Check to see if the player is already taken.
            if pos_name in taken:
                #If the player is already taken, then error message is given.
                pos_name = input("He is taken! Enter another " + pos +"'s name you would like to draft (Case Sensitive): ")
            elif pos_name not in player_list:
                pos_name = input("That player is not a " + pos +" or was spelled wrong! Enter another " + pos +"'s name you would like to draft (Case Sensitive): ")
            else:
                #If player is available, it will print out that player was added.
                print(pos_name + " was added to your team!")
                #Player is then added to the taken list.
                self.taken.append(pos_name)
                #Player stored in Users team.
                self.user_team[pos]=pos_name
                hit = True


    def bot_pick(self, pos, taken, bot_team):
            '''
            bot_pick is a function that is used to randomly generate bot teams for user to play against.

            Args:

                pos (str):      The first argument is a list of all of the positions so they can be looped through.

                taken (list):   The second argument is a list that stores all of the players that have already
                                been drafted by other users.

                bot_team (dict): bot_team is a dictionary that stores all of the players that the bot has on
                                    its team.

            Returns:
                dict: function returns a dictionary that holds randomly generated teams for the bots.  It is formatted so that it is
                      {pos_name, pos} EX: {Tom Brady: QB}
            '''
            player_list = []
            games = nflgame.games(2019, 2, kind='REG')
            players = nflgame.combine_game_stats(games)
            meta = nflgame.players
            for player in players:
                if player.player.position in [pos]:
                    player_name = meta[player.playerid].name
                    player_list.append(player_name)


            hit = False
            while hit == False:
                pos_name = random.choice(player_list)
                if pos_name in taken:
                    hit = False
                else:
                    self.taken.append(pos_name)
                    self.bot_team[pos]=pos_name
                    hit = True



    def draft_start(self):
        '''
        draft_start is a method that takes care of the draft simulation as a whole.

        Args:

            self: The self argument is just the data that is being called from the Draft class.

        Returns:

            The method returns the dictionaries for the user and the three bot teams that are participating.
        '''

        print("Welcome to the Draft!")
        choice_draft_check = 0
        choice_draft = input("Would you like to start the Draft? Y/N: ")
        while choice_draft_check != 1:
            if choice_draft == "Y" or "y":
                choice_draft_check += 1
            elif choice_draft == "N" or "n":
                print("Restart Program")
                return
            else:
                choice_draft = input("Invalid choice! Would you like to start the Draft? Y/N: ")

        #User Team
        for pos in self.pos_list:
            self.player_pick(pos, self.taken, self.user_team)

        print("Your team consists of: " + str(self.user_team))
        print ()

            #Bot 1 Team
        self.bot_team1 = self.bot_team
        for pos in self.pos_list:
            self.bot_pick(pos,self.taken,self.bot_team)

        print("Bot 1 team consists of: " + str(self.bot_team1))
        print()

        #Bot 2 Team
        self.bot_team2 = self.bot_team
        for pos in self.pos_list:
            self.bot_pick(pos,self.taken,self.bot_team)

        print("Bot 2 team consists of: " + str(self.bot_team2))
        print()

        #Bot 3 Team
        self.bot_team3 = self.bot_team
        for pos in self.pos_list:
            self.bot_pick(pos,self.taken,self.bot_team)

        print("Bot 3 team consists of: " + str(self.bot_team3))
        print()
