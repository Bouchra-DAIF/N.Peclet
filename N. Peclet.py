print("N.Peclet")
Mv=input("Entrez la masse volumique : ")
Cp=input("Entrez la capacit√© thermique massique : ")
v=input("Entrez la vitesse: ")
Lambd=input("Entrez la conductivit√© thermique: ")
D=input("Entrez D : ")
try:
    Cp=float(Cp)
    v=float(v)
    Lambd=float(Lambd)
    Mv=float(Mv)
    Pe=(Mv*v*D*Cp)/Lambd
    print("Le nombre Nusselt", Pe)
except:
    print("erreur")