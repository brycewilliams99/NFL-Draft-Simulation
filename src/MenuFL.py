from Draft import Draft
from Stats import Stats
from os import system, name
'''
The Menu class will deal with the main menu and direct the user to the draft selection.
'''

class Menu:

    def menu(self):
        '''
        The Menu function is what the user will see when they first load up the
        fantasy league.
        '''
        MenuRun = Menu()
        DraftTest = Draft()
        StatsTest = Stats()
        choice = None
        #MenuRun.clear_screen()
        print("Welcome to the Fantasy League!")
        print("1. Start Draft Simulation")
        print("2. Description of Program")
        print("3. Exit Program")

        #While loop to take care of user selection.
        #Enter try exception
        #Or check to see if input is a number.
        choice = int(input("Enter which number choice you would like: "))

        while not (1 <= choice <= 3):
            try:
                val = int(choice)
            except ValueError:
                print("Error! A number was not entered! Try again! ")

            choice = int(input("That is not a choice! Enter which number choice you would like: "))

        if choice == 1:
            #MenuRun.clear_screen()
            DraftTest.draft_start()
        elif choice == 2:
            MenuRun.program_description()
        elif choice == 3:
            MenuRun.clear_screen()

        #week = int(input("Enter what week you would like to do! "))
        StatsTest.import_stats()

    def program_description(self):
        '''
        The program_description method explains to the user what the program is supposed to do.  It also
        talks about what goes into the program to make it work.
        '''
        #Clear screen and print out program description.
        MenuRun = Menu()
        #MenuRun.clear_screen()
        print("This is a program that simulates a virtual fantasy football game!")
        print("")
        print("The program gets its stats using an API called NFLGame.")
        print("The API receives its stats from NFL.com Game Center.")
        print("")
        print("Go up against 3 randomly generated bot teams!")
        print("")
        print("In later iterations of this program, integration of more teams including more user teams.")
        print("")
        print("Press ENTER to go back to the Main Menu.")
        input()
        MenuRun.menu()


    def clear_screen(self):
        '''
        clear_screen method is a method that is found at https://www.geeksforgeeks.org/clear-screen-python/
        which just clears the screen for the user.  Used so that the screen is not filled with text when calling
        another method.
        '''
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

if __name__ == "__main__":
    MenuRun = Menu()
    MenuRun.menu()
