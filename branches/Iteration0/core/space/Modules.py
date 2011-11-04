class Module(object) :

    """
    Classe Module :
    Ceci est une sous-partie d'un vaisseau spatial
    """

    def __init__(self, vie_max) :
        self.vie_max = vie_max
        self.vie     = vie_max
        self.actif   = True
        pass

    def desactive(self) :
        self.actif = False
        pass

    def active(self) :
        self.actif = True
        pass

    def repare(self, gain) :
        if self.vie == 0 :
            self.active()
            pass
        self.vie += gain
        if self.vie > self.vie_max :
            self.vie = self.vie_max
            pass
        pass

    def endommage(self, perte) :
        if self.vie < perte :
            self.detruit()
        else :
            self.vie -= perte
        pass

    def detruit(self) :
        self.desactive()
        self.vie = 0
        pass

    def get_vie_max(self) :
        return self.vie_max

    def get_vie(self) :
        return self.vie

    def is_actif(self) :
        return self.actif

    def __repr__(self) :
        rep  = "Ce module a une vie de " + str(self.vie) + "/" + str(self.vie_max)
        return rep



class Coque(Module) :

    """
    Classe Coque :
    Ceci est une sous-partie principale d'un vaisseau spatial.
    """

    def __init__(self, vie_max) :
        Module.__init__(self, vie_max)
        pass

    def __repr__(self) :
        rep = "Cette coque a une vie de " + str(self.vie) + "/" + str(self.vie_max)
        return rep



class Moteur(Module) :

    """
    Classe Moteur :
    Ceci est une sous-partie d'un vaisseau spatial.
    """

    def __init__(self, vie_max, puissance) :
        Module.__init__(self, vie_max)
        self.puissance = puissance
        pass

    def get_puissance(self) :
        return self.puissance

    def __repr__(self) :
        rep  = "Ce moteur a une vie de " + str(self.vie) + "/" + str(self.vie_max) + "\n"
        rep += "Il a une puissance de " + str(self.puissance)
        return rep



class MoteurConventionnel(Moteur) :

    """
    Classe MoteurConventionnel :
    Ceci est une sous-partie principale d'un vaisseau spatial.
    Il permet de mettre en mouvement un vaisseau.
    """

    def __init__(self, vie_max, puissance, vitesse_max) :
        Moteur.__init__(self, vie_max, puissance)
        self.vitesse_max = vitesse_max
        pass

    def get_vitesse_max(self) :
        return self.vitesse_max

    def __repr__(self) :
        rep  = "Ce moteur conventionnel a une vie de " + str(self.vie) + "/" + str(self.vie_max) + "\n"
        rep += "Il a une puissance de " + str(self.puissance) + " et il peut atteindre une vitesse maximale de " + str(self.vitesse_max)
        return rep



class MoteurHyperEspace(Moteur) :

    """
    Classe MoteurHyperEspace :
    Ceci est une sous-partie d'un vaisseau spatial.
    Il permet a un vaisseau d'effectuer des bonds d'hyper-espace.
    """

    def __init__(self, vie_max, puissance, portee) :
        Moteur.__init__(self, vie_max, puissance)
        self.portee = portee
        pass

    def get_portee(self) :
        return self.portee

    def __repr__(self) :
        rep  = "Ce moteur d'hyper-espace a une vie de " + str(self.vie) + "/" + str(self.vie_max) + "\n"
        rep += "Il a une puissance de " + str(self.puissance) + " et une portee de " + str(self.portee)
        return rep



class SystemeVital(Module) :

    """
    Classe SystemeVital :
    Ceci est une sous-partie principale d'un vaisseau spatial.
    Il permet de maintenir en vie l'équipage.
    """

    def __init__(self, vie_max, nb_equipage) :
        Module.__init__(self, vie_max)
        self.nb_equipage = nb_equipage
        pass

    def get_nb_equipage(self) :
        return self.nb_equipage

    def __repr__(self) :
        rep  = "Ce systeme de survie a une vie de " + str(self.vie) + "/" + str(self.vie_max) + "\n"
        rep += "Il permet d'acceuillir " + str(self.nb_equipage) + " membre(s) d'equipage"
        return rep



class Bouclier(Module) :

    """
    Classe Bouclier :
    Ceci est une sous-partie d'un vaisseau spatial.
    Il permet d'ajouter une protection a un vaisseau.
    """

    def __init__(self, vie_max, puissance, regeneration) :
        Module.__init__(self, vie_max)
        self.puissance    = puissance
        self.niveau       = puissance
        self.regeneration = regeneration
        pass

    def regenere(self, nb_clock) :
        self.niveau += nb_clock * self.regeneration
        if self.niveau > self.puissance :
            self.niveau = self.puissance
        pass

    def endommage(self, perte) :
        self.niveau -= perte
        if self.niveau < 0 :
            Module.endommage(self, - self.niveau )
            self.niveau = 0
            pass
        pass

    def get_puissance(self) :
        return self.puissance

    def get_niveau(self) :
        return self.niveau

    def get_regeneration(self) :
        return self.regeneration

    def __repr__(self) :
        rep  = "Ce bouclier a une vie de " + str(self.vie) + "/" + str(self.vie_max) + "\n"
        rep += "Il a une puissance de " + str(self.niveau) + "/" + str(self.puissance) + " et peut se regenerer a la vitesse de " + str(self.regeneration)
        return rep

