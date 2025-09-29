def provide_hint(user_input: int, actual_number: int) -> str: 
    ## provide a hint based on the guess and target number
    if user_input < actual_number: 
        return "your guess is too low"
    else: 
        return "your guess is too high "
    
