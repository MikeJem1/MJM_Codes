


class Machinn():
    kawotchou=4 

    def __init__(self):
        self.pwopriyete="Maignan"
        self.ane="2012"
        self.model="Toyota"
        self._pri=170000
        self.koule="Nwa"
        self.gaz=3500 #lit
        self.tente=False
        self.vites=0

    @property
    def pri(self):
        return self._pri

    #pou afiche mesaj pou le pri a chanje a
    @pri.setter
    def pri(self, nouvo_pri):
        if nouvo_pri > self._pri:
            print(f"vale machinn nan ogmante madam/mesye {self.pwopriyete}")
            self._pri = nouvo_pri
        elif nouvo_pri<self._pri:
            print(f"machinn nan pedi vale madam/mesye {self.pwopriyete}")
    
    @property
    def tente(self):
        return self._tente
    
    @tente.setter
    def tente(self,valeur):
        if valeur and not self._tente:
            print("ATANSYON : pa bliye fok ou gen papye DGI")

        self._tente=valeur

    def akselere(self):
        if self.gaz > 0:
            self.vites += 34
            self.gaz -= 14
        else:
            print("ou pa gen ase gaz")
    
    def frennen(self):
        if self.vites>0:
            self.vites -=58
            self.gaz-=7

    def VannMachinn(self):
        self.pwopriyete=input("rantre nouvo pwopriyete a")
        print(self.pwopriyete)
        print(self.pri)

    def douko(self):
        self.koule=input("nouvo koule a")
        self.pri += 200

    def Achtegaz(self,kob):
        if self.gaz <3500:
            if kob>198.1505:
                self.gaz +=(kob/198.1505)
                self.pri -= (1000/3)
        else:
            print("machinn nan foul")    
    def TenteMachinn(self):
        self.tente=True
   


def afficher_menu():
    print("\nMenu:")
    print("1. Akselere machinn nan")
    print("2. Frennen machinn nan ")
    print("3. Vann machinn nan")
    print("4. Chanje koule machinn nan")
    print("5. Achte  gaz")
    print("6. afiche enfo machinn nan ")
    print("7. tente machinn nan")
    print("8. kite")

# Création d'une instance de la classe Voiture
MachinnMwen=Machinn()
    #mwen kreye fonksyon sa jis pou nou ka afiche enfomasyon machinn nan 
def Dashbod():
    print(f"pwopiyete: {MachinnMwen.pwopriyete}")
    print(f"Koule:{MachinnMwen.koule}, Gaz: {MachinnMwen.gaz} lit, Model:{MachinnMwen.model}, pri: {MachinnMwen.pri}, Tente :{MachinnMwen.tente}")

while True:
    afficher_menu()

    choix = input("Chwazi (1-8): ")

    if choix == "1":
        MachinnMwen.akselere()
    elif choix == "2":
        MachinnMwen.frennen()
    elif choix == "3":
        MachinnMwen.VannMachinn()
    elif choix == "4":
        MachinnMwen.douko()
    elif choix == "5":
        kob = float(input("Rantre vale kob ou genyen : "))
        MachinnMwen.Achtegaz(kob)
    elif choix=="6":
        Dashbod()
    elif choix=="7":
        MachinnMwen.TenteMachinn()
    elif choix == "8":
        print("Mesi, orevwa")
        break
    else:
        print("ou mal chwazi tanpri chwazi ant 1 a 8.") 