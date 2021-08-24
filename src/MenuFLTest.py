from MenuFL import Menu
import io



def test_menu_manual(monkeypatch, capsys):
    '''Test to print out menu manual'''
    monkeypatch.setattr('sys.stdin', io.StringIO("2\n"))

    MenuRun = Menu()
    MenuRun.menu()


    captured = capsys.readouterr().out
    #print(captured)
    assert "Welcome to the Fantasy League\n"
    "1. Start Draft Simulation\n"
    "2. Description of Program\n"
    "3. Exit Program\n"
    "Enter which number choice you would like: \n"
    "This is a program that simulates a virtual fantasy football game!\n"
    "\n"
    "The program gets its stats using an API called NFLGame.\n"
    "The API receives its stats from NFL.com Game Center.\n"
    "\n"
    "Go up against 3 randomly generated bot teams!\n"
    "\n"
    "In later iterations of this program, integration of more teams including more user teams.\n"
    "\n"
    "Press ENTER to go back to the Main Menu." == captured

def test_start_draft(monkeypatch, capsys):
    '''Test to go to draft'''

    monkeypatch.setattr('sys.stdin', io.StringIO("1\nN\n"))

    MenuRun = Menu()
    MenuRun.menu()

    captured = capsys.readouterr().out
    assert "Welcome to the Fantasy League\n"
    "1. Start Draft Simulation\n"
    "2. Description of Program\n"
    "3. Exit Program\n"
    "Enter which number choice you would like: \n"
    "Welcome to the Draft!\n"
    "Would you like to start the Draft? Y/N: Please restart the program!" == captured

def test_exit(monkeypatch, capsys):
    '''Test to see if program exits'''

    monkeypatch.setattr('sys.stdin', io.StringIO("3\n"))

    MenuRun = Menu()
    MenuRun.menu()

    captured = capsys.readouterr().out
    assert "Welcome to the Fantasy League\n"
    "1. Start Draft Simulation\n"
    "2. Description of Program\n"
    "3. Exit Program\n"
    "Enter which number choice you would like: \n" == captured
