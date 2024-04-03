class Padlock():
    def __init__(self, key='0000', locked= True):
        self.__key = key
        self.locked = locked
    def unlock(self, combiation):
        if combiation == self.__key:
            self.locked =  False
            return True
    def lock(self):
        self.locked = True
    def getKey(self):
        return self.__key
    def setKey(self, key):
        if len(key) == 4:
            self.__key = key
            return True
        else:
            return False
