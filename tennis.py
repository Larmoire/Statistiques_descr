import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

joueurs = pd.read_csv('csv/data_tennis/data_players.csv',sep=',')
tournois = pd.read_csv('csv/data_tennis/tournaments.csv',sep=',')
scores = pd.read_csv('csv/data_tennis/match_scores.csv',sep=',') 
stats = pd.read_csv('csv/data_tennis/match_stats.csv',sep=',')
dfrank1= pd.read_csv('csv/data_tennis/rankings.csv',sep=',')
dfrank2= pd.read_csv('csv/data_tennis/rankings_2.csv',sep=',')
dfrank3= pd.read_csv('csv/data_tennis/rankings_3.csv',sep=',')
classement = pd.concat([dfrank1,dfrank2,dfrank3])

def tennis(param):
    
    anneedenaissance = 1960
    joueurheight = joueurs[(joueurs['height_cm']>6.5)&(joueurs['birth_year']>=anneedenaissance)]['height_cm']

    if param == 'a' or param == 'b':
        print(joueurheight)
        print("Nombre de joueurs : ",joueurheight.count())
        print("Moyenne de taille des joueurs : ",joueurheight.mean())
        print("Médiane de taille des joueurs : ",joueurheight.median())
        print("Ecart type de taille des joueurs : ",joueurheight.std())
    if param == 'c':
        hist = joueurheight.plot(kind='hist', title ="Histogramme de la taille des joueurs", figsize=(15, 10), fontsize=12, bins=np.arange(joueurheight.min(),joueurheight.max(),5),edgecolor="black")
        plt.title("Distribution des tailles des joueurs nés à partir de "+str(anneedenaissance))
        plt.show()

def player(id):
    player = classement[classement['player_id']==id]
    player['week_title'] = pd.to_datetime(player['week_title'], format='%Y.%m.%d')
    player = player.sort_values(by='week_title')
    #Inverser l'axe y
    title = "Evolution du classement de "+joueurs[joueurs['player_id']==id]['first_name'].values[0]+" "+joueurs[joueurs['player_id']==id]['last_name'].values[0]
    evolution = player.plot(x='week_title',y='rank_number',title=title,figsize=(15, 10), fontsize=12,legend=False)
    plt.gca().invert_yaxis()
    evolution.set_xlabel("", fontsize=12)
    evolution.set_ylabel("Classement", fontsize=12)
    plt.show()

def nuagetennis():
    joueurheight = joueurs[(joueurs['height_cm']>6.5)][['player_id','height_cm']]
    ServReussis = stats[(stats['winner_first_serve_points_won']<=stats['winner_first_serves_in'])&(stats['loser_first_serve_points_won']<=stats['loser_first_serves_in'])&(stats['winner_first_serves_in']>0)&(stats['loser_first_serves_in']>0)][['match_id','winner_first_serve_points_won','loser_first_serve_points_won','winner_first_serves_in','loser_first_serves_in']]
    winners = scores.merge(ServReussis, on='match_id', how='inner')
    losers = scores.merge(ServReussis, on='match_id', how='inner')
    winners = winners.merge(joueurheight, left_on='winner_player_id', right_on='player_id', how='inner')
    losers = losers.merge(joueurheight, left_on='loser_player_id', right_on='player_id', how='inner')
    winnerheight = winners[['player_id','height_cm','winner_first_serve_points_won','winner_first_serves_in']]
    loserheight = losers[['player_id','height_cm','loser_first_serve_points_won','loser_first_serves_in']]
    general = pd.concat([winnerheight,loserheight])
    general = general.groupby('player_id').mean()
    general['first_serve_points_won'] = (general['winner_first_serve_points_won']+general['loser_first_serve_points_won'])/(general['winner_first_serves_in']+general['loser_first_serves_in'])
    #Enlever les NaN
    general = general.dropna()
    print(general)
    plt.scatter(general['height_cm'],general['first_serve_points_won'],s=1)
    plt.title("Nuage de points des joueurs en fonction de leur taille et du nombre de points gagnés sur leur premier service")
    plt.xlabel("Taille en cm")
    plt.ylabel("Nombre de points gagnés sur le premier service")
    plt.show()