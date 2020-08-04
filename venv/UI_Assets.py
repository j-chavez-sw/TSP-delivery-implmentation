# Julian A. Chavez
#I.D. #: 000966293

from os import system, name




#this class mostly contains string printouts for the UI in Main
#this class also gathers and returns user input
class UI_Assets:
    
    
    def title():
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("         WGUPS - Package Delivery Tracker")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")

    def welcome():

        print("")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print(" Welcome to WGUPS delivery tracker!")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")

        print("")

    def menu1():
        print("")
        print("   What would you like to do?")
        print("     1. Start Deliveries...")
        print("     2. Look Up Package...")
        print("     3. Exit...")
        print("")
        print("   Please enter number selection...")
        selection = input(">>: ")
        return selection

    def lookup():
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("         Package Lookup")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("")
        print("   Please enter package id...")
        selection = input(">>: ")
        return int(selection)
    
    def lookupOptions():
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("         Package Lookup")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("")
        print("   What would you like to do?")
        print("     1. Look up by id...")
        print("     2. Look up by id and time...")
        print("     3. Look up all packages...")
        print("     4. Go back...")
        selection = input(">>: ")
        return selection
    
    def lookup_ID_Time():
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("         Package Lookup by id and time")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("")
        print("   Please enter package id...")
        id = input(">>: ")
        print("   Please enter time in format HH:MM...")
        time = input(">>: ")
        return int(id), time
    
    def invalid():
        print("   Invalid selection... Please try again.")

    def clear():

        if(name == 'nt'):
           x = system('cls')
        else:
           x = system('clear')
    
    def exit():
        print("")
        print("Thank you for using WGUPS delivery tracker!")
        print("Goodbye!")
        print("")
        
    def checkpoint_1():
        
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("  Checkpoint 1 - 8:00AM")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")

    def checkpoint_2():

        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("  Checkpoint 2 - 9:00AM")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")


    def checkpoint_3():

        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("  Checkpoint 3 - 9:05AM")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")


    def checkpoint_4():

        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("  Checkpoint 4 - 10:00AM")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")


    def checkpoint_5():

        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("  Checkpoint 5 - 10:20AM")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("")
        print("***WGUPS has updated the delivery address for package #9")
        print("****route will be updated...")
        print("")





    def checkpoint_6():

        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("  Checkpoint 6 - 10:30AM")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")


    def checkpoint_7():

        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("  Checkpoint 7 - 11:00AM")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")


    def checkpoint_8():

        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("  Checkpoint 8 - 12:00PM")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        
    def checkpoint_9():

        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("  Checkpoint 9 - 1:00PM")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")


    def menu2():
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("")
        print("   What would you like to do?")
        print("     1. Continue to next checkpoint...")
        print("     2. Look Up Package...")
        print("     3. Exit...")
        print("")
        print("   Please enter number selection...")
        selection = input(">>: ")
        return selection

    def menu3():
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("")
        print("   What would you like to do?")
        print("     1. Look Up Package...")
        print("     2. Exit...")
        print("")
        print("   Please enter number selection...")
        selection = input(">>: ")
        return selection