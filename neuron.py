class Neuron:
    def __init__(self, poid, bias):
        """
        poid : liste de nombres (poids)
        bias : nombre
        """
        self.poid = poid
        self.bias = bias

    def forward(self, inputs):
        """
        inputs : liste de nombres (même taille que poid)
        retourne : somme pondérée + biais
        """
        total = 0

        # Produit scalaire
        for w, x in zip(self.poid, inputs):
            total += w * x

        # Ajout du biais
        total += self.bias

        return total
