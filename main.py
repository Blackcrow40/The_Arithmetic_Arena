import random
import operator
import time

maths = [operator.add, operator.sub, operator.mul]



attacks = [
    "swings at", "bashes at", "stabs at", "lunges at", "leaps at", "slashes at", "pokes at", "prods at", "runs at", "charges at",
    "sashays at", "dances at", "swims at",
    "throws a pie at",      
    "tosses a shoe at",     
    "karate kicks",         
    "flails wildly at",     
    "hurls a fireball at",  
    "spins and strikes",    
    "body slams",          
    "screeches and lunges at",  
    "bonks",               
    "tickles",              
    "sprays water at",      
    "smacks",               
    "tackles",              
    "pelts you with muffins",  
    "whacks",               
    "flicks a pebble at",   
    "trips",                
    "dropkicks",            
    "sneezes on",           
    "yeets a chair at",
    "slashes fiercely at",
    "strikes with precision at",
    "pummels",
    "lunges with a blade at",
    "delivers a crushing blow to",
    "aims a deadly strike at",
    "thrusts a spear at",
    "unleashes a flurry of blows at",
    "fires an arrow at",
    "brings down a hammer on",  
]

player_attack = [
    "slash",
    "strike",
    "stab",
    "pummel",
    "smash",
    "cleave",
    "bash",
    "lunge at",
    "shoot",
    "impale",
    "tickle",
    "boop",
    "bonk",
    "throw a sock at",
    "flick",
    "yeet a rubber chicken at",
    "spray silly string at",
    "sneeze on",
    "hug",
    "poke",
]

first_name = [
    "Captain", "Soul", "Doctor", "James", "Jane",
    "Bubbles", "Zigzag", "Shadow", "Muffin", "Turbo",
    "Luna", "Snickerdoodle", "Ace", "Whiskers", "Pixel",
    "Boomer", "Giggles", "Fizzy", "Waffles", "Nova",
    "Emily", "Daniel", "Sophia", "Liam", "Olivia",
    "Ethan", "Isabella", "Michael", "Ava", "Benjamin",
    "Charlotte", "Alexander", "Amelia", "Noah", "Mia",
    "Lucas", "Grace", "Henry", "Chloe", "Jack"
]

last_name = [
    "Crunch", "McFluff", "Banana", "Wiggleton", "Snort",
    "Bubblebeard", "Pickle", "Gigglepants", "Zoodle", "Wobble",
    "Snicklepuff", "Fizzlebang", "McSprinkles", "Jellybean", "Tater",
    "Bananahammock", "Fluffernoodle", "Bop", "Twinklesocks", "Wigglesworth",
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "White"
]


rank = ["The Pirate", "The Captain", "The Gladiator", "The Slave", "The Virgin", "The Lost", "The Dumb", "The Smart", "The Silly", "The Sleepy", "The Sly", "The Sneaky", "The Chad", "The Lost", "The Mad", "The Time Traveller", "The Thief", "The Perfectly Sane", "The Hero", "The Brain" , "The Bastard", "The Dog", "The Provocator", "The Secutor", "The Retiarius", "The Hoplomachus", "The Murmillo", "The Ranger", "The Barbarian", "The Bard", "The Cleric", "The Druid", "The Fighter", "The Monk", "The Paladin", "The Rogue", "The Tavern Keeper", "The Barkeeper", "The Maid", "The Zombie", "The Wizard", "The Wild Child", "The Doctor", "The Conman", "The Beloved", "The Bad Guy"]


ascii_welcome = """\
 __    __     _                          
/ / /\ \ \___| | ___ ___  _ __ ___   ___ 
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \\
 \  /\  /  __/ | (_| (_) | | | | | |  __/
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|"""

ascii_to_the = """\
 _____        _____ _          
/__   \___   /__   \ |__   ___ 
  / /\/ _ \    / /\/ '_ \ / _ \\
 / / | (_) |  / /  | | | |  __/
/\/   \___/   \/   |_| |_|\___|"""

ascii_arena = """\
   _                        
  /_\  _ __ ___ _ __   __ _ 
 //_\\| '__/ _ \ '_ \ / _` |
/  _  \ | |  __/ | | | (_| |
\_/ \_/_|  \___|_| |_|\__,_|"""

ascii_game_over = """
           ___                         ___                         
          / _ \__ _ _ __ ___   ___    /___\__   _____ _ __         
 _____   / /_\/ _` | '_ ` _ \ / _ \  //  //\ \ / / _ \ '__|  _____ 
|_____| / /_\\ (_| | | | | | |  __/ / \_//  \ V /  __/ |    |_____|
        \____/\__,_|_| |_| |_|\___| \___/    \_/ \___|_|           
                                                                
"""

ascii_skull = """
                              ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`     

"""

def main():
    
    win = 0
    lose = 0
    lives = 3
    
    #chosen_rank = random.choice(rank)
    #chosen_first = random.choice(first_name)
    #chosen_last = random.choice(last_name)
    #fighter = f"{chosen_first} {chosen_last} {chosen_rank}"
    #print(fighter)
    
    print(ascii_welcome)
    print()
    print(ascii_to_the)
    print()
    print(ascii_arena)
    print()
    print()
    print("- - - - - - - - - - - - - - - - - - - - - - - - ")
    print()
    print()
    print("             Welcome to the Gladiatorial Arena!")
    time.sleep(2)
    print("""
    Prepare to face a series of fierce challengers in battle!
    To win your fights, you'll need to answer a variety of math questions.
        Be careful—each wrong answer costs you a life!
            You have three lives, so use them wisely!
          """)
    time.sleep(1)
    print() 
    print()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print()
    print()
    
    while lives > 0:
        
        chosen_rank = random.choice(rank)
        chosen_first = random.choice(first_name)
        chosen_last = random.choice(last_name)
        fighter = f"{chosen_first} {chosen_last} {chosen_rank}"
        
        chosen_attack = random.choice(attacks)
        player_attack = random.choice(attacks)
        
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        rand_sum = random.choice(maths)
        
        symbol = {operator.add: '+', operator.sub: '-', operator.mul: '*'}[rand_sum]
        final_sum = f"{num_1} {symbol} {num_2}"
        correct_answer = rand_sum(num_1, num_2)
        
        print()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print()
        print(f"You Have Won {win} Games!")
        print()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("A new challenger enters the arena!")
        print(f"It's {fighter} — Get Ready To Fight! ")
        time.sleep(2)
        print()
        print()
        print(f"{fighter} {chosen_attack} at you!")
        print()
        print(f"|   |   {final_sum} |   |")
        player_guess = int(input("Your Awnser: "))
        print()
        
        if player_guess == correct_answer:
            print(f"Thats Correct! {player_guess} was the right Awnser!")
            print(f"You {player_attack} {fighter}")
            win += 1
            time.sleep(1)
            
        elif player_guess != correct_answer:
            print("OH NO! Thats Incorrect!")
            print(f"The right Awnser is {correct_answer}")
            lives -= 1
            print(f"you have taken a hit!")
            print(f"You have {lives} left!")
            time.sleep(1)
            
    print(ascii_game_over)  
    time.sleep(1)  
    print()
    print("Alas! You have fallen in the arena!")
    print("You now join the countless gladiators who met their end on these bloodstained sands.")
    print(f"Before your final breath, you claimed victory in {win} battles.")
    print()
    print(ascii_skull)
    print()
    print("Your name shall echo among the ghosts of the arena forevermore.")
    time.sleep(2)
    print()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print()
    print("Would you like to play again?")
    time.sleep(0.3)
    restart = input("Y or N :  ")
    
    if restart.lower() == "y":
        main()
    elif restart.lower() == "n":
        print()
        print("Thank You For Playing!") 
    elif restart.lower() == "god":
        lives = 100
        main()

if __name__ == '__main__':
    main()
