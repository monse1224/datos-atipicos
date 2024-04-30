import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#print('hello outliers')

df= pd.read_csv('ventas_totales_sinnulos (1).csv', index_col=0)
#print(df.head())

valores_nulos=df.isnull().sum()
#print(valores_nulos)

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_corrientes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes con outliers')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
#plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corriente con outliers")
#plt.show()

y=df['ventas_precios_corrientes']
print(y)

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
print(percentile25)
print(percentile75)
iqr= percentile75 - percentile25
print(iqr)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
print("Limite superior permitido", Limite_Superior_iqr)
print("Limite inferior permitido", Limite_Inferior_iqr)

#Obtenemos datos limpios
data_clean_iqr= df[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
print(data_clean_iqr)

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["ventas_precios_corrientes"]) 
plt.title("Outliers de ventas_precios_corriente")
#plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["ventas_precios_corrientes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes sin outliers')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
#plt.show()

#Método con desviación estándar
data_clean_iqr["ventas_precios_corrientes"].to_csv('ventas_precios_corrientes.csv')

y=df["ventas_precios_corrientes"]
Limite_Superior_dev_std= y.mean() + 3*y.std()
Limite_Inferior_dev_std= y.mean() - 3*y.std()
print("Limite superior permitido usando desv estandar", Limite_Superior_dev_std)
print("Limite inferior permitido usando desv estandar", Limite_Inferior_dev_std)

#Obtenemos datos limpios
data_clean_dev_std= df[(y<=Limite_Superior_dev_std)&(y>=Limite_Inferior_dev_std)]
print(data_clean_dev_std)

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["ventas_precios_corrientes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_corrientes sin outliers- desv std')
plt.xlabel('ventas_precios_corrientes')
plt.ylabel('Frecuencia')
#plt.show()

#COLUMNA 2: VENTAS_PRECIOS_CONSTANTES
fig2 = plt.figure(figsize =(7, 3))
plt.hist(x=df["ventas_precios_constantes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_constantes con outliers')
plt.xlabel('ventas_precios_constantes')
plt.ylabel('Frecuencia')
#plt.show()

fig2 = plt.figure(figsize =(5, 3))
plt.boxplot(df["ventas_precios_constantes"]) 
plt.title("Outliers de ventas_precios_constantes con outliers")
#plt.show()

y2=df['ventas_precios_constantes']
print(y2)

percentile25=y2.quantile(0.25) #Q1
percentile75=y2.quantile(0.75) #Q3
print(percentile25)
print(percentile75)
iqr2= percentile75 - percentile25
print(iqr2)

Limite_Superior_iqr2= percentile75 + 1.5*iqr2
Limite_Inferior_iqr2= percentile25 - 1.5*iqr2
print("Limite superior permitido", Limite_Superior_iqr2)
print("Limite inferior permitido", Limite_Inferior_iqr2)

#Obtenemos datos limpios
data_clean_iqr2= df[(y2<=Limite_Superior_iqr2)&(y2>=Limite_Inferior_iqr2)]
print(data_clean_iqr2)

fig2 = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr2["ventas_precios_constantes"]) 
plt.title("Outliers de ventas_precios_constantes")
#plt.show()

fig2 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr2["ventas_precios_constantes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_constantes sin outliers')
plt.xlabel('ventas_precios_constantes')
plt.ylabel('Frecuencia')
#plt.show()

#Método con desviación estándar
data_clean_iqr2["ventas_precios_constantes"].to_csv('ventas_precios_constantes.csv')

y2=df["ventas_precios_constantes"]
Limite_Superior_dev_std2= y2.mean() + 3*y2.std()
Limite_Inferior_dev_std2= y2.mean() - 3*y2.std()
print("Limite superior permitido usando desv estandar", Limite_Superior_dev_std2)
print("Limite inferior permitido usando desv estandar", Limite_Inferior_dev_std2)

#Obtenemos datos limpios
data_clean_dev_std2= df[(y2<=Limite_Superior_dev_std2)&(y>=Limite_Inferior_dev_std2)]
print(data_clean_dev_std2)

fig2 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["ventas_precios_constantes"], color='red', rwidth=0.50)
plt.title('Histograma de ventas_precios_constantes sin outliers- desv std')
plt.xlabel('ventas_precios_constantes')
plt.ylabel('Frecuencia')
#plt.show()


#COLUMNA : salon_ventas
fig3 = plt.figure(figsize =(7, 3))
plt.hist(x=df["salon_ventas"], color='red', rwidth=0.50)
plt.title('Histograma de salon_ventas con outliers')
plt.xlabel('salon_ventas')
plt.ylabel('Frecuencia')
#plt.show()

fig3 = plt.figure(figsize =(5, 3))
plt.boxplot(df["salon_ventas"]) 
plt.title("Outliers de salon_ventas con outliers")
#plt.show()

y3=df['salon_ventas']
print(y3)

percentile25=y3.quantile(0.25) #Q1
percentile75=y3.quantile(0.75) #Q3
print(percentile25)
print(percentile75)
iqr3= percentile75 - percentile25
print(iqr3)

Limite_Superior_iqr3= percentile75 + 1.5*iqr3
Limite_Inferior_iqr3= percentile25 - 1.5*iqr3
print("Limite superior permitido", Limite_Superior_iqr3)
print("Limite inferior permitido", Limite_Inferior_iqr3)

#Obtenemos datos limpios
data_clean_iqr3= df[(y3<=Limite_Superior_iqr3)&(y3>=Limite_Inferior_iqr3)]
print(data_clean_iqr3)

fig3 = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr3["salon_ventas"]) 
plt.title("Outliers de salon_ventas")
#plt.show()

fig3 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr3["salon_ventas"], color='red', rwidth=0.50)
plt.title('Histograma de salon_ventas sin outliers')
plt.xlabel('salon_ventas')
plt.ylabel('Frecuencia')
#plt.show()

#Método con desviación estándar
data_clean_iqr3["salon_ventas"].to_csv('salon_ventas.csv')

y3=df["salon_ventas"]
Limite_Superior_dev_std3= y3.mean() + 3*y3.std()
Limite_Inferior_dev_std3= y3.mean() - 3*y3.std()
print("Limite superior permitido usando desv estandar", Limite_Superior_dev_std3)
print("Limite inferior permitido usando desv estandar", Limite_Inferior_dev_std3)

#Obtenemos datos limpios
data_clean_dev_std3= df[(y3<=Limite_Superior_dev_std3)&(y>=Limite_Inferior_dev_std3)]
print(data_clean_dev_std3)

fig3 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr3["salon_ventas"], color='red', rwidth=0.50)
plt.title('Histograma de salon_ventas sin outliers- desv std')
plt.xlabel('salon_ventas')
plt.ylabel('Frecuencia')
#plt.show()