import matplotlib.pyplot as plt

## Parameter definieren ##
##############################
# Bild initialisieren
# Hier wird eine leere Heatmap erstellt, die spaeter mit den Iterationszahlen gefuellt wird.
breitePixel = 1200
hoehePixel = 1200
heatmap = []
for i in range(hoehePixel):
    heatmap.append([0] * breitePixel)  # Erstelle eine Zeile

# Abgebildeter Bereich der Zahlenebene definieren
x_min = -0.751085
x_max = -0.734975
y_min = 0.118378
y_max = 0.134488

# Abstand der Gitterpunkte berechnen
dx = (x_max - x_min) / breitePixel
dy = (y_max - y_min) / hoehePixel

# Maximale Anzahl Iterationen festlegen
max_iter = 300
# Maximaler Betrag fuer die Abbruchbedingung
max_abs = 5




# Berechnung der Mandelbrot-Menge
##################################

#Heatmap berechnen
for i in range(hoehePixel):
    y = y_min + i * dy
    for j in range(breitePixel):
        x = x_min + j * dx
        c = complex(x, y)
        z = complex(0,0)  # Startwert z = 0
        count = 0
        while abs(z) <= max_abs and count < max_iter:
            z = z**2 + c
            count += 1
        heatmap[i][j] = count

 
#Bild aus der Heatmap generieren
plt.imshow(heatmap, extent=(x_min, x_max, y_min, y_max), cmap="Spectral", origin='lower')
plt.xlabel("Re")
plt.ylabel("Im")
plt.title("Mandelbrot-Menge")
plt.colorbar(label="Anzahl Iterationen")
plt.show()
