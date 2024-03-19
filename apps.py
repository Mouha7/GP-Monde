from cargaison import *
from produit import *

def main():
    cargaison_routiere = CargaisonRoutiere(1000)
    cargaison_maritime = CargaisonMaritime(2000)
    cargaison_aerienne = CargaisonAerienne(500)

    produit_alimentaire1 = ProduitAlimentaire("Pommes", 10)
    produit_chimique1 = ProduitChimique("Acide sulfurique", 5, 8)
    produit_fragile1 = ProduitMaterielFragile("Verre", 2)
    produit_incassable1 = ProduitMaterielIncassable("Fer", 15)
    
    print("\nAjout Cargaison routière :")
    cargaison_routiere.ajouter_produit(produit_alimentaire1)
    cargaison_routiere.ajouter_produit(produit_chimique1)
    cargaison_routiere.ajouter_produit(produit_fragile1)
    cargaison_routiere.ajouter_produit(produit_incassable1)
    cargaison_routiere.ajouter_produit(produit_incassable1)
    cargaison_routiere.ajouter_produit(produit_incassable1)
    cargaison_routiere.ajouter_produit(produit_incassable1)
    cargaison_routiere.ajouter_produit(produit_incassable1)
    cargaison_routiere.ajouter_produit(produit_incassable1)
    cargaison_routiere.ajouter_produit(produit_incassable1)
    cargaison_routiere.ajouter_produit(produit_incassable1)
    cargaison_routiere.ajouter_produit(produit_incassable1)
    cargaison_routiere.ajouter_produit(produit_incassable1)
    print("\nAjout Cargaison maritime :")
    cargaison_maritime.ajouter_produit(produit_alimentaire1)
    cargaison_maritime.ajouter_produit(produit_chimique1)
    cargaison_maritime.ajouter_produit(produit_incassable1)
    print("\nAjout Cargaison aérienne :")
    cargaison_aerienne.ajouter_produit(produit_alimentaire1)
    cargaison_aerienne.ajouter_produit(produit_chimique1)
    cargaison_aerienne.ajouter_produit(produit_fragile1)
    cargaison_aerienne.ajouter_produit(produit_incassable1)

    print("\nCargaison routière :")
    print(f"Somme totale : {cargaison_routiere.get_somme_totale():,.2f}")
    print(f"Nombre de produits : {cargaison_routiere.get_nb_produits()}")

    print("\nCargaison maritime :")
    print(f"Somme totale : {cargaison_maritime.get_somme_totale():,.2f}")
    print(f"Nombre de produits : {cargaison_maritime.get_nb_produits()}")

    print("\nCargaison aérienne :")
    print(f"Somme totale : {cargaison_aerienne.get_somme_totale():,.2f}")
    print(f"Nombre de produits : {cargaison_aerienne.get_nb_produits()}")


if __name__ == "__main__":
    main()