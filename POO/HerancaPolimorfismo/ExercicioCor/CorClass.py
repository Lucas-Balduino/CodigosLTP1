class Cor():
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B
        
    def getCor(self):
        self.R /= 255
        self.G /= 255
        self.B /= 255
        tuplaCores = (self.R, self.G, self.B)
        return tuplaCores
        
        