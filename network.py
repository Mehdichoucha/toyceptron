from layer import Layer


class Network:
    def __init__(self, input_size, activation):
        """
        input_size : nombre d'entrées du réseau
        activation : fonction d'activation à appliquer après chaque couche
        """
        self.layers = []
        self.activation = activation
        self.input_size = input_size

    def add(self, poid, bias):
        """
        Ajoute une couche au réseau
        poid : liste de listes de poids (un neurone par liste)
        bias : liste de biais (un par neurone)
        """
        layer = Layer(poid, bias)
        self.layers.append(layer)

    def feedforward(self, inputs):
        """
        Propagation avant complète
        inputs : liste de nombres
        retourne : liste des sorties activées
        """
        for layer in self.layers:
            raw = layer.forward(inputs)           # sortie brute de la couche
            inputs = [self.activation(o) for o in raw]  # activation
        return inputs
