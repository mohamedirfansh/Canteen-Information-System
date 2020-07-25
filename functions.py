from data import *
from datetime import datetime


def getAllStallNames():
    stallNames = list()
    for key in outlet.keys():
        if (isinstance(key, str)):
            stallNames.append(key)
    return stallNames


def updateTime():
    date = datetime.now()
    time = (datetime.now().hour * 100) + datetime.now().minute
    day = datetime.now().weekday()
    return date, time, day


def get_allMenu(stall, day):
    wholeMenu = ''

    # -----------If stall is fast food (Got 2 menus, breakfast and lunch). Hence loop twice----------------------------------------------------------------
    if len(main_database[stall].keys()) == 2:
        noOfLoops = 2

    # -----------If stall has 1 menu for whole day, loop 1 time--------------------------------------------------------------------------
    else:
        noOfLoops = 1

    # -----------Store the menus of a stall in a tuple to be looped--------------------------------------------------------------------------
    nameOfMenu = tuple(main_database[stall].keys())

    # -----------Append the operating hours of the stall in a variable string--------------------------------------------------------------------------
    wholeMenu += main_database[stall][nameOfMenu[0]]['Hours']
    wholeMenu += '\n\n'

    # -----------Append the title and menu of the stall in a variable string--------------------------------------------------------------------------
    for looping in range(noOfLoops):
        wholeMenu += main_database[stall][nameOfMenu[looping]]['Title']
        wholeMenu += '\n'
        for menus in main_database[stall][nameOfMenu[looping]]['Menu'].values():
            for individualMenu in menus:
                wholeMenu = wholeMenu + individualMenu + '\n'
            wholeMenu += '\n'

    # -----------Append the address of the stall in a variable string--------------------------------------------------------------------------
    wholeMenu += main_database[stall][nameOfMenu[0]]['Location']
    wholeMenu += '\n'

    # -----------Return the variable string to be invocator--------------------------------------------------------------------------
    return wholeMenu


def choosing_database(database_choice, time, day):
    # -----------Check if it is a fast food stall and see if it has breakfast or lunch-----------
    if len(main_database[database_choice]) == 2:
        for BreakfastOrLunch in main_database[database_choice]:
            for days, timings in main_database[database_choice][BreakfastOrLunch]['Operating Hours'].items():
                if day in days and timings[0] <= time < timings[1]:
                    return main_database[database_choice][BreakfastOrLunch]

        # -----------If it does not have breakfast, send lunch data by default to minimize errors later-----------
        return main_database[database_choice]['Lunch']

    # -----------Else, just send the stall dictionary's data (For non-fast food stalls)-----------
    else:
        return main_database[database_choice][database_choice]


# -----------Get menu of a particular stall depending whether it is breakfast/lunch (for fast food stall) or which day's menu (for foodcourt stall)-----------------------------------
def get_menu_from_database(database, time, day):
    menu_string = ''
    isStallclose = True

    # -----------First check if the stall is closed or still open-----------
    for days, timings in database['Operating Hours'].items():
        if day in days and timings[0] <= time < timings[1]:

            # -----------Then store the menus depending which day it falls under-----------
            for allTheDays, allMenu in database['Menu'].items():
                if day in allTheDays:
                    for eachMenu in allMenu:
                        menu_string += eachMenu + '\n'
            isStallclose = False
            break

    # -----------Return stall is closed-----------
    if isStallclose:
        menu_string = "Sorry. Stall Closed"

    return menu_string

