class Logic(object):

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def AND(self):
        if self.s1 and self.s1 == 1:
            return True
        else:
            return False
