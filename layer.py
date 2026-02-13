from neuron import Neuron

class Layer:
    def __init__(self, weights_list = [], biases_list=[]):
        self.neurons = []
        for i in range(len(weights_list)):
            neuron = Neuron(weights=weights_list[i], bias=biases_list[i])
            self.neurons.append(neuron)
            
    def forward(self, input):
        outputs = []
        for neuron in self.neurons:
            result = neuron.forward(input)
            outputs.append(result)
        return outputs
