menu_prompts = ["Do you want to try to open the door or text the host for information?\n","Now how will you get out?\n","What do you do?\n"]
options_list = [["Open door","Text host"],["text host for help","start looking around"],["approach desk (inspect computer and surroundings)","approach kitchen","approach bedroom"],["do puzzel","use computer"]]
introduction_text =  """
You have booked a lovely cabin in the woods.
Upon arrival you see the door and remember you haven't yet received a key
You place down your lovely Mushroom basket and inspect the door for clues.
Upon closer inspection you realise there is no keyhole.
 """
enter_cabin_text = """
You open the door.
And as you enter the cabin you suddenly realise,
you forgot to pick up your lovely Mushroom basket. 
And just as you turn around to get it the door slams shut!
Oh no! You're trapped as, you try to open the door again you realise it has been locked.               
"""
host_responce_1 = """
Host says 'the door is open there is a code inside'
Upon reciving this information you decide to open the door
"""
host_responce_2 = """
Host says 'code in house, look around'

"""
living_room_description = """
Looking around you realise you are in the living room of the house and in it you see a desk with a computer on it
and what seems to be the way to the kitchen as well as a master bedroom door.
"""
desk_descprition = """
On the desk you find a note which seems to have a puzzle on it 
and on the computer you see a post it note that says 'enter password to get door code' 
"""
locked_room = """
The door is looked, 
So you decide to look at the desk in the living room instead
"""

puzzle_1_text = """
You look at the puzzle and see that it's a note that says, 1+1=?

Now that you have seen the puzzle you decide to enter the solution to the computer.
To try and login and get the code for the door.
"""

try_computer_to_early = """
As you look at the computer you relize you won't know the answer before doing the puzzle.
So you decide to do the puzzle instead.
"""
win_text = """
You enter the correct password and the code shows up on the screen.
You make a leep of joy as you sprint to the door and enter the code at the terminal you definetly noticed eariler.
Your joy can no longer be expressed in words as you pick up your beloved Mushroom Basket as you are finally reunited.

The End.


Thanks for playing!
"""
lore_list = [introduction_text,enter_cabin_text,host_responce_1,host_responce_2,living_room_description, desk_descprition, locked_room,puzzle_1_text,try_computer_to_early, win_text]

def main():

    print(lore_list[0])
    choice_1 = menu(menu_prompts[0], 0)
    if choice_1 == 1:
        print(lore_list[1])
    elif choice_1 == 2:
        print(lore_list[2])
        print(lore_list[1])

    
    choice_2 = menu(menu_prompts[1], 1)
    if choice_2 == 1:
        print(lore_list[3])
        print(lore_list[4])
    elif choice_2 == 2:
        print(lore_list[4])
        # giving the user the illusion of choice as still first version will be adjusted later 

    choice_3 = menu(menu_prompts[2], 2)
    if choice_3 == 1:
        print(lore_list[5])
    elif choice_3 == 2:
        print(lore_list[6])
        print(lore_list[5])
    elif choice_3 == 3:
        print(lore_list[6])
        print(lore_list[5])
        # same lore for 2 and 3 as this is version 1 and functionality is still fairly basic
        # will be adjusted in future iteretions depending on available time

    choice_4 = menu(menu_prompts[2], 3)
    if choice_4 == 1:
        print(lore_list[7])
    elif choice_4 == 2:
        print(lore_list[8])
        print(lore_list[7])
    done = False
    while not done:
        choise_solve_puzzle = input("Password: ")
        if choise_solve_puzzle == "2":
            done = True
        
    print(lore_list[9])
        

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




class Room:
    done = False

main() 

