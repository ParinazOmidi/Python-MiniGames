import sys
import os
from src.utils.input_validator import get_validated_input
from src.game_logic.hint_generator import provide_hint
from src.game_logic.number_generator import generate_random_number
from src.game_logic.scorer import Score

def main():
    actual_number = generate_random_number(1,100)
    game_score = Score ()
    print("Welcome to the Number Guessing Game!")

    while True: 
        user_input = get_validated_input(1,100)
        if user_input == actual_number: 
            print(f"Congratulations! Your final score is: {game_score.get_score()}")
            break
        else: 
            hint =provide_hint(user_input, actual_number)
            print(hint)
            game_score.decrement_score(10)
            

            

if __name__ == '__main__':
    main()






