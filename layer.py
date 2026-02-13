class Layer:

    def __init__(self, weights_list = [], biases_list=[]):
        self.neurons = []
        for i in range (len(weights_list)):
            self.weights_list = weights_list[i]
        for i in range (len(biases_list)):
            self.biases_list = biases_list[i]


    def forward(self, inpt):

        for neuron in self.neurons:
            neuron.forward
        self.input = inpt

        total = 0

        for o in range(len(inpt)):
            total += inpt[o] * self.weights[o]
            print("yo", o)
            