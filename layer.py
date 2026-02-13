from neuron import Neuron

class Layer:
    def __init__(self, weights_list=[], biases_list=[]):
        self.neurons = []

        for i in range(len(weights_list)):
            n = Neuron(weights=weights_list[i], bias=biases_list[i])
            self.neurons.append(n)

    def forward(self, input):
        outputs = []

        for n in self.neurons:
            output = n.forward(input)
            outputs.append(output)

        return outputs