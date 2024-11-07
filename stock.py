from produit import *

noms=[]
puhts=[]
quantites=[]


def ajouter_produit(nom,puht,quantite):
    noms.append(nom)
    puhts.append(puht)
    quantites.append(quantite)
    return noms,puhts,quantites
N=0
def saisir_stock(N):
    N=int(input('Entrer Nombre de produit :'))
    for i in range(N):
        nom,puht,quantite=saisir_produit()
        ajouter_produit(nom,puht,quantite)



def afficher_stock():
    print('NOM     |PUHT    |QUANTITE')
    for i in range(len(noms)) :
        afficher_produit(noms[i],puhts[i],quantites[i])


def rechercher_produit(nom): 
  indice=None
  se_trouve=False 
  for i in range (0,len(noms)):
    if nom==noms[i] :
       indice=i 
       se_trouve=True
  return se_trouve,indice


def supprimer_produit(nom):
   a=rechercher_produit(nom)
   if a[0]==True :
      i=0
      while noms[i]!=nom:
         i=i+1
      noms.remove(nom)
      puhts.remove(puhts[i])
      quantites.remove(quantites[i])
      return True 
   elif a[0]==False :
    return False



def modifier_produit(nom,nom_new,puht_new,quantite_new):
   a=rechercher_produit(nom)
   if a[0]==True :
       i=0
       while nom!=noms[i]:
        i=i+1
       noms[i]= nom_new
       puhts[i]=puht_new
       quantites[i]=quantite_new 
       return True
   else:
        return False 


global max
max=100 
def acheter_produit(nom,quantite):
    
    i=0
    while nom!=noms[i]:
        i=i+1
    
    if  quantites[i]+quantite >= max:
       
        return False 
    elif quantites[i]+quantite <=max :
        
        quantites[i]= quantites[i]+quantite
        
        return True

def vendre_produit(nom,quantite):
      
    i=0
    while nom!=noms[i]:
        i=i+1
    
    if  quantites[i]<quantite:
       
        return False 
    else:
        
        quantites[i]= quantites[i]-quantite
        
        return True

def enregistrer_stock(fich):
    fichier = open(fich,'w+')
    for i in range(len(noms)) :
        produits=produit2chaine(noms[i],puhts[i],quantites[i])
        fichier.write(produits)
    fichier.close()
enregistrer_stock('produits.txt')


def charger_stock(fich):
    fichier = open(fich,'r')
    for ligne in fichier :
        nom,puht,quantite=chaine2produit(ligne)
        noms.append(nom)
        puhts.append(puht)
        quantites.append(quantite)
    return noms,puhts,quantites
    