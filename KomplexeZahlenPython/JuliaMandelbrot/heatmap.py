import matplotlib.pyplot as plt # Bibliothek für die Darstellung von Grafiken

# Initialisierung des Bildes
# Das Bild ist eine Matrix mit 200x200 Pixeln
# und jeder Pixel hat einen Wert von 0
# Die Werte werden später durch die Berechnung ersetzt
heatmap = []
for i in range(200):
    heatmap.append([0] * 200)  # Erstelle eine Zeile mit 200 Nullen


for x in range(200):
    for y in range(200):
        heatmap[y][x] = 0.9999**((x-100)**2 + (y-100)**2)  # Beispielwert für den Pixel (x,y)

plt.imshow(heatmap)

plt.show()
