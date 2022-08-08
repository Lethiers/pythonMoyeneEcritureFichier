import os
if os.path.exists('moyenne.txt'):
    print('le fichiier existe')
else:
    chemin = "C:\\Users\\Utilisateur\\PycharmProjects\\test\\moyenne.txt"
    file = open(chemin,'a+')
    moyennes = [14.84, 14.14, 16.22, 86, 85, 85, 14.84, 13, 15.85, 9.99, 12.04, 15.03, 16.22, 12, 84, 10.20, 11.03,11.03]
    i = 0
    while i < len(moyennes):
        file.write(f'\t{moyennes[i]}')
        i=i+1
    file.close()
    print(f'le fichier viens d\'être créer avec le tableau suivant {moyennes} !!')

file = open('moyenne.txt','r')
listeBrut = file.read()
liste = listeBrut.split()


tablo=[]
i = 0
while i < len(liste):
    if float(liste[i])<=20:
        # test.remove(liste)
        tablo.append(float(liste[i]))
    i = i+1
liste = tablo
print(liste)

liste.sort()
print(liste[0:3])
liste.reverse()
print(liste[0:3])


