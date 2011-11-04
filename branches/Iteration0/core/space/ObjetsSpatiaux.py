class Coordonnees(object) :

    """
    Classe Coordonnees :
    Cette classe définie le systeme de coordonnees de tout objet spatial
    On la construit en indicant les type du referentiel suivi des coordonnees
    (ex : Coordonnees('cartesien',3,4.5) donne x=3.0, y=4.5, z=0.0)
    ou en indicant le nom des coordonnees dans le constructeur
    (ex : Coordonnees(x=3,z=5.9) donne x=3.0, y=0.0, z=5.9)
    """

    def __init__(self, *non_nommes, **nommes) :

        self.referentiel = 'none'

        # Enregistrement des coordonnees depuis une liste
        if len(non_nommes) :
            self.referentiel = non_nommes[0].lower()
            if self.referentiel == 'cartesien' :
                self.x = 0.
                self.y = 0.
                self.z = 0.
                # Enregistrement de la coordonnee x
                if len(non_nommes)>1 :
                    self.x = float(non_nommes[1])
                # Enregistrement de la coordonnee y
                if len(non_nommes)>2 :
                    self.y = float(non_nommes[2])
                # Enregistrement de la coordonnee z
                if len(non_nommes)>3 :
                    self.z = float(non_nommes[3])
                pass
            pass

        # Enregistrement des coordonnees depuis un dictionnaire
        elif len(nommes) :
            if nommes.get('x') or nommes.get('y') or nommes.get('z') :
                self.referentiel = 'cartesien'
                self.x = 0.
                self.y = 0.
                self.z = 0.
                if nommes.get('x') :
                    self.x = float(nommes['x'])
                if nommes.get('y') :
                    self.y = float(nommes['y'])
                if nommes.get('z') :
                    self.z = float(nommes['z'])
                pass
            pass

    def get_x(self) :
        if self.referentiel == 'cartesien' :
            return self.x
        else :
            return 0.
    
    def get_y(self) :
        if self.referentiel == 'cartesien' :
            return self.y
        else :
            return 0.
    
    def get_z(self) :
        if self.referentiel == 'cartesien' :
            return self.z
        else :
            return 0.

    def set_x(self, x) :
        if self.referentiel == 'cartesien' :
            self.x = x

    def set_y(self, y) :
        if self.referentiel == 'cartesien' :
            self.y = y

    def set_z(self, z) :
        if self.referentiel == 'cartesien' :
            self.z = z

    def __repr__(self) :
        if self.referentiel == 'cartesien' :
            rep = "~~ Coordonnees Cartesiennes ~~\n"
        else :
            rep = "~~ Coordonnees ~~\n"
        rep += "{0}, {1}, {2}".format( str(self.get_x()), str(self.get_y()), str(self.get_z()) )
        return rep

    def __str__(self) :
        return self.__repr__()



class ObjetSpatial(object) :

    """
    Classe ObjetSpatial :
    Ceci est la classe mere de tout objet se trouvant dans l'espace
    """

    def __init__(self, point_central = Coordonnees()) :
        self.point_central = point_central
        pass

    def get_point_central(self) :
        return self.point_central

    def __repr__(self) :
        rep  = "Cette objet spatial se trouve aux coordonnees suivantes :\n"
        rep += self.point_central.__repr__()
        return rep

    def __str__(self) :
        return self.__repr__()

