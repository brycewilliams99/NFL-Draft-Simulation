from ScoringSystem import *

#defensive score
defensive_score = 0
sacks_points = 0
intercepts = 0
intercepts_points = 0
fumbles_receiving = 0
fumbles_receiving_points = 0
safeties = 0
safeties_points = 0
def_tds = 0
def_tds_points = 0
kick_punt_tds = 0
kick_punt_tds_points = 0
def_two_point_conv = 0
def_two_point_conv_points = 0
points_allow = 0
sacks = 0

#offensive score
offensive_score = 0
passing_yds = 0
passing_tds = 0
passing_ints = 0
rushing_yds = 0
rushing_tds = 0
receiving_yrds = 0
receiving_tds = 0
two_point_conv = 0
fumbles = 0

#individual defensive score
solo_tackles = 0
assist_tackles = 0
sacks = 0
sack_yrds = 0
tackle_for_loss = 0
qb_hits = 0
pass_def = 0
individual_intercepts = 0
fumbles_forced = 0

#special teams score
special_teams_score = 0
pat_made = 0
fg_made = 0


#Defensive Testing
def test_defensive_scoring0():
    assert ScoringSystem.defensive_scoring(0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) == 0

def test_defensive_scoring1():
    assert ScoringSystem.defensive_scoring(2, 21, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) == 4

def test_defensive_scoring2():
    assert ScoringSystem.defensive_scoring(2, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0) == 32

def test_defensive_scoring3():
    assert ScoringSystem.defensive_scoring(0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) == 7

def test_defensive_scoring4():
    assert ScoringSystem.offensive_scoring(25, 1, 1, 10, 1, 10, 1, 1, 1) == 17

    #Check for Points Allowed
def test_defensive_scoring5():
    assert ScoringSystem.defensive_scoring(0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) == 4

def test_defensive_scoring6():
    assert ScoringSystem.defensive_scoring(0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) == 1

def test_defensive_scoring7():
    assert ScoringSystem.defensive_scoring(0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) == -1

def test_defensive_scoring8():
    assert ScoringSystem.defensive_scoring(0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) == -4

#Offensive Testing
def test_offensive_scoring0():
    assert ScoringSystem.offensive_scoring(0, 0, 0, 0, 0, 0, 0, 0, 0) == 0

def test_offensive_scoring1():
    assert ScoringSystem.offensive_scoring(25, 1, 0, 10, 1, 10, 1, 1, 0) == 21

def test_offensive_scoring2():
    assert ScoringSystem.offensive_scoring(25, 1, 0, 10, 1, 10, 1, 1, 1) == 19

#Special Teams Testing
def test_special_teams_scoring1():
    assert ScoringSystem.special_teams_scoring(1, 50) == 6

def test_special_teams_scoring2():
    assert ScoringSystem.special_teams_scoring(0, 20) == 3

def test_special_team_scoring0():
    assert ScoringSystem.special_teams_scoring(0, 0) == 0

#Individual Defensive Testing
def test_individual_defensive_scoring0():
    assert ScoringSystem.individual_defensive_scoring(0, 0, 0, 0, 0, 0, 0, 0, 0) == 0

def test_individual_defensive_scoring1():
    assert ScoringSystem.individual_defensive_scoring(1, 2, 1, 10, 1, 1, 1, 1, 1) == 13




ScoringSystem.defensive_scoring(sacks, points_allow, defensive_score, sacks_points, intercepts, intercepts_points,
fumbles_receiving, fumbles_receiving_points, safeties, safeties_points, def_tds, def_tds_points,
kick_punt_tds, kick_punt_tds_points, def_two_point_conv, def_two_point_conv_points)

ScoringSystem.offensive_scoring(passing_yds, passing_tds, passing_ints, rushing_yds, rushing_tds,
receiving_yrds, receiving_tds, two_point_conv, fumbles)

ScoringSystem.special_teams_scoring(pat_made, fg_made)

ScoringSystem.individual_defensive_scoring(solo_tackles, assist_tackles, sacks, sack_yrds,
tackle_for_loss, qb_hits, pass_def, individual_intercepts, fumbles_forced)
