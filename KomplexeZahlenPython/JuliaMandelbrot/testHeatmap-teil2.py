import matplotlib.pyplot as plt # Bibliothek fuer die Darstellung von Grafiken
#Bild erzeugen
bild = [[1, 2, 3, 4, 5],  [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]

plt.imshow(bild,extent=(0, 10, -20, 20)) 
plt.show() 

