
class Error (Exception):
    
    def __init__(self, message = "You done fucked up boi"):
        self.message = message

        super().__init__(self.message)
    

class DifficultyError (Exception):
    

    def __init__(self, difficulty:int, message = "Invalid Difficulty"):
        self.message = message
        print('Invalid Difficulty')
        super().__init__(self.message)

class SolutionOverloadError(Exception):

    def __init__(self,  message = "Too many Solutions"):
        self.message = message

        super().__init__(self.message)