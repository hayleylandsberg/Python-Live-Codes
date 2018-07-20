from building import Building

class Outhouse(Building):

    def __init__(self):
        super().__init__()
        self.dignity = False
        self.toilets = 1

# def __str__():
# #print(f'I am a stinky {self.__class__} and I have {self.dignity} dignity')