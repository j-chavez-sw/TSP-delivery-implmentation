# Julian A. Chavez
#I.D. #: 000966293

from WGUPSHub import *
from UI_Assets import *
import sys
import re


class Main:

    hub = WGUPSHub()
    hub.start()
    UI_Assets.title()
    checkpoint = 1
    currentTime = 480

    #start check point
    #contains simple nested while loops to provide the UI and capture valid input
    while(True):
        UI_Assets.welcome()
        selection = UI_Assets.menu1()
        if(selection == "1"):
            break
        elif(selection == "2"):
            id = UI_Assets.lookup()
            hub.packageLookup(id,479)
        elif(selection == "3"):
            UI_Assets.exit()
            sys.exit()
        else:
            UI_Assets.clear()
            UI_Assets.invalid()
    
    while(True):

        if(checkpoint == 1):
            UI_Assets.checkpoint_1()
        if(checkpoint == 2):
            currentTime = 540
            UI_Assets.checkpoint_2()
        if(checkpoint == 3):
            currentTime = 545
            UI_Assets.checkpoint_3()
        if(checkpoint == 4):
            currentTime = 600
            UI_Assets.checkpoint_4()
        #This is the 10:20 address change per the project requirements
        if(checkpoint == 5):
            currentTime = 620
            hub.reoptimize_Wrong_Address(currentTime, 9, "410 S State St")
            UI_Assets.checkpoint_5()
        if(checkpoint == 6):
            currentTime = 630
            UI_Assets.checkpoint_6()
        if(checkpoint == 7):
            currentTime = 660
            UI_Assets.checkpoint_7()
        if(checkpoint == 8):
            currentTime = 720
            UI_Assets.checkpoint_8()
        if(checkpoint == 9):
            currentTime = 780
            UI_Assets.checkpoint_9()
        checkpoint+=1
        if(checkpoint == 10):
            while(True):
                hub.finalReport()
                selection = UI_Assets.menu3()
                if (selection == "1"):
                    while (True):

                        sub_selection = UI_Assets.lookupOptions()
                        if (sub_selection == "1"):
                            id = UI_Assets.lookup()
                            hub.packageLookup(id, currentTime)
                        elif (sub_selection == "2"):
                            while (True):

                                id, time = UI_Assets.lookup_ID_Time()
                                expression = re.compile('\d{2}:\d{2}')
                                if (int(id)):
                                    if (expression.match(time)):
                                        hour, minute = time.split(':')
                                        time = (int(hour) * 60) + int(minute)
                                        break
                                UI_Assets.invalid()

                            hub.packageLookup(id, time)
                        elif (sub_selection == "3"):
                            hub.printAllDeliveries(currentTime)
                        elif (sub_selection == "4"):
                            break
                        else:
                            UI_Assets.clear()
                            UI_Assets.invalid()
                elif (selection == "2"):
                    UI_Assets.exit()
                    sys.exit()
                else:
                    UI_Assets.clear()
                    UI_Assets.invalid()
        selection = UI_Assets.menu2()

        if(selection == "1"):
            print("Next checkpoint...")
        elif(selection == "2"):
            while (True):

                sub_selection = UI_Assets.lookupOptions()
                if (sub_selection == "1"):
                    id = UI_Assets.lookup()
                    hub.packageLookup(id, currentTime)
                elif (sub_selection == "2"):
                    while(True):

                        id, time = UI_Assets.lookup_ID_Time()
                        expression = re.compile('\d{2}:\d{2}')
                        if(int(id)):
                            if(expression.match(time)):
                                hour, minute = time.split(':')
                                time = (int(hour)*60) + int(minute)
                                break
                        UI_Assets.invalid()

                    hub.packageLookup(id, time)
                elif (sub_selection == "3"):
                    hub.printAllDeliveries(currentTime)
                elif (sub_selection == "4"):
                    break
                else:
                    UI_Assets.clear()
                    UI_Assets.invalid()
        elif(selection == "3"):
            UI_Assets.exit()
            sys.exit()
        else:
            UI_Assets.clear()
            UI_Assets.invalid()




