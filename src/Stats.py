import nflgame

class Stats:
    '''
    The Stats class deals with retrieving data from the NFLGame API and returning them to the program.
    '''
    def __init__(self):
        pass
    #add self when done
    def import_stats(self):
        '''
        import_stats is a method that pulls stats from games per NFLGame API and returns a JSON file
        of the specific stat a user is looking for.

        Args:
            None

        Returns:
            msg : msg is a string that prints out the number of yards, tds, carries, etc. according to what
                        is being asked.
        '''
        week = 1
        print("Stats!")

        print("Week 1\n")
        #week = int(input("Enter what week you would like to do! \n"))
        #Offense
        #Top 5 RBs
        print("Rushing")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.rushing().sort('rushing_yds').limit(5):
            msg = '%s carried %d times for %d yards and %d touchdowns'
            print(msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds))

        print("")

        #passing
        print("Passing")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.passing().sort('passing_yds').limit(5):
            msg = '%s passed %d times for %d yards and %d touchdowns'
            print(msg % (p, p.passing_att, p.passing_yds, p.passing_tds))

        print("")

        #recieving
        print("Receiving")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.receiving().sort('receiving_yds').limit(5):
            msg = '%s received %d times for %d yards and %d touchdowns'
            print(msg % (p, p.receiving_rec, p.receiving_yds, p.receiving_tds))

        print("")

        print("Two Point Conv")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.passing().sort('passing_twoptm').limit(5):
            if p.passing_twoptm > 0:
                msg = '%s threw for %d two point conversion during the game.'
                print(msg % (p, p.passing_twoptm))
            else:
                continue
        for p in players.receiving().sort('receiving_twoptm').limit(5):
            if p.receiving_twoptm > 0:
                msg = '%s received for %d two point conversion during the game.'
                print(msg % (p, p.receiving_twoptm))
            else:
                continue
        for p in players.rushing().sort('rushing_twoptm').limit(5):
            if p.rushing_twoptm > 0:
                msg = '%s rushed for %d two point conversion during the game.'
                print(msg % (p, p.rushing_twoptm))
            else:
                continue

        print("")

        print("Fumbles")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.fumbles().sort('fumbles').limit(5):
            if p.fumbles_lost > 0:
                msg = '%s fumbled %d time(s) during the game.'
                print(msg % (p, p.fumbles_lost))
            else:
                continue

        print("")
        print("Interceptions")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.passing().sort('passing_ints').limit(5):
            msg = '%s threw %d interception(s) during the game.'
            print(msg % (p, p.passing_ints))


        #Defense
        print("")
        print("Defensive Touchdowns")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.defense().sort('defense_tds').limit(5):
            msg = '%s got %d touchdown(s) during the game.'
            print(msg % (p, p.defense_tds))

        print("")
        print("Fumbles Recovered")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.fumbles().sort('fumbles_rec').limit(5):
            msg = '%s recovered a fumble during the game.'
            print(msg % (p))


        print("")
        print("Interceptions Caught")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.defense().sort('defense_int').limit(5):
            msg = '%s caught %d interception(s) during the game.'
            print(msg % (p, p.defense_int))

        print("")
        print("Sacks")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.defense().sort('defense_sk').limit(5):
            msg = '%s got %d sack(s) during the game.'
            print(msg % (p, p.defense_sk))

        print("")
        print("Safeties")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.defense().sort('defense_safe').limit(5):
            msg = '%s got a tackle during the game, resulting in a safety.'
            print(msg % (p))

        print("")
        print("Fumbles Forced")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.defense().sort('defense_ffum').limit(5):
            msg = '%s forced %d fumble(s) during the game. '
            print(msg % (p, p.defense_ffum))

        print("")
        print("Field Goals Made")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.kicking().sort('kicking_fgm').limit(5):
            msg = '%s forced %d and %d during the game. '
            print(msg % (p, p.kicking_fgm, p.kicking_fgm_yds))

        print("")
        print("Extra Points")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.kicking().sort('kicking_xpmade').limit(5):
            msg = '%s successfully made %d extra point(s) during the game. '
            print(msg % (p, p.kicking_xpmade))

        print("")
        print("Quarterback Hits")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.defense().sort('defense_qbhit').limit(5):
            msg = '%s successfully got a quarterback hit during the game. '
            print(msg % (p))

        print("")
        print("Tackle Assist")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.defense().sort('defense_ast').limit(5):
            msg = '%s assisted %d tackle(s) during the game. '
            print(msg % (p, p.defense_ast))

        print("")
        print("Solo Tackles")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.defense().sort('defense_tkl').limit(5):
            msg = '%s got %d solo tackle(s) during the game. '
            print(msg % (p, p.defense_tkl))

        print("")
        print("Pass Defensed")
        games = nflgame.games(2019, week = week)
        players = nflgame.combine_game_stats(games)
        for p in players.defense().sort('defense_pass_def').limit(5):
            msg = '%s stopped %d passed from being completed during the game. '
            print(msg % (p, p.defense_pass_def))

if __name__ == "__main__": #Remove when running tests
    import_stats()
