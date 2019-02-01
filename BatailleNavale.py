"""
Bataille navale version simplifiée
Par Kamel El Mazroui et Marasa Enzo
"""


from random import randint

def initialiser_grille():
    #fonction qui permet de créer la grille de l'adversaire
    grille=[]
    for a in range(10):
        ligne=[]
        for a in range(10):
            ligne.append(-1)
        grille.append(ligne)
    return grille

def placer_bateaux(grille):
    #fonction qui permet de placer les bateaux aléatoirement sur la grille de l'adversaire
    porteavion=False
    croiseur=False
    contretorpilleur=False
    sousmarin=False
    torpilleur=False
    while not porteavion:
        x=randint(0,9)     #permet d'obtenir aléatoirement la coordonnée x du premier point du bateau (ligne)
        y=randint(0,9)     #permet d'obtenir aléatoirement la coordonnée y du premier point du bateau (colonnes)
        sens=randint(1,2)  #permet de choisir un sens, 1 pour vertical, 2 pour horizontale
        if sens==1 and x<=5:
            if x!=0:
                grille[x-1][y]=9
            if x+5<=9:
                grille[x+5][y]=9
            for a in range(5):
                grille[x+a][y]=1
                if y!=0:
                    grille[x+a][y-1]=9
                if y!=9:
                    grille[x+a][y+1]=9
            porteavion=True
        elif sens==2 and y<=5:
            if y!=0:
                grille[x][y-1]=9
            if y+5<=9:
                grille[x][y+5]=9
            for a in range(5):
                grille[x][y+a]=1
                if x!=0:
                    grille[x-1][y+a]=9
                if x!=9:
                    grille[x+1][y+a]=9
            porteavion=True
    while not croiseur:
        x=randint(0,9)
        y=randint(0,9)
        sens=randint(1,2)
        if sens==1 and x<=6 and grille[x][y]==-1 and grille[x+1][y]==-1 and grille[x+2][y]==-1 and grille[x+3][y]==-1:
            if x!=0:
                grille[x-1][y]=9
            if x+4<=9:
                grille[x+4][y]=9
            for a in range(4):
                grille[x+a][y]=2
                if y!=0:
                    grille[x+a][y-1]=9
                if y!=9:
                    grille[x+a][y+1]=9
            croiseur=True
        if sens==2 and y<=6 and grille[x][y]==-1 and grille[x][y+1]==-1 and grille[x][y+2]==-1 and grille[x][y+3]==-1:
            if y!=0:
                grille[x][y-1]=9
            if y+4<=9:
                grille[x][y+4]=9
            for a in range(4):
                grille[x][y+a]=2
                if x!=0:
                    grille[x-1][y+a]=9
                if x!=9:
                    grille[x+1][y+a]=9
            croiseur=True
    while not contretorpilleur:
            x=randint(0,9)
            y=randint(0,9)
            sens=randint(1,2)
            if sens==1 and x<=7 and grille[x][y]==-1 and grille[x+1][y]==-1 and grille[x+2][y]==-1:
                if x!=0:
                    grille[x-1][y]=9
                if x+3<=9:
                    grille[x+3][y]=9
                for a in range(3):
                    grille[x+a][y]=3
                    if y!=0:
                        grille[x+a][y-1]=9
                    if y!=9:
                        grille[x+a][y+1]=9
                contretorpilleur=True
            if sens==2 and y<=7 and grille[x][y]==-1 and grille[x][y+1]==-1 and grille[x][y+2]==-1:
                if y!=0:
                    grille[x][y-1]=9
                if y+3<=9:
                    grille[x][y+3]=9
                for a in range(3):
                    grille[x][y+a]=3
                    if x!=0:
                        grille[x-1][y+a]=9
                    if x!=9:
                        grille[x+1][y+a]=9
                contretorpilleur=True
    while not sousmarin:
            x=randint(0,9)
            y=randint(0,9)
            sens=randint(1,2)
            if sens==1 and x<=7 and grille[x][y]==-1 and grille[x+1][y]==-1 and grille[x+2][y]==-1:
                if x!=0:
                    grille[x-1][y]=9
                if x+3<=9:
                    grille[x+3][y]=9
                for a in range(3):
                    grille[x+a][y]=4
                    if y!=0:
                        grille[x+a][y-1]=9
                    if y!=9:
                        grille[x+a][y+1]=9
                sousmarin=True
            if sens==2 and y<=7 and grille[x][y]==-1 and grille[x][y+1]==-1 and grille[x][y+2]==-1:
                if y!=0:
                    grille[x][y-1]=9
                if y+3<=9:
                    grille[x][y+3]=9
                for a in range(3):
                    grille[x][y+a]=4
                    if x!=0:
                        grille[x-1][y+a]=9
                    if x!=9:
                        grille[x+1][y+a]=9
                sousmarin=True
    while not torpilleur:
            x=randint(0,9)
            y=randint(0,9)
            sens=randint(1,2)
            if sens==1 and x<=8 and grille[x][y]==-1 and grille[x+1][y]==-1:
                if x!=0:
                    grille[x-1][y]=9
                if x+2<=9:
                    grille[x+2][y]=9
                for a in range(2):
                    grille[x+a][y]=5
                    if y!=0:
                        grille[x+a][y-1]=9
                    if y!=9:
                        grille[x+a][y+1]=9
                torpilleur=True
            if sens==2 and y<=8 and grille[x][y]==-1 and grille[x][y+1]==-1:
                if y!=0:
                    grille[x][y-1]=9
                if y+2<=9:
                    grille[x][y+2]=9
                for a in range(2):
                    grille[x][y+a]=5
                    if x!=0:
                        grille[x-1][y+a]=9
                    if x!=9:
                        grille[x+1][y+a]=9
                torpilleur=True
    for a in range(10):
        for b in range(10):
            if grille[a][b]==9:
                grille[a][b]=-1

def tir_valide(tirs,ligne,colonne):
    # fonction qui permet de savoir si un tir est valide ou non 
    if ligne<="J" and colonne<10 and ligne>="A" and colonne>=0:   #condition qui vérifie si le tir est dans la grille ou non 
        if tirs[(ord(ligne)-65)][colonne]==-1:
            return True
        else:
            return False
    else:
        return False

def prochain_coup(tirs):
    # fonction qui permet de lancer le prochain coup ou non 
    ligne="Z"     
    colonne=11   

#gràce aux initialisations précédentes le test juste en dessous n'est pas valide donc on rentre dans la boucle
#donc le programme demande au joueur de rentrer ses coordonnées pour son tir

    while not tir_valide(tirs,ligne,colonne):    
        ligne=input("Entrez une ligne (lettre entre A et J) :")
        colonne=int(input("Entrez une colonne (chiffre entre 1 et 10) :"))
        colonne-=1   # colonne - 1 car dans une liste on part de 0 et comme l'utilisateur lui rentre un chiffre entre 1 et 10 il faut soustraire 1 à son chiffre
    return [ligne,colonne]

"""
ord() permet de transformer un caractère en décimale grâce à la table ASCII 
"""

def resultat_tir(bateaux,ligne,colonne):
    if bateaux[ord(ligne)-65][colonne]==-1:
        print("Loupé !")
        return 0
    elif bateaux[ord(ligne)-65][colonne]==1:
        if compte_bateau(bateaux,1)==1:  # condition qui vérifie si le bateau est la ou le tir est éffectué
            return 2
        else:
            return 1
    elif bateaux[ord(ligne)-65][colonne]==2:
        if compte_bateau(bateaux,2)==1:
            return 2
        else:
            return 1
    elif bateaux[ord(ligne)-65][colonne]==3:
        if compte_bateau(bateaux,3)==1:
            return 2
        else:
            return 1
    elif bateaux[ord(ligne)-65][colonne]==4:
        if compte_bateau(bateaux,4)==1:
            return 2
        else:
            return 1
    else:
        if compte_bateau(bateaux,5)==1:
            return 2
        else:
            return 1

def compte_bateau(bateaux,num):
    nb=0
    for a in range(10):
        for b in range(10):
            if bateaux[a][b]==num:
                nb+=1
    return nb

def tirer(bateaux,tirs,ligne,colonne):
    if resultat_tir(bateaux,ligne,colonne)==0:
        tirs[ord(ligne)-65][colonne]=0  #ord car si l'utilisateur entre A en ligne celui ci vaut grâce à ord(A), dans la table ASCII : 65, donc 65-65 = 0 ca crée donc le bon indice 
    elif resultat_tir(bateaux,ligne,colonne)==1:
        print("Touché !")
        if bateaux[ord(ligne)-65][colonne]==1:
            tirs[ord(ligne)-65][colonne]="T1"
        if bateaux[ord(ligne)-65][colonne]==2:
            tirs[ord(ligne)-65][colonne]="T2"
        if bateaux[ord(ligne)-65][colonne]==3:
            tirs[ord(ligne)-65][colonne]="T3"
        if bateaux[ord(ligne)-65][colonne]==4:
            tirs[ord(ligne)-65][colonne]="T4"
        if bateaux[ord(ligne)-65][colonne]==5:
            tirs[ord(ligne)-65][colonne]="T5"
        bateaux[ord(ligne)-65][colonne]=0
    else:
        print("Bateau coulé !")
        if bateaux[ord(ligne)-65][colonne]==1:
            tirs[ord(ligne)-65][colonne]="T1"
            for a in range(10):
                for b in range(10):
                    if tirs[a][b]=="T1":
                        tirs[a][b]=2
        if bateaux[ord(ligne)-65][colonne]==2:
            tirs[ord(ligne)-65][colonne]="T2"
            for a in range(10):
                for b in range(10):
                    if tirs[a][b]=="T2":
                        tirs[a][b]=2
        if bateaux[ord(ligne)-65][colonne]==3:
            tirs[ord(ligne)-65][colonne]="T3"
            for a in range(10):
                for b in range(10):
                    if tirs[a][b]=="T3":
                        tirs[a][b]=2
        if bateaux[ord(ligne)-65][colonne]==4:
            tirs[ord(ligne)-65][colonne]="T4"
            for a in range(10):
                for b in range(10):
                    if tirs[a][b]=="T4":
                        tirs[a][b]=2
        if bateaux[ord(ligne)-65][colonne]==5:
            tirs[ord(ligne)-65][colonne]="T5"
            for a in range(10):
                for b in range(10):
                    if tirs[a][b]=="T5":
                        tirs[a][b]=2
        bateaux[ord(ligne)-65][colonne]=0

def partie_finie(tirs):
    nbcases=0
    for a in range(10):
        for b in range(10):
            if tirs[a][b]==2:
                nbcases+=1
    return nbcases==17 # nombre de cases qu'occupent toute la flotte 

def affiche_grille(tirs):
    lettres=["A","B","C","D","E","F","G","H","I","J"]
    p=0
    print("  1 2 3 4 5 6 7 8 9 10")
    for a in tirs:
        print(lettres[p],end=" ")
        for b in a:
            if b==-1:
                print('.',end=" ")
            elif b==0:
                print('*',end=" ")
            elif b==2:
                print("X",end=" ")
            else:
                print("+",end=" ")
        print()
        p+=1

def jouer():
    bateaux_adverse=initialiser_grille()
    placer_bateaux(bateaux_adverse)
    tirs_joueur=initialiser_grille()
    print("Mes tirs :")
    affiche_grille(tirs_joueur)
    print("\n\n")
    while not partie_finie(tirs_joueur):
        coup=prochain_coup(tirs_joueur)
        print("Tir aux coordonnées :",coup[0],coup[1]+1)
        tirer(bateaux_adverse,tirs_joueur,coup[0],coup[1])
        affiche_grille(tirs_joueur)
        print("\n")
    if partie_finie(tirs_joueur):
        print("Félicitations ! Vous avez coulé la flotte ennemie et vous gagnez la partie !")

jouer()