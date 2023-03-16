import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

from nuages import *

client = pd.read_csv('csv/base_comptoir_espace_table_clients.csv',sep=';')
entreprise = pd.read_csv('csv/base_comptoir_espace_table_decisions_entreprises.csv',sep=';')
annee = 1
produit = 1
# choixClient = client[(client['CLI_CHOIX']>0)&(client['CLI_ANNEE']==annee)&(client['CLI_PROD']==produit)]["CLI_CHOIX"].value_counts()
# print(choixClient.index)

# plt.pie(choixClient,labels=choixClient.index,autopct='%1.0f%%',counterclock=False, startangle=110, colors=['blue','red','green','orange'])
# plt.title("Répartition des choix des clients")


ClientParEntreprise = client.groupby(["CLI_ANNEE","CLI_CHOIX"])

#Chiffres d'affaires par entreprise et par année
annee = 1
choixClient1 = client[(client['CLI_CHOIX']>0)&(client['CLI_ANNEE']==annee)][["CLI_CHOIX","CLI_PROD","CLI_ANNEE"]].value_counts()
prixProd1 = entreprise[(entreprise["ENT_ANNEE"]==annee)][["ENT_ID","ENT_PRIX","ENT_PROD","ENT_ANNEE"]]

# print(choixClient1)
annee = 2
choixClient2 = client[(client['CLI_CHOIX']>0)&(client['CLI_ANNEE']==annee)][["CLI_CHOIX","CLI_PROD","CLI_ANNEE"]].value_counts()
prixProd2 = entreprise[(entreprise["ENT_ANNEE"]==annee)][["ENT_ID","ENT_PRIX","ENT_PROD","ENT_ANNEE"]]
# print(choixClient2)

mergeEntreprise1 = pd.merge(choixClient1.rename('Choix1'),prixProd1,how= 'left' , left_on=["CLI_CHOIX","CLI_ANNEE","CLI_PROD"],right_on=["ENT_ID","ENT_ANNEE","ENT_PROD"])
# print(mergeEntreprise1)

mergeEntreprise2 = pd.merge(choixClient2.rename('Choix2'),prixProd2,how= 'left' , left_on=["CLI_CHOIX","CLI_ANNEE","CLI_PROD"],right_on=["ENT_ID","ENT_ANNEE","ENT_PROD"])

#Multiplication du nombre de choix par le prix du produit

mergeEntreprise1["CA1"] = mergeEntreprise1["Choix1"]*mergeEntreprise1["ENT_PRIX"]
mergeEntreprise2["CA2"] = mergeEntreprise2["Choix2"]*mergeEntreprise2["ENT_PRIX"]
# print(mergeEntreprise1)
# print(mergeEntreprise2)

#Additionner les chiffres d'affaires par entreprise
CA1 = mergeEntreprise1.groupby(["ENT_ID","ENT_ANNEE"])["CA1"].sum()
CA2 = mergeEntreprise2.groupby(["ENT_ID","ENT_ANNEE"])["CA2"].sum()
# print(CA1)
# print(CA2)

#Faire un graphique en barre des deux années
CA = pd.merge(CA1.rename('CA1'),CA2.rename('CA2'),how= 'left' , left_on=["ENT_ID"],right_on=["ENT_ID"])
# print(CA)
# ca = CA.plot(kind='bar', title ="Chiffre d'affaires par entreprise", figsize=(15, 10), legend=True, fontsize=12)
# ca.set_xlabel("Entreprise", fontsize=12)
# ca.set_ylabel("Chiffre d'affaires", fontsize=12)

# plt.show()
# print(prixProd1)

# cliProd1 = client[(client['CLI_CHOIX']>0)&(client['CLI_PROD']==1)]["CLI_PRIX"].value_counts()
# GraphBar = cliProd1.plot(kind='bar', title ="Chiffre d'affaires par entreprise", figsize=(15, 10), legend=True, fontsize=12)
# GraphBar.set_xlabel("Entreprise", fontsize=12)
# GraphBar.set_ylabel("Chiffre d'affaires", fontsize=12)
# plt.yticks(np.arange(0, 350, 50))
# plt.xticks(np.arange(0,17500,2500))
# plt.show()

# print(cliProd1)





nuage(1,2)



