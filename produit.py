from abc import ABC

class Produit(ABC):
    def __init__(self, libelle, poids) -> None:
        self.__libelle = libelle
        self.__poids = poids
    
    def get_libelle(self):
        return self.__libelle
    
    def set_libelle(self, new_libelle):
        self.__libelle = new_libelle
        
    def get_poids(self):
        return self.__poids
    
    def set_poids(self, new_poids):
        self.__poids = new_poids
    
    def info(self):
        print(f"Libellé : {self.__libelle}, Poids : {self.__poids}")

class ProduitAlimentaire(Produit):
    pass

class ProduitChimique(Produit):
    def __init__(self, libelle, poids, degree_toxicite) -> None:
        super().__init__(libelle, poids)
        self.__degree_toxicite = degree_toxicite
    
    def get_degree_toxicite(self):
        return self.__degree_toxicite
    
    def set_degree_toxicite(self, new_degree_toxicite):
        self.__degree_toxicite = new_degree_toxicite

    def info(self):
        super().info()
        print(f"Degré de tonicité : {self.__degree_toxicite}")


class ProduitMateriel(Produit):
    pass

class ProduitMaterielFragile(ProduitMateriel):
    pass

class ProduitMaterielIncassable(ProduitMateriel):
    pass