# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
labels='a','b','c','d'
sizes=5,6,7,8
colors='lightgreen','gold','lightskyblue','lightcoral'
explode=0,0,0,0
plt.pie(sizes,explode=explode,labels=labels,
        colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()