from ObjetsSpatiaux import Coordonnees, ObjetSpatial
from Modules        import *


class Vaisseau(ObjetSpatial) :

    """
    Classe Vaisseau :
    Ceci est la classe mere de tout vaisseau spatial.
    """

    def __init__(self, nom, pt_central, coque, moteur, systeme_vital) :
        ObjetSpatial.__init__(self, pt_central)
        self.nom           = nom
        self.coque         = coque
        self.moteur        = moteur
        self.systeme_vital = systeme_vital
        self.vie           = coque.get_vie()     + moteur.get_vie()     + systeme_vital.get_vie()
        self.vie_max       = coque.get_vie_max() + moteur.get_vie_max() + systeme_vital.get_vie_max()
        pass

    def get_nom(self) :
        return self.nom

    def get_vie(self) :
        return self.vie

    def get_vie_max(self) :
        return self.vie_max

    def __repr__(self) :
        rep = "Ce vaisseau a une vie de " + str(self.vie) + "/" + str(self.vie_max)
        return rep


