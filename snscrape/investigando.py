import pandas as pd

# palavra = input()

# dados = pd.read_csv("../../dados-tcc/word-"+palavra+".csv")

dados = pd.read_csv("./dados/com-rotulagem-d.csv")

# toxidade = dados["toxidade"]
# hate = dados["HateSpeech"]

# toxic_hate = 0
# is_hate_notToxic = 0

# for t in range(len(toxidade)):
#     if(toxidade[t] == 1):
#         if(hate[t] == "yes"):
#             toxic_hate += 1
#     else:
#         if(hate[t] == "yes"):
#             is_hate_notToxic += 1

# print("O número de tweets tóxicos e com discurso de ódio foi %i" % toxic_hate)
# print("O número de tweets com discurso de ódio e não tóxico foi %i" %
#       is_hate_notToxic)

# del dados["Unnamed: 0.2"]

# del dados["Unnamed: 0.1"]
# del dados["Unnamed: 0.1.1"]

# dados.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

# dados["rotulagem-manual"] = None

# dados.to_csv("./dados-finalizados.csv", index=False)

print(dados.columns)

rotulagem_d = dados["rotulage-description"]
rotulagem = dados["rotulagem"]

size = len(rotulagem)
print(size)
homofobico = 0

for i in range(size):
    if(rotulagem_d[i] > 0 and rotulagem[i] == "yes"):
        homofobico += 1

print(homofobico)

# dados = pd.read_csv("./dados/dados-finalizados.csv")

# palavras = ["baitola", "bichona", "bixa", "boiola", "gayzada",
#             "gayzismo", "homossexualismo", "viadagem", "viadao", "viadinho", "bicha"]

# tweets = dados["Texto"]
# print(len(tweets))

# duplicated = 0

# for t in tweets:
#     check_p = 0
#     for p in palavras:
#         if(p in t):
#             check_p += 1
#     if(check_p == 0):
#         duplicated += 1

# print(duplicated)
