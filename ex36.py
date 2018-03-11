from sys import exit

def die(message):
    print(message, "Game Over!")
    exit(0)

def start_game():
    dragon_health = 100
    human_health = 100
    print("You come across a mean dragon to fight.")
    while True:
        if human_health < 1:
            die("The dragon has killed you.")
        elif dragon_health < 1:
            print("You killed the dragon!")
            exit(0)
        print(f"The dragon has {dragon_health} remaining.")
        print(f"And you have {human_health} remaining.")
        show_choices()
        choice = input("> ")
        if choice == "1":
            dragon_health = dragon_health - 3
            human_health = human_health - 5
            print("You punch the dragon, and it claws you.")
        elif choice == "2":
            dragon_health = dragon_health - 5
            human_health = human_health - 20
            print("The dragon, angered by your kick, breathes fire at you.")
        elif choice == "3":
            dragon_health = dragon_health - 50
            print("You stab the dragon real hard.")
        else:
            print("Try a real command.")

def show_choices():
    print("1. Punch the dragon.")
    print("2. Kick the dragon.")
    print("3. Attack the dragon with a pointy knife.")



start_game()
