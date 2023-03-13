import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

client = pd.read_csv('csv/base_comptoir_espace_table_clients.csv',sep=';')
entreprise = pd.read_csv('csv/base_comptoir_espace_table_decisions_entreprises.csv',sep=';')
annee = 1
produit = 1
# choixClient = client[(client['CLI_CHOIX']>0)&(client['CLI_ANNEE']==annee)&(client['CLI_PROD']==produit)]["CLI_CHOIX"].value_counts()
# print(choixClient.index)

# plt.pie(choixClient,labels=choixClient.index,autopct='%1.0f%%',counterclock=False, startangle=110, colors=['blue','red','green','orange'])
# plt.title("Répartition des choix des clients")

#Chiffres d'affaires par entreprise et par année
annee = 1
choixClient1 = client[(client['CLI_CHOIX']>0)&(client['CLI_ANNEE']==annee)][["CLI_PROD","CLI_CHOIX"]].value_counts()
print(choixClient1)
annee = 2
choixClient2 = client[(client['CLI_CHOIX']>0)&(client['CLI_ANNEE']==annee)][["CLI_PROD","CLI_CHOIX"]].value_counts()
print(choixClient2)

#Chiffres d'affaires par entreprise et par année
