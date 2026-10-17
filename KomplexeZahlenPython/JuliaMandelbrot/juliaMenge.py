import matplotlib.pyplot as plt

def julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter):
    dx = (x_max - x_min) / width
    dy = (y_max - y_min) / height
    img = [[0 for _ in range(width)] for _ in range(height)]  # Initialisierung des Bildes
   

    for i in range(height):
        y = y_min + i * dy
        for j in range(width):
            x = x_min + j * dx
            z = complex(x, y)
            count = 0
            while abs(z) <= 2.0 and count < max_iter:
                z = z*z + c
                count += 1
            img[i][j] = count

    return img

def plot_julia(img, x_min, x_max, y_min, y_max):
    plt.figure(figsize=(8, 8))
    plt.imshow(img, extent=(x_min, x_max, y_min, y_max), cmap="inferno", origin='lower')
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.title("Julia-Menge")
    plt.colorbar(label="Anzahl Iterationen")
    plt.show()

# Parameter definieren
width, height = 800, 800
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5
c = complex(-0.7, 0.27015)  # Beispielwert für c
max_iter = 300

# Julia-Menge berechnen und darstellen
img = julia_set(width, height, x_min, x_max, y_min, y_max, c, max_iter)
plot_julia(img, x_min, x_max, y_min, y_max)
