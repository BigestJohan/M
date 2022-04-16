import random


valeurATrouver = random.randint(0, 100)

nombreWhile = True

nombreRentreParUtilisateur = int(input("Quel est votre nombre ?"))

while valeurATrouver != nombreRentreParUtilisateur:
    
    if nombreWhile == False :
        nombreRentreParUtilisateur = int(input("Quel est votre nombre ?"))
    
    if nombreWhile:
        nombreWhile = False
    
    
    if nombreRentreParUtilisateur>valeurATrouver :
        print("Votre proposition est trop haute")
    elif nombreRentreParUtilisateur<valeurATrouver :
        print("Votre proposition est trop basse")


print("Félicitations")
        
      
        
        
    
                                     