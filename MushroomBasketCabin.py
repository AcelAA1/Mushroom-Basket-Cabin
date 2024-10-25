from text import *
menu_prompts = ["Do you want to try to open the door or text the host for information?\n","Now how will you get out?\n","What do you do?\n"]
options_list = [["Open door","Text host"],
                ["Text host for help","Start looking around","Call 112"],
                ["Approach desk (inspect computer and surroundings)","Approach kitchen","Approach bedroom"],
                ["Do puzzel","Use computer","Leave desk"],
                ["Try to login","Check inventory for solutions","Leave computer"],
                ["Try to solve the puzzle and save the solution to your inventory","Give up for now and come back later"],
                ["Approach bed","Inspect floor plan","Go back to the living room"],
                ["Inspect the note on the counter","Go to the sink","Go and open the Fridge","Go back to the living room"]]
lore_list = [introduction_text,enter_cabin_text,host_responce_1,host_responce_2,
             living_room_description, desk_descprition, locked_room,puzzle_1_text,
             try_computer_to_early, win_text, call_112, key_on_desk, unlock_bedroom,
             bedroom_description, puzzle_2_text, floor_plan_text,kitchen_descprition,puzzle_3_text,sink_lore,fridge_lore,unlock_kitchen]
uncoperative = 0
inventory = []
been_to_bedroom = False
been_to_kitchen = False
answers = {"desk_puzzle":"mushroombasket","bedroom_puzzle":"342","kitchen_puzzle":"42"}
def main():
    print(lore_list[0])
    enter_cabin_scenario()   
    start_plaiyng_scenario()   
    
def menu(prompt,menucount):
    print(prompt)
    i = 1
    options_values_list =[]
    for option in options_list[menucount]:
        print(f"{i}. {option}")
        options_values_list.append(i)
        i+=1
    choice = input()
    if choice.isnumeric():
        if int(choice) in options_values_list:
            return int(choice)
        else:
            print("\nInvalid option. Try again\n")
            return menu(prompt,menucount)
    else:
        print("\nPlease only enter numeric values. Try Again\n")
        return menu(prompt,menucount)        
    
def enter_cabin_scenario():
    choice_1 = menu(menu_prompts[0], 0)
    global uncoperative
    if choice_1 == 1:
        print(lore_list[1])        
    elif choice_1 == 2:
        print(lore_list[2])
        uncoperative += 1
        if uncoperative >= 10:
            print("Just move on!\n")
        enter_cabin_scenario()


def start_plaiyng_scenario():
        choice_2 = menu(menu_prompts[1], 1)
        if choice_2 == 1:
            print(lore_list[3])
            start_plaiyng_scenario()
        elif choice_2 == 2:
            print(lore_list[4])
            living_room_scenario()
            # giving the user the illusion of choice as still first version will be adjusted later
        elif choice_2 == 3:
            print(lore_list[10])
            start_plaiyng_scenario()


def living_room_scenario():
    global been_to_bedroom
    global been_to_kitchen
    choice_3 = menu(menu_prompts[2], 2)
    if choice_3 == 1:
        if "key" in inventory:
            print(lore_list[5])
        else:
            print(lore_list[5],lore_list[11])
            inventory.append("key")
            print(f"Your inventory:{inventory}")
        desk_scenario()
    elif choice_3 == 2:
        if "key" in inventory and been_to_kitchen:
            kitchen_scenario()
        elif "key" in inventory and not been_to_kitchen:
            print(lore_list[20])
            been_to_kitchen = True
            kitchen_scenario()
        else:
            print(lore_list[6])
            living_room_scenario()
    elif choice_3 == 3:
        if "key" in inventory and been_to_bedroom:
            bedroom_scenario()
        elif "key" in inventory and not been_to_bedroom:
            print(lore_list[12])
            been_to_bedroom = True
            bedroom_scenario()
        else:    
            print(lore_list[6])
            living_room_scenario()
        # same lore for 2 and 3 as this is version 1 and functionality is still fairly basic
        # will be adjusted in future iteretions depending on available time


def desk_scenario():
    choice_4 = menu(menu_prompts[2], 3)

    if choice_4 == 1:
        print(lore_list[7])
        solve_puzzle("desk_puzzle")
        desk_scenario()
    elif choice_4 == 2:
        print(lore_list[8])
        computer_login()
    elif choice_4 == 3:
        living_room_scenario()
  

def bedroom_scenario():
    print(lore_list[13])
    choice_5 = menu(menu_prompts[2],6)
    if choice_5 == 1:
        print(lore_list[14])
        solve_puzzle("bedroom_puzzle")
        bedroom_scenario()
    elif choice_5 == 2:
        print(lore_list[15])
        bedroom_scenario()
    elif choice_5 == 3:
        living_room_scenario()

def kitchen_scenario():
    print(lore_list[16])
    choice_6 = menu(menu_prompts[2], 7)
    if choice_6 == 1:
        print(lore_list[17])
        solve_puzzle("kitchen_puzzle")
        kitchen_scenario()
    elif choice_6 == 2:
        print(lore_list[18])
        kitchen_scenario()
    elif choice_6 == 3:
        print(lore_list[19])
        kitchen_scenario()
    elif choice_6 == 4:
        living_room_scenario()

def solve_puzzle(puzzle_location):
    trying_puzzle = True
    while trying_puzzle:
        choice_puzzle_1 = menu("You look at the puzzle\n", 5)
        if choice_puzzle_1 == 1:
            choice_solve_puzzle = input("Puzzle answer: ")
            if choice_solve_puzzle == answers[puzzle_location]:
                trying_puzzle = False
                print("""
You answered correctly!
The answer has been added to your inventory
""")
                inventory.append({puzzle_location:answers[puzzle_location]})
                break
        if choice_puzzle_1 == 2:
            break
    
def computer_login():
    win = False
    trying_puzzle = True
    while trying_puzzle:
        puzzle_choice = menu("What do you do on the computer",4)
        if puzzle_choice == 1:
                choice_computer_login = input("Password: ")
                if choice_computer_login == "342mushroombasket":
                    win = True
                    trying_puzzle = False
                else:
                    print("\nIncorrect. Try again.\n")
        elif puzzle_choice == 2:
            print(inventory)
        elif puzzle_choice == 3:
            desk_scenario()
        
    if win:
        print(lore_list[9])
        
main() 


