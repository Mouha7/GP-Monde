from abc import ABC, abstractmethod
from produit import *

class Cargaison(ABC):
    def __init__(self, distance) -> None:
        self.__distance = distance
        self.__produits = []
        self.__frais = 0
    
    def ajouter_produit(self, produit):
        if(len(self.__produits) < 10):
            self.__produits.append(produit)
            self.__frais += self.calculer_frais(produit)
            print(f"Produit ajouté({produit.get_libelle()}) => Montant total de la cargaison : {self.__frais:,.2f}")
        else:
            print("La cargaison est pleine. Impossible d'ajouter un nouveau produit.")

    def get_frais(self):
        return self.__frais
    
    def get_distance(self):
        return self.__distance
    
    def set_distance(self, new_distance):
        self.__distance = new_distance
    
    def get_produits(self):
        return self.__produits
    
    def set_produits(self, new_produits):
        self.__produits = new_produits

    @abstractmethod
    def calculer_frais(self, produit):
        pass
    
    def get_somme_totale(self):
        return self.__frais
        
    def get_nb_produits(self):
        return len(self.__produits)

class CargaisonRoutiere(Cargaison):
    def calculer_frais(self, produit):
        if isinstance(produit, ProduitAlimentaire):
            return 100 * produit.get_poids() * self.get_distance()
        elif isinstance(produit, ProduitChimique):
            print("Les produits chimiques ne peuvent pas être transportés par voie routière.")
            return 0
        elif isinstance(produit, ProduitMateriel):
            return 800 * produit.get_poids() * self.get_distance()
        return 0

class CargaisonMaritime(Cargaison):
    def calculer_frais(self, produit):
        if isinstance(produit, ProduitAlimentaire):
            return (90 * produit.get_poids() * self.get_distance()) + 5000
        elif isinstance(produit, ProduitChimique):
            return (500 * produit.get_poids() * produit.get_degree_toxicite()) + 10000
        elif isinstance(produit, ProduitMateriel):
            if isinstance(produit, ProduitMaterielIncassable):
                return 400 * produit.get_poids() * self.get_distance()
            else:
                print("Les produits fragiles ne peuvent pas être transportés par voie maritime.")
                return 0
        return 0

class CargaisonAerienne(Cargaison):
    def calculer_frais(self, produit):
        if isinstance(produit, ProduitAlimentaire):
            return 300 * produit.get_poids() * self.get_distance()
        elif isinstance(produit, ProduitChimique):
            print("Les produits chimiques ne peuvent pas être transportés par voie aérienne.")
            return 0
        elif isinstance(produit, ProduitMateriel):
            return 1000 * produit.get_poids()
