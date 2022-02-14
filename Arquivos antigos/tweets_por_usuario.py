import os
import tweepy as tw
import pandas as pd
import gspread_dataframe as gd
import re
import schedule
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# KEYS PARA CONSEGUIR OS DADOS DO TWITTER
consumer_key = 'D7CowpO9FOwoigwClR8k2MN9E'
consumer_secret = 'Oc866wtthIiOUV1iksTK7n14mEeKHUgwavJzCKP8gTMyQBKFr1'
access_token = '1542145388-xodgfVEv8WrOHNAKYtpmPUghD0nDvy5G6HTBi7P'
access_token_secret = 'w9ljBnC99rES8lT2xT50r6VIhAKl9940NkAe2Md0V3lbj'
# AUTENTICAÇÃO TWITTER
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# CÓDIGO QUE ENTRAR NO TWITTER
date_since = "2019-01-01"
user = ["@GabrielaPrioli", "@lauraabcarvalho", "@bollemdb", "@cirogomes", "@AdrillesRJorge", "@MarceloAdnet0",
        "@Ticostacruz",
        "@gcassianosp", "@VillaMarcovilla", "@Rconstantino", "@felipeneto", "@eduardomoreira", "@RachelSherazade",
        "@_makavelijones", "@opropriolavo", "@pedrodoria"]
tabela_mestre = []

for x in range(len(user)):
    tweets = tw.Cursor(api.search, q="from:" + user[x], lang="pt", tweet_mode='extended').items(1)

    users_locs = [[tweet.user.screen_name, tweet.full_text, tweet.retweet_count, tweet.favorite_count,
                   str(tweet.created_at)[0:10], str(tweet.created_at)[11:19]] for tweet in tweets]
    tabela_mestre = tabela_mestre + users_locs

# PRINT TESTE
# print(tabela_mestre)

tabela_resposta = []
tabela_RT = []
tabela_tt = []

# CÓDIGO QUE SEPARA E CLASSIFICA OS DADOS
for x in range(len(tabela_mestre)):
    if tabela_mestre[x][1][0] == "@":
        tabela_resposta.append(tabela_mestre[x])
    elif tabela_mestre[x][1][0] == "R" and tabela_mestre[x][1][1] == "T":
        tabela_RT.append(tabela_mestre[x])
    else:
        tabela_tt.append(tabela_mestre[x])

tabela_resposta = [x + ['Resposta'] for x in tabela_resposta]
tabela_RT = [x + ['Retweet'] for x in tabela_RT]
tabela_tt = [x + ['Tweet'] for x in tabela_tt]

# PRINT TESTE
# print("_______________________________________________")
# print("resposta",tabela_resposta)
# print("RT",tabela_RT)
# print("tt",tabela_tt)


# CÓDIGO QUE ENTRA NA GOOGLESHEET


scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file',
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet1 = client.open('Python').worksheet("Página1")

# CÓDIGO QUE INSERE DADOS NA GOOGLESHEET
for x in range(len(tabela_resposta)):
    sheet1.insert_row(tabela_resposta[x], 2)
for x in range(len(tabela_RT)):
    sheet1.insert_row(tabela_RT[x], 2)
for x in range(len(tabela_tt)):
    sheet1.insert_row(tabela_tt[x], 2)

# PEGANDO DADOS QUE ACABEI DE ADD
sheetopen = client.open("Python").sheet1
list_of_hashes = sheetopen.get_all_records()

# FAZENDO UMA LISTA COM APENAS USUARIO E TEXTO
lista = []
for x in list_of_hashes:
    [lista.extend([k, v]) for k, v in x.items()]

words = []
multiplo = 3
for x in range(len(lista)):
    if str(x) == str(multiplo):
        words.append([lista[x - 2], lista[x].split()])
        multiplo += 14

# APAGANDO DADOS REPETIDOS
repeated = []
repeated2 = []
for x in range(len(words)):
    for y in range(len(words)):
        if words[x] == words[y]:
            repeated.append(y)
            break
for x in range(len(words)):
    for y in range(len(words)):
        if words[x] == words[y]:
            repeated2.append(y)
delete = list(list(set(repeated2) - set(repeated)) + list(set(repeated) - set(repeated2)))

delete2 = []
for x in range(len(delete)):
    delete2.append(delete[x] + 2)

for x in reversed(range(len(delete2))):
    sheet1.delete_row(delete2[x])
