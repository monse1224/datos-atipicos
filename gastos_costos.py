import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df2= pd.read_excel('gastos_costos_20_23.xlsx', index_col=0)

valores_nulos=df2.isnull().sum()
#print(valores_nulos)

fig = plt.figure(figsize =(7, 3))
plt.hist(x=df2["IVA"], color='red', rwidth=0.50)
plt.title('Histograma de IVA con outliers')
plt.xlabel('IVA')
plt.ylabel('Frecuencia')
#plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df2["IVA"]) 
plt.title("Outliers de IVA con outliers")
#plt.show()

y=df2['IVA']
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
data_clean_iqr= df2[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
print(data_clean_iqr)

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["IVA"]) 
plt.title("Outliers de IVA")
#plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["IVA"], color='red', rwidth=0.50)
plt.title('Histograma de IVA sin outliers')
plt.xlabel('IVA')
plt.ylabel('Frecuencia')
#plt.show()

#Método con desviación estándar
data_clean_iqr["IVA"].to_csv('IVA.csv')

y=df2["IVA"]
Limite_Superior_dev_std= y.mean() + 3*y.std()
Limite_Inferior_dev_std= y.mean() - 3*y.std()
print("Limite superior permitido usando desv estandar", Limite_Superior_dev_std)
print("Limite inferior permitido usando desv estandar", Limite_Inferior_dev_std)

#Obtenemos datos limpios
data_clean_dev_std= df2[(y<=Limite_Superior_dev_std)&(y>=Limite_Inferior_dev_std)]
print(data_clean_dev_std)

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["IVA"], color='red', rwidth=0.50)
plt.title('Histograma de IVA sin outliers- desv std')
plt.xlabel('IVA')
plt.ylabel('Frecuencia')
#plt.show()

#COLUMNA 2: TOTAL MX
fig2 = plt.figure(figsize =(7, 3))
plt.hist(x=df2["TOTAL MX"], color='red', rwidth=0.50)
plt.title('Histograma de TOTAL MX con outliers')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()

fig2 = plt.figure(figsize =(5, 3))
plt.boxplot(df2["TOTAL MX"]) 
plt.title("Outliers de TOTAL MX con outliers")
#plt.show()

y2=df2['TOTAL MX']
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
data_clean_iqr2= df2[(y2<=Limite_Superior_iqr2)&(y2>=Limite_Inferior_iqr2)]
print(data_clean_iqr2)

fig2 = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr2["TOTAL MX"]) 
plt.title("Outliers de TOTAL MX")
#plt.show()

fig2 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr2["TOTAL MX"], color='red', rwidth=0.50)
plt.title('Histograma de TOTAL MX sin outliers')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()

#Método con desviación estándar
data_clean_iqr2["TOTAL MX"].to_csv('TOTAL MX.csv')

y2=df2["TOTAL MX"]
Limite_Superior_dev_std2= y2.mean() + 3*y2.std()
Limite_Inferior_dev_std2= y2.mean() - 3*y2.std()
print("Limite superior permitido usando desv estandar", Limite_Superior_dev_std2)
print("Limite inferior permitido usando desv estandar", Limite_Inferior_dev_std2)

#Obtenemos datos limpios
data_clean_dev_std2= df2[(y2<=Limite_Superior_dev_std2)&(y>=Limite_Inferior_dev_std2)]
print(data_clean_dev_std2)

fig2 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["TOTAL MX"], color='red', rwidth=0.50)
plt.title('Histograma de TOTAL MX sin outliers- desv std')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()


#COLUMNA : IMPORTE
fig3 = plt.figure(figsize =(7, 3))
plt.hist(x=df2["IMPORTE"], color='red', rwidth=0.50)
plt.title('Histograma de IMPORTE con outliers')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
#plt.show()

fig3 = plt.figure(figsize =(5, 3))
plt.boxplot(df2["IMPORTE"]) 
plt.title("Outliers de IMPORTE con outliers")
#plt.show()

y3=df2['IMPORTE']
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
data_clean_iqr3= df2[(y3<=Limite_Superior_iqr3)&(y3>=Limite_Inferior_iqr3)]
print(data_clean_iqr3)

fig3 = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr3["IMPORTE"]) 
plt.title("Outliers de IMPORTE")
#plt.show()

fig3 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr3["IMPORTE"], color='red', rwidth=0.50)
plt.title('Histograma de IMPORTE sin outliers')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
#plt.show()

#Método con desviación estándar
data_clean_iqr3["IMPORTE"].to_csv('IMPORTE.csv')

y3=df2["IMPORTE"]
Limite_Superior_dev_std3= y3.mean() + 3*y3.std()
Limite_Inferior_dev_std3= y3.mean() - 3*y3.std()
print("Limite superior permitido usando desv estandar", Limite_Superior_dev_std3)
print("Limite inferior permitido usando desv estandar", Limite_Inferior_dev_std3)

#Obtenemos datos limpios
data_clean_dev_std3= df2[(y3<=Limite_Superior_dev_std3)&(y>=Limite_Inferior_dev_std3)]
print(data_clean_dev_std3)

fig3 = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr3["IMPORTE"], color='red', rwidth=0.50)
plt.title('Histograma de IMPORTE sin outliers- desv std')
plt.xlabel('IMPORTE')
plt.ylabel('IMPORTE')
#plt.show()


