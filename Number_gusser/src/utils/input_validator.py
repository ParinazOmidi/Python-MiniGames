# def get_validated_input(prompt, start, end):
    # while True:
        # try: 
            # user_input = int(input(prompt))
            # if start <= user_input <= end:
                # return user_input
            # else:
                # print(f"Input must be between {start} and {end}. Please try again.")


def get_validated_input(start, end):  
    while True: 
        try:
            user_input = int(input('enter your number: '))
            if start <= user_input <= end: 
                print('valid input')
                return user_input
            else: 
                print(f'please enter a number between {start} and {end}')
                continue
        except ValueError:
            print('invalid input, please enter an integer')
            continue
