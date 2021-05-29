#Ejemplos de destinos turisticos.
import matplotlib.pyplot as plt
#creamos listas 
turistas = [86.9, 81.8, 75.9, 60.7, 58.2, 39.3, 37.7, 37.6, 37.5, 35.4]
paises = ['Francia', 'España', 'EEUU', 'China', 'Italia','México', 'Reino Unido', 'Turquía', 'Alemania', 'Tailandia']
explode = [0, 0.2, 0, 0, 0, 0.4, 0, 0, 0, 0]  # Destacar algunos

plt.pie(turistas, labels=paises,explode=explode,autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('TOP 10 DESTINOS TURÍSTICOS EN 2017')
plt.show()