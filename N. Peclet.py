print("N.Peclet")
Mv=input("Entrez la masse volumique : ")
Cp=input("Entrez la capacité thermique massique : ")
v=input("Entrez la vitesse: ")
Lambd=input("Entrez la conductivité thermique: ")
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