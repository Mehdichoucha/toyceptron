from layer import Layer

class Network:
    def __init__(self, input_size = [], activation = []):
        self.input_size = input_size
        self.activation = activation
        self.layers = []

    def add(self, weights, biases):
        self.layers.append(Layer(weights, biases))
    def feedforward(self, input):
        for layer in self.layers:
            input = layer.forward(input)
            input = [self.activation(o) for o in input]
        return input