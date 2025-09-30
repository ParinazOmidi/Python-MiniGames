import random

class RockPaperScissors:
    def __init__(self, name): 
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name 


    def get_player_choice(self): 
        user_choice= input (f'Enter your choice ({self.choices}): ')
        if user_choice.lower() in self.choices: 
            return user_choice.lower()
        
        print(f'Invalid choice, you must select from {self.choices}. ')
        return self.get_player_choice()


    def get_camputer_choice (self):
        return random.choice(self.choices)


    def decide_winner(self, user_choice , camputer_choice):
        if user_choice == camputer_choice: 
            return "It's a Tie!"
        
        win_combination = [ 
            ('paper','rock'),
            ('scissors','paper'),
            ('rock','scissors')
        ]
        for win_comb in  win_combination: 
            if (user_choice == win_comb[0]) & (camputer_choice == win_comb[1]):
                return (f"{self.player_name} won the game!")
            
    
        return (f"{self.player_name} Sorry it seems you lose the game!")


    def play(self): 
        user_choice = self.get_player_choice()
        camputer_choice = self.get_camputer_choice()
        print(f'Computer choice: {camputer_choice}')
        winner_message= self.decide_winner(user_choice, camputer_choice)
        print(winner_message)


game = RockPaperScissors('parinaz')

while True: 
    game.play()

    continue_game = input('do you want to play again? (Enter any key to play again, enter q to exit) ')
    if continue_game.lower() == 'q': 
        break
