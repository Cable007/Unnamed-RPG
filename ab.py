from string import *
class AB:
    def __init__(self, l, u, *args):
        self.l = [ord(n) for n in l]
        self.u = [ord(n) for n in u]
        self.a = self.u + self.l

key = AB(ascii_lowercase, ascii_uppercase)