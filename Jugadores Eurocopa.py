#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfjugadores_euro24 = pd.read_csv('D:\Descargas\euro2024_players.csv')
dfjugadores_euro24.head(100)


# In[2]:


# Realiza la limpieza de datos del DataFrame.

# Eliminar filas duplicadas
dfjugadores_euro24.drop_duplicates(inplace=True)

# Manejo de valores nulos
dfjugadores_euro24.fillna(dfjugadores_euro24.mean(numeric_only=True), inplace=True)
dfjugadores_euro24.fillna("", inplace=True)  # Para columnas no numéricas


# In[3]:


# Realiza un análisis descriptivo del DataFrame.
print("Primeras 5 filas del DataFrame:")
print(dfjugadores_euro24.head(5))


# In[4]:


print("Descripción estadística del DataFrame:")
print(dfjugadores_euro24.describe())


# In[5]:


print("Información del DataFrame:")
print(dfjugadores_euro24.info())


# In[6]:


# Histograma de las edades de los jugadores
plt.figure(figsize=(10, 7))
sns.histplot(dfjugadores_euro24['Age'], bins=15, kde=True)
plt.title('Distribución de Edades de los Jugadores')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()


# In[7]:


# Mapa de calor de correlaciones
plt.figure(figsize=(12, 8))
sns.heatmap(dfjugadores_euro24.corr(), annot=True, cmap="coolwarm")
plt.title("Mapa de Calor de Correlaciones")
plt.show()


# In[8]:


# Boxplot de edades por posición
plt.figure(figsize=(14, 8))
sns.boxplot(x='Position', y='Age', data= dfjugadores_euro24)
plt.title('Distribución de Edades por Posición')
plt.xlabel('Posición')
plt.ylabel('Edad')
plt.xticks(rotation=45)
plt.show()


# In[9]:


# Boxplot de edades por posición
plt.figure(figsize=(25, 15))
sns.boxplot(x='Country', y='MarketValue', data= dfjugadores_euro24)
plt.title('Distribución de Mercado de Valor por Edades')
plt.xlabel('País')
plt.ylabel('Mercado de valor')
plt.xticks(rotation=45)
plt.show()


# In[10]:


# Gráfico de barras de los jugadores con mayor valor de mercado y su país de procedencia
top_players = dfjugadores_euro24.nlargest(25, 'MarketValue')[['Name', 'MarketValue', 'Country']]
plt.figure(figsize=(14, 8))
sns.barplot(x='MarketValue', y='Name', hue='Country', data=top_players, dodge=False)
plt.title('Jugadores con Mayor Valor de Mercado y su País de Procedencia')
plt.xlabel('Valor de Mercado (millones)')
plt.ylabel('Jugador')
plt.legend(title='País', bbox_to_anchor=(1, 1), loc='upper left')
plt.show()


# In[13]:


# Visualización del valor de mercado por país
country = input("Introduce el nombre del país para visualizar el valor de mercado de sus jugadores: ").lower()
dfjugadores_euro24['Country'] = dfjugadores_euro24['Country'].str.lower()
country_df = dfjugadores_euro24[dfjugadores_euro24['Country'] == country]

if country_df.empty:
    print(f"No se encontraron jugadores del país: {country}")
else:
    plt.figure(figsize=(14, 8))
    sns.barplot(x='Name', y='MarketValue', data=country_df, palette='viridis')
    plt.title(f'Valor de Mercado de los Jugadores de {country.capitalize()}')
    plt.xlabel('Jugador')
    plt.ylabel('Valor de Mercado')
    plt.xticks(rotation=90)
    plt.show()

