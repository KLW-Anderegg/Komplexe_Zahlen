import matplotlib.pyplot as plt # Bibliothek fuer die Darstellung von Grafiken

# Initialisierung des Bildes
# Hier wird ein 5x5 Bild mit Werten von 1 bis 9 erstellt
# Die Werte sind in einer Liste von Listen organisiert,
# wobei jede innere Liste eine Zeile des Bildes darstellt
# Die Werte in den Listen sind so angeordnet, dass sie eine Art Farbverlauf erzeugen
bild = [[1, 2, 3, 4, 5],  [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]


plt.imshow(bild) #Die Funktion imshow erstellt eine Heatmap aus den Werten in der Liste bild.
plt.show() # Die Funktion show zeigt das Bild an.
