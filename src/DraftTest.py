from Draft import Draft
import io
import random

def test_user_team_and_bot(monkeypatch, capsys):


    monkeypatch.setattr('sys.stdin',
                        io.StringIO("Y\nTom Brady\nTy Johnson\nJuJu Smith-Schuster\nGreg Olsen\nJoey Slye\nMario Addison\nTre Boston\nN"))

    def seed_bots():
        random.seed(4)

    d = Draft()
    seed_bots() #seed so that bot teams are the same
    d.draft_start()




    captured = capsys.readouterr().out
    output = '''Welcome to the Draft!
Would you like to start the Draft? Y/N: \nQB
Jameis Winston
Lamar Jackson
Kyler Murray
Andy Dalton
Jimmy Garoppolo
Matthew Stafford
Philip Rivers
Aaron Rodgers
Kirk Cousins
Deshaun Watson
Gardner Minshew
Ryan Fitzpatrick
Josh Rosen
Tom Brady
Josh Allen
Mason Rudolph
Ben Roethlisberger
Russell Wilson
Marcus Mariota
Jacoby Brissett
Case Keenum
Dak Prescott
Derek Carr
Patrick Mahomes
Mitchell Trubisky
Jared Goff
Teddy Bridgewater
Drew Brees
Taysom Hill
Matt Ryan
Carson Wentz
Baker Mayfield

Enter the QB's name you would like to draft from above list (Case Sensitive): \nTom Brady was added to your team!

RB
Christian McCaffrey
Peyton Barber
Ronald Jones
Dare Ogunbowale
Mark Ingram
Gus Edwards
Justice Hill
David Johnson
Chase Edmonds
Joe Mixon
Giovani Bernard
Matt Breida
Raheem Mostert
Jeff Wilson
Kerryon Johnson
Ty Johnson
J.D. McKissic
Austin Ekeler
Justin Jackson
Aaron Jones
Jamaal Williams
Dalvin Cook
Alexander Mattison
Ameer Abdullah
Duke Johnson
Leonard Fournette
Tyler Ervin
Kenyan Drake
Kalen Ballage
Sony Michel
Rex Burkhead
James White
Saquon Barkley
Devin Singletary
Patrick DiMarco
James Conner
Benny Snell
Jaylen Samuels
Rashaad Penny
Chris Carson
Derrick Henry
Dion Lewis
Jordan Wilkins
Marlon Mack
Nyheim Hines
Adrian Peterson
Ezekiel Elliott
Tony Pollard
Josh Jacobs
DeAndre Washington
Jalen Richard
Damien Williams
Darwin Thompson
Royce Freeman
Phillip Lindsay
David Montgomery
Tarik Cohen
Mike Davis
Todd Gurley
Malcolm Brown
Alvin Kamara
Latavius Murray
Ito Smith
Miles Sanders
Jordan Howard
Le'Veon Bell
Trenton Cannon
Nick Chubb
D'Ernest Johnson

Enter the RB's name you would like to draft from above list (Case Sensitive): \nTy Johnson was added to your team!

WR
Curtis Samuel
D.J. Moore
Ray-Ray McCloud
Chris Godwin
Mike Evans
Marquise Brown
Miles Boykin
Willie Snead
Christian Kirk
Damiere Byrd
Larry Fitzgerald
KeeSean Johnson
Tyler Boyd
John Ross
Alex Erickson
Auden Tate
Damion Willis
Dante Pettis
Deebo Samuel
Marquise Goodwin
Richie James
Kendrick Bourne
Kenny Golladay
Marvin Jones
Danny Amendola
Keenan Allen
Mike Williams
Davante Adams
Geronimo Allison
Marquez Valdes-Scantling
Jake Kumerow
Adam Thielen
Chad Beebe
Stefon Diggs
DeAndre Hopkins
Will Fuller
Kenny Stills
Keke Coutee
DeAndre Carter
D.J. Chark
Chris Conley
Dede Westbrook
Jakeem Grant
Preston Williams
Allen Hurns
Julian Edelman
Phillip Dorsett
Gunner Olszewski
Cody Latimer
Cody Core
Isaiah McKenzie
John Brown
Cole Beasley
Zay Jones
JuJu Smith-Schuster
James Washington
Diontae Johnson
Ryan Switzer
Tyler Lockett
DK Metcalf
Adam Humphries
Corey Davis
A.J. Brown
Tajae Sharpe
Darius Jennings
T.Y. Hilton
Parris Campbell
Steven Sims
Terry McLaurin
Trey Quinn
Randall Cobb
Michael Gallup
Devin Smith
Ced Wilson
Tyrell Williams
Hunter Renfrow
Demarcus Robinson
Sammy Watkins
Mecole Hardman
De'Anthony Thomas
Emmanuel Sanders
Courtland Sutton
DaeSean Hamilton
Diontae Spencer
Cordarrelle Patterson
Allen Robinson
Anthony Miller
Robert Woods
Cooper Kupp
Brandin Cooks
JoJo Natson
Michael Thomas
Tre'Quan Smith
Deonte Harris
Calvin Ridley
Julio Jones
Mohamed Sanu
Nelson Agholor
Mack Hollins
J.J. Arcega-Whiteside
Robby Anderson
Jamison Crowder
Josh Bellamy
Braxton Berrios
Odell Beckham
Jarvis Landry
Damion Ratley
Taywan Taylor

Enter the WR's name you would like to draft from above list (Case Sensitive): \nJuJu Smith-Schuster was added to your team!

TE
Greg Olsen
Cameron Brate
Mark Andrews
Nick Boyle
Hayden Hurst
Maxx Williams
Tyler Eifert
Drew Sample
George Kittle
Jesse James
T.J. Hockenson
Logan Thomas
Virgil Green
Kyle Rudolph
Irv Smith
Jordan Akins
James O'Shaughnessy
Durham Smythe
Mike Gesicki
Nick O'Leary
Matt LaCosse
Evan Engram
Dawson Knox
Lee Smith
Vance McDonald
Will Dissly
Nick Vannett
Eric Ebron
Jack Doyle
Jeremy Sprinkle
Jason Witten
Darren Waller
Derek Carrier
Travis Kelce
Noah Fant
Jeff Heuerman
Troy Fumagalli
Adam Shaheen
Ben Braunecker
Trey Burton
Gerald Everett
Tyler Higbee
Jared Cook
Austin Hooper
Zach Ertz
Demetrius Harris

Enter the TE's name you would like to draft from above list (Case Sensitive): \nGreg Olsen was added to your team!

K
Joey Slye
Matt Gay
Justin Tucker
Zane Gonzalez
Randy Bullock
Robbie Gould
Matt Prater
Ty Long
Mason Crosby
Dan Bailey
Ka'imi Fairbairn
Josh Lambo
Aldrick Rosas
Stephen Hauschka
Chris Boswell
Jason Myers
Dustin Hopkins
Brett Maher
Daniel Carlson
Harrison Butker
Brandon McManus
Eddy Pineiro
Greg Zuerlein
Wil Lutz
Jake Elliott
Sam Ficken
Austin Seibert

Enter the K's name you would like to draft from above list (Case Sensitive): \nJoey Slye was added to your team!

LB
Mario Addison
Jermaine Carter
Kevin Minter
Shaquil Barrett
Devin White
Devante Bond
Anthony Nelson
Jack Cichy
Tim Williams
Tyus Bowser
Chris Board
Joe Walker
Dre Greenlaw
Azeez Al-Shaair
Jahlani Tavai
Uchenna Nwosu
Kyler Fackrell
Quincy Williams
Josh Allen
Sam Eguavoen
Avery Moss
Vince Biegel
Ja'Whaun Bentley
Lorenzo Carter
Devin Bush
Ola Adeniyi
Harold Landry
Cole Holcomb
Shaun Dion Hamilton
Montez Sweat
Ryan Anderson
Nicholas Morrow
Ben Niemann
Tanoh Kpassagnon
Isaiah Irving
Deion Jones
Foye Oluokun
Nate Gerry
Neville Hewitt
Blake Cashman
Harvey Langi
Mack Wilson

Enter the LB's name you would like to draft from above list (Case Sensitive): \nMario Addison was added to your team!

DB
Tre Boston
Chris Jones
Brandon Wilson
K'Waun Williams
Tarvarius Moore
Tracy Walker
Desmond King
Brandon Facyson
Adrian Phillips
Rayshawn Jenkins
Jaylen Watkins
Darnell Savage
Raven Greene
Anthony Harris
Ronnie Harrison
Jarrod Wilson
D.J. Hayden
Chris Lammons
Steven Parker
Ken Webster
Jonathan Jones
J.C. Jackson
Terrence Brooks
Corey Ballentine
Michael Thomas
Grant Haley
Levi Wallace
Siran Neal
Lano Hill
Simeon Thomas
Keisean Nixon
Bashaud Breeland
Juan Thornhill
Nickell Robey-Coleman
Sharrod Neasman
Kendall Sheffield
Blidi Wreh-Wilson
T.J. Carrie

Enter the DB's name you would like to draft from above list (Case Sensitive): \nTre Boston was added to your team!
Your team consists of: {'QB': 'Tom Brady', 'RB': 'Ty Johnson', 'WR': 'JuJu Smith-Schuster', 'TE': 'Greg Olsen', 'K': 'Joey Slye', 'LB': 'Mario Addison', 'DB': 'Tre Boston'}

Bot 1 team consists of: {'QB': 'Mason Rudolph', 'RB': 'Rashaad Penny', 'WR': 'John Ross', 'TE': 'Will Dissly', 'K': 'Jason Myers', 'LB': 'Tyus Bowser', 'DB': 'Tracy Walker'}

Bot 2 team consists of: {'QB': 'Jimmy Garoppolo', 'RB': 'Ronald Jones', 'WR': 'John Brown', 'TE': 'Jeff Heuerman', 'K': 'Dan Bailey', 'LB': 'Shaquil Barrett', 'DB': 'Ronnie Harrison'}

Bot 3 team consists of: {'QB': 'Patrick Mahomes', 'RB': 'James Conner', 'WR': 'J.J. Arcega-Whiteside', 'TE': 'Logan Thomas', 'K': 'Austin Seibert', 'LB': 'Anthony Nelson', 'DB': 'D.J. Hayden'}

'''
    assert output == captured

def test_draft_exit(monkeypatch, capsys):

    monkeypatch.setattr('sys.stdin', io.StringIO("N\n"))

    d = Draft()
    d.draft_start()

    captured = capsys.readouterr().out
    assert "Welcome to the Draft!\n"
    "Would you like to start the Draft? Y/N: \n" == captured
