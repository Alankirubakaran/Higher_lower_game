import art
import random
from game_data import data

print(art.logo)

# Initialize the score outside the result function to keep it persistent
Current_score = 0

def result(choice, choice_1, choice_2):
    global Current_score
    if choice == 'A':
        if choice_1['follower_count'] > choice_2['follower_count']:
            Current_score += 1
            print(f"You're right! Current score: {Current_score}")
            return True  # Game continues, swap choices
        else:
            print(f"Sorry, that's wrong. Final score: {Current_score}")
            return False  # End the game
    elif choice == 'B':
        if choice_1['follower_count'] < choice_2['follower_count']:
            Current_score += 1
            print(f"You're right! Current score: {Current_score}")
            return True  # Game continues, swap choices
        else:
            print(f"Sorry, that's wrong. Final score: {Current_score}")
            return False  # End the game
    return False  # If no valid choice, end the game

game_should_continue = True

# Start the game loop
while game_should_continue:
    # Randomly choose two different items
    choice_1 = random.choice(data)
    choice_2 = random.choice(data)
    while choice_1 == choice_2:  # Ensure the two choices are different
        choice_2 = random.choice(data)

    print(f"Compare A: {choice_1['name']}, a {choice_1['description']}, from {choice_1['country']}")
    print(art.vs)
    print(f"Against B: {choice_2['name']}, a {choice_2['description']}, from {choice_2['country']}")

    # Get the user's choice and make the comparison
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    print("\n" * 20)
    print(art.logo)

    # Check if the user wants to continue the game
    game_should_continue = result(choice, choice_1, choice_2)
    
    if game_should_continue:
        # If the game continues, update choice_1 to the correct choice
        if choice == 'A' and choice_1['follower_count'] > choice_2['follower_count']:
            choice_1 = choice_1
        elif choice == 'B' and choice_1['follower_count'] < choice_2['follower_count']:
            choice_1 = choice_2
        
        # Randomize choice_2 to a new, different item for the next round
        choice_2 = random.choice(data)
        while choice_1 == choice_2:  # Ensure the two choices are different
            choice_2 = random.choice(data)
