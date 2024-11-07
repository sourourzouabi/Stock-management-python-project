def saisir_produit():
  nom= input("entrer le nom")
  puht= float(input("entrer le puht"))
  quantite= int(input("entrer la quantite"))
  return (nom,puht,quantite)

def afficher_produit(nom,puht,quantite):
    produit='%-8s|%-8.2f|%-5d' %(nom,puht,quantite)
    print(produit)

def produit2chaine(nom,puht,quantite):
  message='%s;%f;%d\n'%(nom,puht,quantite)
  return message

def chaine2produit(message):
    message.rstrip() 
    nom,puht,quantite=message.split(";")
    return nom,float(puht),int(quantite)


