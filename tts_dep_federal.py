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
user = ["@AbilioSantana_", "@AcacioFavacho", "@AdolfoViana_", "@adrianasounovo", "@adrianodobaldy",
        "@AecioNeves", "@AfonsoFlorence", "@DepAfonsoHamm", "@afonso_motta", "@depaguinaldo11",
        "@FaleiroAirton", "@Alan_Rick", "@Alceu_Moreira", "@oficialalesilva", "@AlencarBraga13",
        "@alessandromolon", "@AlexManentePPS", "@depalexsantana", "@alefrotabrasil",
        "@lexandreleite", "@padilhando", "@AleSerfiotis", "@AlexisFonteyne",
        "@Alice_Portugal", "@alielmachado", "@dep_alinegurgel", "@AlineSleutjes",
        "@AluisioMendesMA", "@amaronetotv", "@andrepdt12", "@DepAndreFufuca", "@AndreJanonesAdv",
        "@DeputadaAngela", "@achinaglia", "@ArnaldoJardim", "@aroldomartins", "@ArthurLira_",
        "@DepArthurMaia", "@assis_carvalho", "@deputadoatila", "@dep_acoutinho", "@aureacarolinax",
        "@AureoRibeiroRJ", "@DeputadoBacelar", "@Baleia_Rossi", "@dasilvabenedita",
        "@benesleocadiorn", "@BetoFaroPT", "@betopereirams", "@BetoRosado", "@BiaCavassa",
        "@Biakicis", "@bibonunes1", "@bilac_pinto", "@BiradoPindare", "@BocaAbertaOf",
        "@BohnGass", "@BoscoCosta_SE", "@boscosaraiva", "@DepBrunaFurlan", "@CacaLeao",
        "@CamiloPSB", "@capalbertoneto", "@capitao_augusto", "@capitao_wagner", "@CarlaZambelli17",
        "@carloschiodini", "@Carlos_Gaguim", "@carlosgomesdep", "@carlosjordy", "@carlossampaio_",
        "@carlosveraspt", "@CarlosZarattini", "@carmenzanotto", "@CarolDeToni", "@Cassio_4011",
        "@celinaleao", "@CelioMouraTO", "@csilveira4599", "@CelioStudart", "@maldaner_celso",
        "@celsorussomanno", "@depcelsosabino", "@Czmadureira", "@Charles_Federal", "@charllesevg",
        "@chico_dangelo", "@BrazaoChiquinho", "@ToniettoChris", "@ChristianeYared", "@christinoaureo",
        "@dep_clarissa", "@deputadocajado", "@CleberVerde10", "@dep_cel_armando", "@CoronelTadeu",
        "@josiasdavitoria", "@dagobertopdt", "@Drdamiaof", "@Daniel_PCdoB", "@DanielCoelho23", "@DFDanielFreitas",
        "@DanielPMERJ", "@TrzeciakDaniel", "@DanielaWaguinho", "@danilo4010", "@depdarcidematos",
        "@davidmirandario", "@davidbrsoares", "@DelegadoFurtado", "@EderMauroPA", "@DelegadoFreitas",
        "@DelegadoPablo_", "@delegado_waldir", "@denisbezerra", "@diegogarciapr", "@depdimasfabiano",
        "@Domingos_Neto", "@DomingosSavioMG", "@DrFredericoMG", "@DrLeonardomt", "@SinvalMalheiros",
        "@DraManato", "@dulcemiranda_to", "@EdilazioJunior_", "@ediolopes", "@EdmilsonPSOL",
        "@eduardobarbosa_", "@eduardobismarck", "@BolsonaroSP", "@EduardoBraide", "@eduardocosta14",
        "@Eduardo_Cury", "@eduardodafonte", "@efraimfilho", "@elcionepmdb", "@elidiasborges", "@EliasVazGyn",
        "@ElmarNascimento", "@emanuelzinhomt", "@DepEneiasReis", "@enioverri", "@enricomisasi", "@erikakokay",
        "@erosbiondini", "@EuclydesPetter", "@EvairdeMelo", "@roman_evandro", "@fabiofaria5555",
        "@FabioHenriqueSE", "@depfmitidieri", "@_FabinhoRamalho", "@fabioreis1515", "@f_trad", "@Fausto_Pinato",
        "@felipecarreras", "@FFrancischini_", "@rigoni_felipe", "@FelixMendoncaJr", "@fernandapsol",
        "@FBCFilho", "@fmonteiroPE", "@filipebarrost", "@FlaviaArrudaDF", "@depflaviamorais",
        "@Flaviano_Melo", "@flavionoguera", "@Flordelismk", "@franciscojr_go", "@FrancoCartafina",
        "@FredCosta5133", "@freianastaciopt", "@gastaodvieira", "@DepGenecias", "@GeneralGirao",
        "@GenPeternelli", "@geninhozuliani", "@geovaniadesa", "@gervasiomaia", "@fernandogiacobo",
        "@gilcutrim", "@gilbertoabramo", "@GilbertoPSC20", "@DGildenemyr", "@gilsonmarques30",
        "@giovanicherini", "@GiovaniFeltes", "@Glauber_Braga", "@glaustinfokus", "@gleisi",
        "@zeguilherme_10", "@GuilhermeMussi", "@GuilhermeMussi", "@GurgelSoares", "@gustavofruet",
        "@GustinhoRibeiro", "@guth_reis", "@HeitorFreireCE", "@HeitorSchuch", "@heldersalomao",
        "@h_leite", "@depheliolopes", "@HenriqueFontana", "@herculanopassos", "@HermesLaranja",
        "@hildorocha1513", "@deputadohiran", "@depHugoLeal", "@HugoMottaPB", "@IdilvanAlencar",
        "@Igor_Kannario", "@oficialigortimo", "@iracemaportela", "@bulhoesjr", "@IvanValente",
        "@jandira_feghali", "@jqcassol", "@DepJefferson", "@jeronimogoergen", "@JHC_40", "@jhonatan_djesus",
        "@joaocamposdep", "@depjoaodanielpt", "@JoaoCampos", "@depjoaomaia", "@joaoromaneto",
        "@depjpassarinho", "@JoeniaWapichana", "@joicehasselmann", "@Jorge_Braz", "@depjorgesolla",
        "@JoseAirtonPT", "@guimaraes13PT", "@SchreinerJose", "@JoseMedeirosMT", "@depjosenelto",
        "@JoseNunesDep", "@priante", "@ZeRicardoAM", "@LemosFederal", "@DepJulioCesarPI", "@JulioCesarRib",
        "@depjuliodelgado", "@JuninhodoPneu", "@cabojunioamaral", "@juniorbozzella", "@JuniorManoDep",
        "@DepJuscelino", "@kimpkat", "@LaercioFederal", "@lafayetteandrad", "@laurietecantora",
        "@leandredaideal", "@LedaSadala", "@Dep_LeoMoraes", "@leomotta_ofc", "@depleomonteiro",
        "@joseleonidas", "@LeurLomantoJr", "@lidicedamata", "@lincoln_portela", "@LizianeBayer",
        "@LTrutis", "@LourivalGomesrj", "@lucasvgonzalez", "@LucasRedecker", "@VergilioLucas77",
        "@Bivar1717", "@LucianoDucci", "@luciomosquini", "@LuisMirandaUSA1", "@LuisTibeOficial",
        "@luisa_canziani", "@drluizantoniojr", "@lcm_motta", "@lcm_motta", "@luizlaurofilho",
        "@Oficialluizlima", "@LuizNishimori", "@lpbragancabr", "@luizaerundina", "@luizaogoulart",
        "@Luizianne13PT", "@Magdamofatto", "@majorfabianadep", "@mararocha4545", "@marcelvanhattem",
        "@marceloaro", "@caleromarcelo", "@MarceloFreixo", "@depmarcelonilo", "@marceloramosam",
        "@AlvinoMarcio", "@marciobiolchi", "@marciojerry", "@marciolabre", "@dpmarciomarinho",
        "@MarcoBertaiolli", "@depmarcon", "@MarcosA_Sampaio", "@marcospereira04", "@MargaretCoelho",
        "@JFMargarida", "@mariadorosario", "@mariarosassp", "@DeputadaMariana", "@MariliaArraes",
        "@mario_heringer", "@depnegromontejr", "@deputado_marlon", "@depmarrecafilho", "@marxbeltrao",
        "@mauricioptbrs", "@mauro_bfilho", "@depmaurolopes", "@drmauronazif", "@Dmiguellombardi",
        "@MiltonVieiraOfc", "@DepFederalMoses", "@natbonavides", "@nelsonbarbudo", "@nereucrispim",
        "@NeriGeller", "@newton1510", "@depnicoletti", "@DepNilsonPinto", "@NiltoTatto",
        "@NivaldoAlbuque", "@odaircunhamg", "@OLIVALMARQUES", "@orlandosilva", "@OrDamaso",
        "@OsmarTerra", "@Ossesio_Silva", "@OtoniDepFederal", "@ottoalencar", "@dep_padrejoao",
        "@depPaesLandim", "@DEPPASTOREURICO", "@prisidorio", "@PatriciaLFerraz", "@Patrus_Ananias",
        "@paulambelmonte", "@paulaodopt", "@pauloabiackel", "@PauloAzi", "@PauloBengtson",
        "@PauloMartins10", "@DF_PauloFreire", "@pauloganime", "@deppauloguedes", "@dep_paulinho",
        "@DeputadoFederal", "@pauloramosdep", "@pauloteixeira13", "@PedroAugusto_CE", "@pedroocl",
        "@depPedroLucasF", "@Dep_PedroLupion", "@pedropaulo", "@uczai", "@pedrowestphalen",
        "@perpetua_acre", "@pinheirinhomg", "@KatiaSastre", "@PompeodeMattos", "@marcofeliciano",
        "@ProfIsrael", "@professorjoziel", "@deppimentel", "@profdorinha", "@marcivania65",
        "@prof_rosaneide", "@RafaelMottaRN", "@RaulHenry", "@ReginaldoLopes", "@StephanesJr",
        "@rejane_dias", "@renildo", "@RicardoBarrosPP", "@ricardozguidi", "@RicardoIzar",
        "@PSDBricardo45", "@RobertoAlvesPRB", "@robertodelucena", "@RobertoPessoaCE",
        "@rodrigoagost", "@coelho_rodrigo", "@RodrigoCastro45", "@RodrigoMaia", "@RogerioCorreia_",
        "@deputadopeninha", "@ronaldocarletto", "@DepRosanaValle", "@rosangelasgomes",
        "@rosemodestoms", "@23rubensbueno", "@RubensOtoni", "@rfalcao13", "@depruycarneiro",
        "@samiabomfim", "@samuelmoreira", "@DepSanderson", "@dep_santini", "@SargentoFAHUR",
        "@Schiavinato_", "@SebaOliveirajr", "@_sergiosouza", "@depsergiotoledo", "@vidigalsergio",
        "@DepSheridan", "@sidneyleite_", "@silascamara_", "@Silvio_CFilho", "@sorayasantos",
        "@DepSostenes", "@depstefano", "@SubGonzagaMG", "@tabataamaralsp", "@taliriapetrone",
        "@tedcontioficial", "@TerezaNelma_", "@tiago_dimas", "@TiagoMitraud", "@tiriricanaweb",
        "@deputadotoninho", "@tuliogadelha", "@VaidonOliveira", "@ValdevanNoventa", "@DepValmir",
        "@vanderloubet", "@vanderleimacris", "@vavamartinspa", "@TerezaNelma_", "@VICENTINHOPT",
        "@vicentinhojr", "@falecomvinicius", "@Vinicius_Farah", "@ViniciusPoit", "@MajorVitorHugo",
        "@DepVitorLippi", "@waldenorpereira", "@walteralvesrn", "@pradoweliton", "@WilsonSantiago_",
        "@WladGarotinho", "@WolneyQueirozM", "@Dep_ZeCarlosPT", "@ZeMarioGO", "@depzeneto", "@ZeSilva_", "@zeca_dirceu"]
tabela_mestre = []

for x in range(len(user)):
    tweets = tw.Cursor(api.search, q="from:" + user[x], lang="pt", tweet_mode='extended').items(2)

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
sheetopen = client.open("TT_dep_federais").sheet1
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
