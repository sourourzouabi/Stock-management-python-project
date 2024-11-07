class Produit:
    def __init__(self,nom='',puht=0,quantite=0) :
        self.nom=nom
        self.puht=puht
        self.quantite=quantite

    def afficher(self):
        produit='%-8s | %-8.2f | %-5d' %(self.nom,self.puht,self.quantite)
        print(produit)  

    def saisir(self):  
     self.nom = input("entrer le nom : ")
     self.puht= float(input("entrer le puht : "))
     self.quantite= int(input("entrer la quantite : "))

    def to_chaine(self):
       message='%s;%f;%d\n'%(self.nom,self.puht,self.quantite)
       return message

    def from_chaine(self):
     message=self.to_chaine()
     message.rstrip() 
     nom,puht,quantite=message.split(";")
     self.nom = str(nom)
     self.puht = float(puht)
     self.quantite = int(quantite)
     return self.nom,self.puht,self.quantite

    def setNom(self,nom):
      self.nom=nom

    def setPuht(self,puht):
       self.puht=puht 

    def setQuantite(self,quantite):
       self.quantite=quantite
    
    def getNom(self):
        return self.nom

    def getPuht(self):
        return self.puht 

    def getQuantite(self):
        return self.quantite 



#tester la foncion afficher 
print("\n tester la foncion afficher  \n")
p1=Produit("TV",1200.55,5)
p1.afficher()

#tester la fonction saisir
print("\n tester la foncion saisir  \n")
p2=Produit()
p2.saisir()
p2.afficher()

#tester les fonctions setters 
print("\n tester les fonctions setters   \n")
p3=Produit()
p3.setNom('MO')
p3.setPuht(350.556)
p3.setQuantite(25)
p3.afficher()

#tester les fonctions getters
print("\n tester les fonctions getters   \n")
nom=p3.getNom()
puht=p3.getPuht()
quantite=p3.getQuantite()
p4=Produit(nom,puht,quantite)
p4.afficher()

#tester la fonction from_chaine 
print("\n tester la fonction from_chaine    \n")

p5=Produit()
p5.saisir()
p5.from_chaine()
p5.afficher()

#tester la fonction produit de chaine
print("\n tester la fonction produit de chaine  \n")
print(p5.to_chaine())
