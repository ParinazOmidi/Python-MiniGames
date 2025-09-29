import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.utils.input_validator import get_validated_input
from src.game_logic.hint_generator import provide_hint
from src.game_logic.number_generator import generate_random_number
from src.game_logic.scorer import score

def main():
    actual_number = generate_random_number(1,100)
    game_score = score ()
    print("Welcome to the Number Guessing Game!")

    while True: 
        user_input = get_validated_input(1,100)
        if user_input == actual_number: 
            print(f"You guess the numner {game_score} guesses.")
            break
        else: 
            hint =provide_hint(user_input, actual_number)
            print(hint)
            game_score.decrement_score(10)
            

            # print(f"Your current score is: {score.get_score()}")

if __name__ == '__main__':
    main()

    # user_input = get_validated_input(1,100)
    # print(f'You entered: {user_input}')


print('Current Directory:', os.getcwd)
print('sys.path:',sys.path)




# game_score -= 10
#             print(f"Your current score is: {game_score}")
#             if game_score <= 0:
#                 print(f"Game Over! The correct number was {actual_number}.")
#                 break