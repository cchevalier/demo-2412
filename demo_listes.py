def tri_selection(L):
    liste_triee = []
    while len(L) > 0:
        carte_min = min(L)
        liste_triee.append(carte_min)
        L.remove(carte_min)
    return liste_triee


promo = ['Théo', 'Philippe', 'Lamia', 'Marvin', 
         'Maëlle', 'Yoann', 'Jonathan', 'Corentin', 
         'Joris', 'Matthias', 'Alicia', 'Izak', 
         'Mayel', 'Corentin', 'Jordan', 'Abire' 
]
print(promo)


promo_triee = tri_selection(promo)

count = 0
for p in promo_triee:
    count += 1
    print(count, p)