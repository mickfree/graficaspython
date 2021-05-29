#Ejemplo de distribución de manzanas

#IMPORTAMOS "matplotlib".
import matplotlib.pyplot as plt

#DEFINIMOS ETIQUETAS  
manzanas = [20,10,25,30]
nombres = ["Ana","Juan","Diana","Catalina"]

#DIBUJAMOS GRÁFICA. 
plt.pie(manzanas, labels=nombres, autopct="%0.1f %%")

#MOSTRAMOS GRÁFICA.
plt.show()