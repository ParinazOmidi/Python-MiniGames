class score: 
    def __init__(self, initial_score=100):
        self.score = initial_score

    def decrement_score (self, penalty=10):
        ##Decrese penalty score## 
        self.score -= penalty
        self.score = max(self.score, 0)
         
    def get_score (self): 
        ##return current score##
        return self.score
def scorer(): 
    return score()
# if __name__ == '__main__':
#     score()






















