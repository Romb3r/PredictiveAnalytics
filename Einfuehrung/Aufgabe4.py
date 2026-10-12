import matplotlib.pyplot as plt

# Daten
x_achse = [1, 2, 3, 4, 5]
y1 = [1, 3, 2, 5, 4]
y2 = [2, 2, 3, 3, 5]
y3 = [5, 4, 3, 2, 1]

# Figure erstellen
plt.figure(figsize=(8, 5))

# 3 Linien mit eigener Farbe zeichnen
plt.plot(x_achse, y1, color="red", label="Linie 1")
plt.plot(x_achse, y2, color="blue", label="Linie 2")
plt.plot(x_achse, y3, color="green", label="Linie 3")

# Beschriftung der Achsen und Titel
plt.xlabel("X-Achse")
plt.ylabel("Y-Achsle")
plt.title("Linienplot mit 3 Werte-Linien")

# Legende anzeigen (nutzt label)
plt.legend()

# Als PDF speichern
plt.savefig("Einfuehrung/Aufgabe4_data/plot.pdf", format="pdf")
plt.close()