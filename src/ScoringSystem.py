'''
The class ScoringSystem handles all of the points that will be involved with the fantasy league.
'''

class ScoringSystem:
    '''

    Methods:

        offensive_scoring(): Gets all of the points that were earned by the offesive side of the
        user's team. Returns the variable offensive_score (int).

        defensive_scoring(): Gets all of the points that were earned by the defensive side of the
        user's team.  Returns the variable defensive_score (int).

        individual_defensive_scoring(): Gets all of the points that were earned by a singular
        defensive player that is on the user's team.  Returns the variable individual_def_score (int).

        special_teams_scoring(): Gets all of the points that were earned by the special teams
        on the user's team.  Returns the variable special_teams_score (int).

    Returns:

        All of the points that the user's team earned through a week.
    '''

    def offensive_scoring(passing_yds, passing_tds, passing_ints, rushing_yds, rushing_tds, receiving_yrds,
    receiving_tds, two_point_conv, fumbles):
        '''
        offensive_scoring adds up all the points that a team would receivingeive and
        prints out the total for offensive side.

        Args:

            passing_yds (int): Number of passing yard a player receivingeives.

            passing_tds (int): Number of passing touchdowns a player receivingeives from passing.

            pass_ints (int): Number of passing interceptions a player had thrown.
            rushing_yds (int): Number of yards one gained from rushing.
            rushing_tds (int): Number of touchdowns a player receivingeives from rushing.
            receiving_yrds (int): Number of yards gained from receivingeiving the ball.
            receiving_tds (int): Number of touchdowns scored from receivingeiving
            two_point_conv (int): Number of two point conversions scored.
            fumbles (int): Number of fumbles committed.

        Returns:

            The functinon offensive_scoring() returns the variable offensive_score (int)
            which is the total number of points earned from the other variables that are
            present within the function.
        '''

        offensive_score = 0

        #Passing Yards
        if passing_yds >= 25:
            passing_yds_points = passing_yds // 25
            offensive_score += passing_yds_points
        else:
            offensive_score += 0

        #Passing Touchdowns
        if passing_tds >= 1:
            passing_tds_points = passing_tds * 4
            offensive_score += passing_tds_points
        else:
            offensive_score += 0

        #Passing Interceptions
        if passing_ints >= 1:
            passing_ints_points = passing_ints * -2
            offensive_score += passing_ints_points
        else:
            offensive_score += 0

        #Rushing Yards
        if rushing_yds >= 10:
            rushing_yds_points = rushing_yds // 10
            offensive_score += rushing_yds_points
        else:
            offensive_score += 0

        #Rushing Touchdowns
        if rushing_tds >= 1:
            rushing_tds_points = rushing_tds * 6
            offensive_score += rushing_tds_points
        else:
            offensive_score += 0


        #receivingeiving Yards
        if receiving_yrds >= 10:
            receiving_yrds_points = receiving_yrds // 10
            offensive_score += receiving_yrds_points
        else:
            offensive_score += 0

        #receivingeiving Touchdowns
        if receiving_tds >= 1:
            receiving_tds_points = receiving_tds * 6
            offensive_score += receiving_tds_points
        else:
            offensive_score += 0

        #2-Point Conversions
        if two_point_conv >= 1:
            two_point_conv_points = two_point_conv * 2
            offensive_score += two_point_conv_points
        else:
            offensive_score += 0

        #Fumbles
        if fumbles >= 1:
            fumbles_points = fumbles * -2
            offensive_score += fumbles_points
        else:
            offensive_score += 0

        return offensive_score



    def defensive_scoring(sacks, points_allow, defensive_score, sacks_points, intercepts, intercepts_points,
    fumbles_receiving, fumbles_receiving_points, safeties, safeties_points, def_tds, def_tds_points,
    kick_punt_tds, kick_punt_tds_points, def_two_point_conv, def_two_point_conv_points):
        '''
        defensive_scoring adds up all the total points a team would receivingieve
        from their defense and then prints out the score.

        Args:

            sacks (int): Number of sacks a player got.
            points_allow (int): Number of points that the defense let up.
            defensive_score (int): Total number of points a team receivingeived for the week.
            sack_points (int): Total number of points they receivingeived from sacks.
            intercepts (int): Number of interceptions a defender had.
            intercepts_points (int): Number of total points a team receivingeived from interceptions
            fumbles_receiving (int): Number of fumbeles a team got.
            fumbles_receiving_points (int): Total number of points that a team got from fumbles.
            safeties (int): Number of safeties
            safeties_points (int): Total number of points a team got from safeties.
            def_tds (int): Number of touchdowns a defender got.
            def_tds_points (int): Total points earned from touchdowns scored by defenders.
            kick_punt_tds (int): Total number of kick punt touchdowns.
            kick_punt_tds_points (int): Total points earned from kick punt touchdowns.
            def_two_point_conv (int): Number of two point conversions from defenders.
            def_two_point_conv_points (int): Total points a team receivingeived from two point conversions.

        Returns:

            the variable defensive_score for the total amount of points one
            earned from the function.
        '''
        defensive_score = 0
        #Sacks
        if sacks >= 1:
            sacks_points = sacks
            defensive_score += sacks_points
        else:
            defensive_score += 0

        #Interceptions
        if intercepts >= 1:
            intercepts_points = intercepts * 2
            defensive_score += intercepts_points
        else:
            defensive_score += 0

        #Fumbles receivingovered
        if fumbles_receiving >= 1:
            fumbles_receiving_points = fumbles_receiving * 2
            defensive_score += fumbles_receiving_points
        else:
            defensive_score += 0

        #Safeties
        if safeties >= 1:
            safeties_points = safeties * 2
            defensive_score += safeties_points
        else:
            defensive_score += 0

        #Defensive Touchdowns
        if def_tds >= 1:
            def_tds_points = def_tds * 6
            defensive_score += def_tds_points
        else:
            defensive_score += 0

        #Kick and Punt Return Touchdowns
        if kick_punt_tds >= 1:
            kick_punt_tds_points = kick_punt_tds * 6
            defensive_score += kick_punt_tds_points
        else:
            defensive_score += 0

        #2 Point Conversion Returns
        if def_two_point_conv >= 1:
            def_two_point_conv_points = def_two_point_conv * 2
            defensive_score += def_two_point_conv_points
        else:
            defensive_score += 0

        #Points Allowed
        if points_allow == 0:
            points_allow_points = 10
            defensive_score += points_allow_points
        elif 1<=points_allow<= 6:
            points_allow_points = 7
            defensive_score += points_allow_points
        elif 7<=points_allow<=13:
            points_allow_points = 4
            defensive_score += points_allow_points
        elif 14<=points_allow<=20:
            points_allow_points = 1
            defensive_score += points_allow_points
        elif 21<=points_allow<=27:
            defensive_score += 0
        elif 28<=points_allow<=34:
            points_allow_points = -1
            defensive_score += points_allow_points
        else:
            points_allow_points = -4
            defensive_score += points_allow_points

        return defensive_score

    def individual_defensive_scoring(solo_tackles, assist_tackles, sacks, sack_yrds,
    tackle_for_loss, qb_hits, pass_def, individual_intercepts, fumbles_forced):
        '''
        individual_defensive_scoring adds up all of the total points that a single defender
        would earn after a game.

        Args:

            solo_tackles (int): Number of solo tackles by a singluar player.
            assist_tackles (int): Assist tackles by one player.
            sacks (int): Number of sacks.
            sack_yrds (int): Number of yards lost from sack.
            tackle_for_loss (int): Number of yards lost from a tackle.
            qb_hits (int): Number of times a player hits a quarterback.
            pass_def (int): Number of times player made an incomplete pass.
            individual_intercepts (int): Number of interceptions caught.
            fumbles_forced (int): Number of times a fumble was forced by player.

        Returns:

            the int individual_def_score back to be added up in the total score.
        '''

        individual_def_score = 0
        #Solo Tackles
        if solo_tackles >= 1:
            individual_def_score += solo_tackles
        else:
            individual_def_score += 0

        #Assisted Tackles
        if assist_tackles >= 1:
            assist_tackles_points = assist_tackles * .5
            individual_def_score += assist_tackles_points
        else:
            individual_def_score += 0

        #Sacks
        if sacks >= 1:
            sacks_points = sacks
            individual_def_score += sacks_points
        else:
            individual_def_score += 0

        #Sack Yards
        if sack_yrds >= 10:
            sack_yrds_points = sack_yrds // 10
            individual_def_score += sack_yrds_points
        else:
            individual_def_score += 0

        #Tackle For Loss
        if tackle_for_loss >= 1:
            individual_def_score += tackle_for_loss
        else:
            individual_def_score += 0

        #Quarterback Hits
        if qb_hits >= 1:
            individual_def_score += qb_hits
        else:
            individual_def_score += 0

        #Passes Defended
        if pass_def >= 1:
            individual_def_score += pass_def
        else:
            individual_def_score += 0

        #Interceptions
        if individual_intercepts >= 1:
            individual_intercepts_points = individual_intercepts * 3
            individual_def_score += individual_intercepts_points
        else:
            individual_def_score += 0

        #Fumbles Forced
        if fumbles_forced >= 1:
            fumbles_forced_points = fumbles_forced * 3
            individual_def_score += fumbles_forced_points
        else:
            individual_def_score += 0

        return individual_def_score


    def special_teams_scoring(pat_made, fg_made):
        '''
        special_teams_scoring adds up the total points that a team receivingieves
        from scoring with special teams.

        Args:

            pat_made (int): Number of Points After Touchdowns made or extra points.
            fg_made (int): Yard distance of field goal made. Determines how many points.

        Returns:

            The function special_teams_scoring() returns the variable special_teams_score, which
            is the total points from both pat_made and fg_made.
        '''
        special_teams_score = 0
        #PAT Made
        if pat_made >= 1:
            special_teams_score += pat_made
        else:
            special_teams_score += 0

        #FG Made
        if 10 <= fg_made <= 49:
            special_teams_score += 3
        elif fg_made >= 50:
            special_teams_score += 5
        else:
            special_teams_score += 0

        return special_teams_score
