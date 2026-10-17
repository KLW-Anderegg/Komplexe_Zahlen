import matplotlib.pyplot as plt

## Parameter definieren ##
##############################
# Bild initialisieren
# Hier wird eine leere Heatmap erstellt, die spaeter mit den Iterationszahlen gefuellt wird.
breitePixel = 800
hoehePixel = 800
heatmap = []
for i in range(hoehePixel):
    heatmap.append([0] * breitePixel)  # Erstelle eine Zeile

# Abgebildeter Bereich der Zahlenebene definieren
x_min = -1.5
x_max = 1.5
y_min = -1.5 
y_max = 1.5

# Abstand der Gitterpunkte berechnen
dx = (x_max - x_min) / breitePixel
dy = (y_max - y_min) / hoehePixel

# Konstante c fuer die Julia-Menge festlegen
c = complex(-1, 0.3)
# Maximale Anzahl Iterationen festlegen
max_iter = 300
# Maximaler Betrag fuer die Abbruchbedingung
max_abs = 5




# Berechnung der Julia-Menge
##################################

#Heatmap berechnen
for i in range(hoehePixel):
    y = y_min + i * dy
    for j in range(breitePixel):
        x = x_min + j * dx
        z = complex(x, y)
        count = 0
        while abs(z) <= max_abs and count < max_iter:
            z = z**2 + c
            count += 1
        heatmap[i][j] = count

 
#Bild aus der Heatmap generieren
plt.imshow(heatmap, extent=(x_min, x_max, y_min, y_max), cmap="Spectral", origin='lower')
plt.xlabel("Re")
plt.ylabel("Im")
plt.title("Julia-Menge")
plt.colorbar(label="Anzahl Iterationen")
plt.show()
