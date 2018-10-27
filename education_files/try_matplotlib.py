from __future__ import print_function

import pandas as pd
pd.__version__
import matplotlib as mp
mp.__version__
import matplotlib.pyplot as plt

dataset = pd.read_csv("../datafiles/data-science-blog-python-beispiel.txt", sep="|", header=0, encoding="utf8")
 
var= dataset.groupby(['Funktion']).sum().stack()
temp = var.unstack()
type(temp)
x_list = temp['Mitarbeiter']
label_list = temp.index
plt.axis("equal") # Kreisdiagramm rund gestaltet (sonst Standard: oval!)
plt.pie(x_list, labels=label_list, autopct="%1.1f%%")
plt.title('Aufteilung alle Mitarbeiter auf die Standorte nach Funktion')
plt.show()

