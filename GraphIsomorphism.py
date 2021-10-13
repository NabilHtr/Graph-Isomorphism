import numpy as N


a = int(input("nombre de sommets de G1:  "))
matrice1 = []

b = int(input("nombre de sommet de G2:   "))
matrice2 = []

if a <= 0 or b <= 0 or a != b:
    print("erreur")

else:

    print("rempilissage de la matrice d'adjacence du graphe 1 :\n")
    for i in range(a):
        x = []

        for y in range(a):
            arc = int(input("arc entre x " + str(i + 1) + " et x " + str(y + 1)))
            x.append(arc)
        matrice1.append(x)
    print (N.array(matrice1))

    print("remplissage de la matrice d'adjacence du graphe 2 :\n")
    for s in range(b):
        x2 = []

        for d in range(b):
            arc2 = int(input("arc entre x " + str(s + 1) + " et x " + str(d + 1)))
            x2.append(arc2)
        matrice2.append(x2)
    print (N.array(matrice2))

    ii = []
    for i1 in range(a):
        c1 = []
        for j1 in range(a):
            if j1 == i1:
                c1.append(1)
            else:
                c1.append(0)

        ii.append(c1)

    print("Generation des matrices de permutaion:\n")
    print(N.array(ii))

    ss = 0
    boo = False
    test2=[]
    test3=[]
    while ss in range(a) and boo == False:
        test2 = N.dot(N.array(ii), N.array(ii).T)
        test3 = N.dot(N.array(test2), N.array(matrice2))
        if N.allclose(N.array(test3), N.array(matrice1)):
            print ("incroyable!!!!!")
            boo = True
        else:
            ss = ss + 1
            ii = N.random.permutation(N.array(ii))
            print (N.array(ii))

    print("\n\n")
    if boo == True:
        print("LES 2 GRAPHES SONT ISOMORPHES")
    else:
        print ("LES 2 GRAPHES NE SONT PAS ISOMORPHES")

#    test = []
#   for k in range(b):
#      test=N.random.permutation(N.array(matrice2))
#     test2=N.dot(test,N.array(ii).T)
#    if N.allclose(test2,matrice1):

#       print ("incroyable!!!!!")
#  else:
#     print ("PAS ISO!")
