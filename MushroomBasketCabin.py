from text import *
menu_prompts = ["Do you want to try to open the door or text the host for information?\n","Now how will you get out?\n","What do you do?\n"]
options_list = [["Open door","Text host"],["Text host for help","Start looking around","Call 112"],["Approach desk (inspect computer and surroundings)","Approach kitchen","Approach bedroom"],["Do puzzel","Use computer"],["Try to login","Check inventory for solutions","Leave computer"]]
lore_list = [introduction_text,enter_cabin_text,host_responce_1,host_responce_2,living_room_description, desk_descprition, locked_room,puzzle_1_text,try_computer_to_early, win_text, call_112, key_on_desk]
uncoperative = 0
inventory = []
answer = {}
def main():
    print(lore_list[0])
    scenario_1()   
    scenario_2()
    
    scenario_4()
    solve_puzzle()    
    
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
    
def scenario_1():
    choice_1 = menu(menu_prompts[0], 0)
    global uncoperative
    if choice_1 == 1:
        print(lore_list[1])        
    elif choice_1 == 2:
        print(lore_list[2])
        uncoperative += 1
        if uncoperative >= 10:
            print("Just move on!\n")
        scenario_1()
#enter house scenario

def scenario_2():
        choice_2 = menu(menu_prompts[1], 1)
        if choice_2 == 1:
            print(lore_list[3])
            scenario_2()
        elif choice_2 == 2:
            print(lore_list[4])
            scenario_3()
            # giving the user the illusion of choice as still first version will be adjusted later
        elif choice_2 == 3:
            print(lore_list[10])
            scenario_2()
#start playing game scenario

def scenario_3():
    choice_3 = menu(menu_prompts[2], 2)
    if choice_3 == 1:
        if "key" in inventory:
            print(lore_list[5])
        else:
            print(lore_list[5],lore_list[11])
            inventory.append("key")
    elif choice_3 == 2:
        print(lore_list[6])
        scenario_3()
    elif choice_3 == 3:
        print(lore_list[6])
      
        scenario_3()
        # same lore for 2 and 3 as this is version 1 and functionality is still fairly basic
        # will be adjusted in future iteretions depending on available time
#living room /main scenario

def scenario_4():
    choice_4 = menu(menu_prompts[2], 3)

    if choice_4 == 1:
        print(lore_list[7])
    elif choice_4 == 2:
        print(lore_list[8])
        scenario_4()
    #desk scenario

def scenario_5():
    pass   
    
def solve_puzzle():
    win = False
    
        if puzzle_choice == 1:
                choise_solve_puzzle = input("Password: ")
                if choise_solve_puzzle == "mushroombasket":
                    win = True
                    trying_puzzle = False
                else:
                    print("\nIncorrect. Try again.\n")
        elif puzzle_choice == 2:
            print(inventory)
        elif puzzle_choice == 3:
            scenario_3()
        
    if win:
        print(lore_list[9])
        
main() 


