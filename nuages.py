import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

client = pd.read_csv('csv/base_comptoir_espace_table_clients.csv',sep=';')
entreprise = pd.read_csv('csv/base_comptoir_espace_table_decisions_entreprises.csv',sep=';')

def nuage(annee=1,produit=1):

    yEnt1 = client[(client['CLI_ANNEE']==annee)&(client['CLI_PROD']==produit)]["CLI_CONFORT"]
    xEnt1 = client[(client['CLI_ANNEE']==annee)&(client['CLI_PROD']==produit)]["CLI_PRIX"]

    res_reg=linregress(xEnt1,yEnt1)
    a=res_reg.slope
    b=res_reg.intercept
    coef_cor=res_reg.rvalue

    x = np.arange(0, 30000, 1)
    y = a*x+b

    textline = 'Confort = '+str(round(a,2))+'*Prix + '+str(round(b,2))
    plt.plot(x,y, color='red')
    plt.text(15000, 2500, textline, bbox=dict(facecolor='red'), fontsize=12)

    Entreprises1 = entreprise[(entreprise["ENT_ANNEE"]==annee)&(entreprise["ENT_PROD"]==produit)][["ENT_ID","ENT_PRIX","ENT_CONF"]]

    plt.plot(Entreprises1[(Entreprises1['ENT_ID']==1)]["ENT_PRIX"],Entreprises1[(Entreprises1['ENT_ID']==1)]["ENT_CONF"],'o', color='lime')
    plt.plot(Entreprises1[(Entreprises1['ENT_ID']==2)]["ENT_PRIX"],Entreprises1[(Entreprises1['ENT_ID']==2)]["ENT_CONF"],'o', color='orange')
    plt.plot(Entreprises1[(Entreprises1['ENT_ID']==3)]["ENT_PRIX"],Entreprises1[(Entreprises1['ENT_ID']==3)]["ENT_CONF"],'o', color='cyan')
    plt.plot(Entreprises1[(Entreprises1['ENT_ID']==4)]["ENT_PRIX"],Entreprises1[(Entreprises1['ENT_ID']==4)]["ENT_CONF"],'o', color='magenta')
    if produit==2:
        plt.plot(Entreprises1[(Entreprises1['ENT_ID']==5)]["ENT_PRIX"],Entreprises1[(Entreprises1['ENT_ID']==5)]["ENT_CONF"],'o', color='green')
        plt.text(Entreprises1[(Entreprises1['ENT_ID']==5)]["ENT_PRIX"],Entreprises1[(Entreprises1['ENT_ID']==5)]["ENT_CONF"],'Ent 5', fontsize=8, bbox=dict(facecolor='white', alpha= 0.5))

    plt.text(Entreprises1[(Entreprises1['ENT_ID']==1)]["ENT_PRIX"],Entreprises1[(Entreprises1['ENT_ID']==1)]["ENT_CONF"],'Ent 1', fontsize=8, bbox=dict(facecolor='white', alpha= 0.5))
    plt.text(Entreprises1[(Entreprises1['ENT_ID']==2)]["ENT_PRIX"],Entreprises1[(Entreprises1['ENT_ID']==2)]["ENT_CONF"],'Ent 2', fontsize=8, bbox=dict(facecolor='white', alpha= 0.5))
    plt.text(Entreprises1[(Entreprises1['ENT_ID']==3)]["ENT_PRIX"],Entreprises1[(Entreprises1['ENT_ID']==3)]["ENT_CONF"],'Ent 3', fontsize=8, bbox=dict(facecolor='white', alpha= 0.5))
    plt.text(Entreprises1[(Entreprises1['ENT_ID']==4)]["ENT_PRIX"],Entreprises1[(Entreprises1['ENT_ID']==4)]["ENT_CONF"],'Ent 4', fontsize=8, bbox=dict(facecolor='white', alpha= 0.5))

    plt.scatter(xEnt1,yEnt1)
    plt.title("Corrélation entre le confort et le prix pour les entreprises et les clients")
    plt.xticks(np.arange(0, 30000, 5000))
    plt.yticks(np.arange(0, 4000, 500))
    plt.show()