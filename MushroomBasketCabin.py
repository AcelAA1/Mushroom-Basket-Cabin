menu_prompts = ["Do you want to try to open the door or text the host for information?"]
optionslist = [["Open door","Text host"]]
menucount = 0
def main():
    print("You have booked a lovely cabin in the woods.\nUpon arrival you see the door and remember you haven't yet received a key\nYou place down your lovely Mushroom basket and inspect the door for clues.\nUpon closer inspection you realise there is no keyhole.")
    menu(menu_prompts[0], menucount)
    pass

def menu(prompt,menucount):
    print(prompt)
    i = 1
    n = 0
    for option in optionslist[menucount]:
        print(f"{i}.{optionslist[menucount][n]}")
        i+=1
        n+=1
    choice = input()
    print(choice)

class Room:
    done = False

main()