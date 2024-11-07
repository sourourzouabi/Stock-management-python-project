class Adresse:
    def __init__(self,Tunis,Tunisie):
        self.rue=''
        self.ville=Tunis
        self.pays=Tunisie 

    def Setrue(self,rue):
       self.rue=rue
    def Setville(self,ville):
        self.ville=ville
    def Setpays(self,pays):
        self.pays=pays
    def Getrue(self):
        return self.rue
    def Getville(self):
        return self.ville
    def Getpays(self):
        return self.pays
   
    def to_chaine_adresse(self):
     msg='%-8s;%-8s;%-8s\n'%(self.rue,self.ville,self.pays)
     return msg

    def saisir(self):  
     self.rue= input("entrer la rue")
     self.ville= float(input("entrer la ville"))
     self.pays= int(input("entrer la pays"))




class Client:
    def __init__(self,nom,type,adresse) :
     self.nom=nom
     self.type=type
     self.adresse=adresse
    def Setnom(self,nom):
       self.nom=nom
    def Settype(self,type):
        self.type=type
    def Setadresse(self,adresse):
        self.adresse=adresse
    def Getnom(self):
        return self.nom
    def Gettype(self):
        return self.type
    def Getadresse(self):
        return self.adresse
    
    def to_chaine_client(self):

     msg='%-8s %-15s %-8s'%(nom,type)+ Adresse.to_chaine_adresse()
     return msg

    def saisir(self):  
     self.nom= input("entrer le nom")
     self.type= float(input("entrer le type"))
     Adresse.saisir_adresse()


    def afficher():
     produit= to_chaine_client(self)
     print(produit)
     
     
a1=Adresse('Republique','Bizerte')
c1=Client('VenteElectro','Professionnel',a1)
c1.afficher()
# client 2
a2=Adresse(rue='Ibn Khaldoun')
c2=Client(nom='Walid')
c2.afficher()
# client 3
c3=Client()
c3.Setnom('Sonia')
c3.Settype('Particulier')
a3=Adresse()
a3.Setrue('Ibn Jazzar')
a3.Setrue('Kairouan')
c3.Setadresse(a3)
c3.afficher()
# client 4
c4=Client()
c4.saisir()
c4.afficher()
