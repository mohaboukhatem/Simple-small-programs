class CompteBancaire:
    
    def __init__(self,id,nom,solde):
        self.nom=nom
        self.id=id
        self.solde=int(solde)
    
    def virer(self,somme):
        if somme <= 0 :
            print("donnez une correcte somme ! ")
        else : self.solde+=somme
    
    def retirer(self,somme):
        if somme <= 0 or somme > int(solde) :
            print("donnez une correcte somme ! ")
        else : self.solde+=somme
    
    def consulter(self):
        print(" id    : "+self.id)
        print(" nom   : "+self.nom)
        print(" solde : "+str(self.solde))

   id=input("donnez votre id    : ")
  nom=input("donnez votre nom   : ")
solde=input("donnez votre solde : ")

compte=CompteBancaire(id,nom,solde)
n=0
while n != 4 : 
    print(" 1 - virer ")
    print(" 2 - retirer ")
    print(" 3 - consulter ")
    print(" 4 - exit ")

    choix = int(input("entrez votre choix : "))
    if choix == 1 : 
        k = int(input("donnez la somme : "))
        compte.virer(k)
    elif choix == 2 : 
        k = int(input("donnez la somme : "))
        compte.retirer(k)
    elif choix == 3 : 
        compte.consulter()
    elif choix == 4 : 
        n=4