import random

class Neuron:
    def __init__(self, weights=[], bias=[], size =0):
        if weights == []:
            self.weights == []
            
            for i in range (size):
                self.weights.append(random.uniform (-1, 1,))
            else:
                self.weights = weights

            if bias == []:
                self.bias = random.uniform(-1, 1)
            else:
                self.bias= bias

        self.weights = weights
        self.bias = bias
    
    def forward(self, inpt):
        if len(inpt) != len(self.weights):
            print("Nein")
            return -1
        
        total = 0
        
        for i in range(len(inpt)):
            total += inpt[i] * self.weights[i]
            print("yo", i)

        total += self.bias
        return total