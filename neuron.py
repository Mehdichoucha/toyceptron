class Neuron :
    def __init__(self,weights, bias):
        self.weights = weights
        self.bias = bias

    def forward(self, input):
        if len(input) != len(self.weights):
            print("Nein")
            return -1
        total = 0
        for i in range(len(input)):
            total = total + input[i] * self.weights[i]
        total = total + self.bias
        return total