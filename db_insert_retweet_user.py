import json
import MySQLdb

# with open("sample.txt", "r") as f:
with open("sample1.json", "r") as f:
    data = json.loads(f.read())

# print(data[0]['retweeted_status']['user'])

val_dict = {}

for i in range(len(data)):
    if data[i]['retweeted_status']:
        val_list = []
        key_list = list(data[i]['retweeted_status']['user'].keys())
        for key in key_list:
            val_list.append(data[i]['retweeted_status']['user'][key])
        val_dict[i] = tuple(val_list)
    else:
        continue

print(val_dict[0])


###gfofbosfnb