from neuron import Neuron


class Layer:
    def __init__(self, poid_list, bias_list):
        """
        poid_list : liste de listes (poid de chaque neurone)
        bias_list : liste de biais (un par neurone)
        """
        self.neurons = []

        # Création des neurones
        for poid, bias in zip(poid_list, bias_list):
            neuron = Neuron(poid, bias)
            self.neurons.append(neuron)

    def forward(self, inputs):
        """
        inputs : liste de nombres
        retourne : liste des sorties brutes des neurones
        """
        outputs = []

        for neuron in self.neurons:
            outputs.append(neuron.forward(inputs))

        return outputs
