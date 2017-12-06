import json

# -----------create file-------------------------- #
fileurl = "files\\user_settings.txt"
myfile = open(fileurl, mode="w", encoding="utf_8")

player1 = {
    "playrname": "Donald",
    "Score": 234,
    "awards":["OR","NY","NV"]
}

player2 = {
    'playrname': "Hillary",
    "Score": 257,
    "awards":["WT","TX","MI"]
}

mypayers = []
mypayers.append(player1)
mypayers.append(player2)

# ----------------save file to json--------------- #
json.dump(mypayers, myfile)
myfile.close()

# ----------------read json from file------------- #
myfile = open(fileurl, mode="r",encoding="utf_8")
jsondata = json.load(myfile)

for user in jsondata:
    print(str(user['playrname']))
