
import tweepy as tw
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

deputados = [["@abou_anni", "@AcacioFavacho", "@AdolfoViana_", "@adrianasounovo", "@adrianodobaldy", "@AecioNeves", 
             "@AfonsoFlorence", "@DepAfonsoHamm", "@afonso_motta", "@depaguinaldo11", "@FaleiroAirton", "@Alan_Rick", 
             "@Alceu_Moreira", "@oficialalesilva", "@AlencarBraga13", "@alessandromolon", "@AlexManentePPS", 
             "@depalexsantana", "@alefrotabrasil", "@lexandreleite"], 
            ["@padilhando", "@AleSerfiotis", "@AlexisFonteyne", "@Alice_Portugal", "@alielmachado", 
             "@dep_alinegurgel", "@AlineSleutjes", "@Altineu", "@AluisioMendesMA", "@amaronetotv", 
             "@aferreira2020", "@andrepdt12", "@DepAndreFufuca", "@AndreJanonesAdv", "@DeputadaAngela", 
             "@AntonioBrito_", "@achinaglia", "@ArnaldoJardim", "@aroldomartins", "@ArthurLira_", "@DepArthurMaia"], 
             ["@assis_carvalho", "@deputadoatila", "@dep_acoutinho", "@aureacarolinax", "@AureoRibeiroRJ", 
             "@DeputadoBacelar", "@Baleia_Rossi", "@dasilvabenedita", "@benesleocadiorn", "@BetoFaroPT", 
             "@betopereirams", "@BetoRosado", "@Biakicis", "@bibonunes1", "@bilac_pinto", "@BiradoPindare", 
             "@BocaAbertaOf", "@BohnGass", "@BoscoCosta_SE", "@boscosaraiva"], ["@DepBrunaFurlan", "@CacaLeao", 
             "@CamiloPSB", "@capalbertoneto", "@capitao_augusto", "@fabioabreuofc", "@capitao_wagner", 
             "@CarlaZambelli17", "@CarlosBezerraJr", "@carloschiodini", "@Carlos_Gaguim", "@carlosgomesdep", 
             "@carlosjordy", "@carlossampaio_", "@carlosveraspt", "@CarlosZarattini", "@carmenzanotto", "@CarolDeToni", 
             "@Cassio_4011", "@celinaleao"], ["@CelioMouraTO", "@csilveira4599", "@CelioStudart", "@maldaner_celso", 
             "@celsorussomanno", "@depcelsosabino", "@Czmadureira", "@Charles_Federal", "@charllesevg", "@chico_dangelo", 
             "@BrazaoChiquinho", "@ToniettoChris", "@ChristianeYared", "@christinoaureo", "@dep_clarissa", 
             "@deputadocajado", "@CleberVerde10", "@dep_cel_armando", "@CoronelTadeu", "@CovattiFilho"], ["@dagobertopdt", 
             "@Drdamiaof", "@Daniel_PCdoB", "@DanielCoelho23", "@DFDanielFreitas", "@DanielPMERJ", "@TrzeciakDaniel", 
             "@DanielaWaguinho", "@danilo4010", "@depdarcidematos", "@davidmirandario"], 
             ["@davidbrsoares", "@DelegadoFurtado", "@EderMauroPA", "@DelegadoFreitas", "@DelegadoPablo_", "@delegado_waldir", 
             "@denisbezerra", "@diegogarciapr", "@depdimasfabiano", "@depmarcon", "@Domingos_Neto", "@DomingosSavioMG", 
             "@DrFredericoMG", "@jaziel_dr", "@DrLeonardomt", "@drluizovando", "@zachariascalil", "@DraManato", 
             "@dulcemiranda_to", "@EdilazioJunior_"], ["@ediolopes", "@EdmilsonPSOL", "@eduardobarbosa_", "@eduardobismarck", 
             "@BolsonaroSP", "@EduardoBraide", "@eduardocosta14", "@Eduardo_Cury", "@eduardodafonte", "@efraimfilho", 
             "@elcionepmdb", "@elidiasborges", "@Assessoria2577", "@EliasVazGyn", "@ElmarNascimento", "@emanuelzinhomt", 
             "@enioverri", "@enricomisasi", "@erikakokay", "@erosbiondini"], ["@EuclydesPetter", "@EvairdeMelo", 
             "@roman_evandro", "@fabiofaria5555", "@FabioHenriqueSE", "@depfmitidieri", "@_FabinhoRamalho", "@fabioreis1515", 
             "@deputadofabiosc", "@f_trad", "@Fausto_Pinato", "@FederalFelicio", "@felipecarreras", "@FFrancischini_", 
             "@rigoni_felipe", "@FelixMendoncaJr", "@fernandapsol", "@fernandofilhope", "@fernandogiacobo", "@fmonteiroPE"], 
             ["@depfernandor", "@filipebarrost", "@FlaviaArrudaDF", "@depflaviamorais", "@Flaviano_Melo", "@flavionoguera", 
             "@Flordelismk", "@franciscojr_go", "@FrancoCartafina", "@FredCosta5133", "@freianastaciopt", 
             "@GelsonAzevedoRJ", "@DepGenecias", "@GeneralGirao", "@GenPeternelli", "@geninhozuliani", "@geovaniadesa", 
             "@gervasiomaia", "@gilcutrim", "@gilbertoabramo"], ["@GilbertoPSC20", "@DGildenemyr", "@gilsonmarques30", 
             "@giovanicherini", "@GiovaniFeltes", "@Glauber_Braga", "@glaustinfokus", "@gleisi", "@greyceelias", 
             "@zeguilherme_10", "@GuilhermeMussi", "@GuilhermeMussi", "@GurgelSoares", "@gustavofruet", "@GustinhoRibeiro", 
             "@guth_reis", "@ze_haroldo", "@HeitorFreireCE", "@HeitorSchuch", "@heldersalomao"], ["@HelioCosta15", 
             "@h_leite", "@depheliolopes", "@HenriqueFontana", "@herciliodiniz", "@herculanopassos", "@HermesLaranja", 
             "@hildorocha1513", "@deputadohiran", "@depHugoLeal", "@HugoMottaPB", "@IdilvanAlencar", "@Igor_Kannario", 
             "@oficialigortimo", "@iracemaportela", "@bulhoesjr", "@IvanValente", "@jandira_feghali", "@jqcassol", 
             "@DepJefferson"], ["@jeronimogoergen", "@jesussergioac", "@JHC_40", "@DeputadoBacelar", "@joaocamposdep", 
             "@depjoaodanielpt", "@JoaoCampos", "@depjoaomaia", "@joaoromaneto", "@depjpassarinho", "@JoeniaWapichana", 
             "@jhonatan_djesus", "@joicehasselmann", "@Jorge_Braz", "@depjorgesolla", "@JoseAirtonPT", "@Schiavinato_", 
             "@guimaraes13PT", "@JoseMedeirosMT", "@depjosenelto"], ["@JoseNunesDep", "@priante", "@ZeRicardoAM", 
             "@dep_joserocha", "@josiasdavitoria", "@josiasgomesba", "@josimarPL22", "@LemosFederal", "@DepJulioCesarPI", 
             "@JulioCesarRib", "@depjuliodelgado", "@JuninhodoPneu", "@cabojunioamaral", "@bozzellajr", "@JuniorManoDep", 
             "@DepJuscelino", "@kimpkat", "@LaercioFederal", "@lafayetteandrad", "@laurietecantora"], ["@leandredaideal", 
             "@LedaSadala", "@Dep_LeoMoraes", "@leomotta_ofc", "@depleomonteiro", "@joseleonidas", "@LeurLomantoJr", 
             "@lidicedamata", "@lincoln_portela", "@LizianeBayer", "@LTrutis", "@LourivalGomesrj", "@lucasvgonzalez", 
             "@LucasRedecker", "@VergilioLucas77", "@Bivar1717", "@LucianoDucci", "@luciomosquini", "@LuisMirandaUSA1", 
             "@LuisTibeOficial"], ["@luisa_canziani", "@drluizantoniojr", "@lcm_motta", "@lcm_motta", "@professorLFG", 
             "@luizlaurofilho", "@Oficialluizlima", "@LuizNishimori", "@lpbragancabr", "@luizaerundina", "@luizaogoulart", 
             "@Luizianne13PT", "@Magdamofatto", "@majorfabianadep", "@PrManuelMarcos"], 
             ["@mararocha4545", "@marcelvanhattem", "@Marceloalvaroan", "@marceloaro", "@caleromarcelo", "@MarceloFreixo", 
              "@depmarcelonilo", "@marceloramosam", "@AlvinoMarcio", "@marciobiolchi", "@marciojerry", "@marciolabre", 
              "@dpmarciomarinho", "@MarcoBertaiolli", "@MarcosA_Sampaio", "@marcospereira04", "@MargaretCoelho", 
              "@JFMargarida", "@mariadorosario", "@mariarosassp"], 
             ["@DeputadaMariana", "@MariliaArraes", "@mario_heringer", "@depnegromontejr", "@deputado_marlon", 
              "@depmarrecafilho", "@marxbeltrao", "@mauricioptbrs", "@mauro_bfilho", "@depmaurolopes", "@drmauronazif", 
              "@MerlongSolano", "@Dmiguellombardi", "@MiltonVieiraOfc", "@Lael_Varella", "@DepFederalMoses", 
              "@natbonavides", "@nelsonbarbudo", "@nelsonpelegrino", "@nereucrispim"], ["@NeriGeller", "@newton1510", 
              "@neyleprevost", "@depnicoletti", "@DepNilsonPinto", "@NiltoTatto", "@NivaldoAlbuque", "@odaircunhamg", 
              "@OLIVALMARQUES", "@onyxlorenzoni", "@orlandosilva", "@OrDamaso", "@OsmarTerra", "@Ossesio_Silva", 
              "@OtoniDepFederal", "@ottoalencar", "@dep_padrejoao", "@AbilioSantana_", "@DEPPASTOREURICO", 
              "@marcofeliciano"], ["@prisidorio", "@Patrus_Ananias", "@paulambelmonte", "@paulaodopt", "@dep_paulinho", 
              "@pauloabiackel", "@PauloAzi", "@PauloBengtson", "@PauloMartins10", "@DeputadoFoletto", "@DF_PauloFreire", 
              "@pauloganime", "@deppauloguedes", "@DeputadoFederal", "@pauloramosdep", "@pauloteixeira13", 
              "@PedroABezerra", "@pedroocl", "@depPedroLucasF", "@Dep_PedroLupion"], ["@pedropaulo", "@uczai", 
              "@pedrowestphalen", "@perpetua_acre", "@pinheirinhomg", "@KatiaSastre", "@PompeodeMattos", "@deppimentel", 
              "@marcivania65", "@profalcids", "@ProfIsrael", "@professorjoziel", "@profdorinha", "@prof_rosaneide", 
              "@RafaelMottaRN", "@raimundocostaba", "@RaulHenry", "@ReginaldoLopes", "@rejane_dias", "@RenataAbreu1919", 
              "@renildo", "@RicardoBarrosPP", "@ricardozguidi"], ["@RicardoIzar", "@RicardoSilvaRP", "@PSDBricardo45", 
              "@RobertoAlvesPRB", "@robertodelucena", "@RobertoPessoaCE", "@rodrigoagost", "@coelho_rodrigo", 
              "@RodrigoCastro45", "@RodrigoMaia", "@RogerioCorreia_", "@deputadopeninha", "@ronaldocarletto", 
              "@DepRosanaValle", "@rosangelasgomes", "@rosemodestoms", "@23rubensbueno", "@rubenspereirajr", "@RubensOtoni", 
              "@rfalcao13"], ["@depruycarneiro", "@samiabomfim", "@samuelmoreira", "@DepSanderson", "@SandroAlex5555", 
              "@SargentoFAHUR", "@SebaOliveirajr", "@_sergiosouza", "@depsergiotoledo", "@vidigalsergio", 
              "@DepSheridan", "@sidneyleite_", "@silascamara_", "@silviacristinax", "@coelho_rodrigo", "@sorayasantos", 
              "@DepSostenes", "@depstefano", "@SubGonzagaMG", "@tabataamaralsp", "@TadeuAlencarPE", "@taliriapetrone", 
              "@TerezaCrisMS"], ["@TerezaNelma_", "@tiago_dimas", "@TiagoMitraud", "@tiriricanaweb", "@deputadotoninho", 
              "@tuliogadelha", "@ulduricojr", "@VaidonOliveira", "@ValdevanNoventa", "@DepValmir", "@Vandamilani1", 
              "@vanderloubet", "@vanderleimacris", "@vavamartinspa", "@TerezaNelma_", "@VICENTINHOPT", "@vicentinhojr", 
              "@Vilsondafetaemg", "@falecomvinicius", "@Vinicius_Farah"], ["@ViniciusPoit", "@MajorVitorHugo", 
              "@DepVitorLippi", "@depwagnermontes", "@waldenorpereira", "@walteralvesrn", "@pradoweliton", "@wr22", 
              "@WilsonSantiago_", "@WladGarotinho", "@WolneyQueirozM", "@Dep_ZeCarlosPT", "@ZeMarioGO", 
              "@depzeneto", "@ZeSilva_", "@zeca_dirceu"]]

for item in reversed(range(len(deputados))):

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
    user = deputados[item]
    tabela_mestre = []

    for x in range(len(user)):
        tweets = tw.Cursor(api.search, q="from:" + user[x], lang="pt", tweet_mode='extended').items(2)

        users_locs = [[tweet.user.screen_name, tweet.full_text, tweet.retweet_count, tweet.favorite_count,
                       str(tweet.created_at)[0:10], str(tweet.created_at)[11:19]] for tweet in tweets]
        tabela_mestre = tabela_mestre + users_locs

    # PRINT TESTE
    print(tabela_mestre)
    print("_______________________________________________")


    # CÓDIGO QUE ENTRA NA GOOGLESHEET

    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file',
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet1 = client.open('TT_dep_federais_DB').worksheet("DB")

    # CÓDIGO QUE INSERE DADOS NA GOOGLESHEET
    for x in range(len(tabela_mestre)):
        sheet1.insert_row(tabela_mestre[x], 2)

    # PEGANDO DADOS QUE ACABEI DE ADD
    sheetopen = client.open("TT_dep_federais_DB").sheet1
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
            multiplo += 12

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
    print("_______________________________________________")
    print("DADOS REPETIDOS APAGADOS")
    print("_______________________________________________FIM DE CÓDIGO NÚMERO {}".format([item]))

    time.sleep(100)
    
    
