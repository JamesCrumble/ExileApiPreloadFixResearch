# location_content = {"location_content": [
#     "Gwennen [Items gambler]",
#     "Farric Lynx Alpha [Add Suffix, Remove Prefix]",  # -
#     "Harvest",
#     "Einhar, Beastmaster",
#     "Eternal Chest",
#     "Vaal Chest",
#     "Fenumal Plagued Arachnid [Split an Item in Two]",  # -
#     "Fenumal Queen [Unique Staff][Redeemer Mod]"
# ]}


# # InsectSpawner
# fen_queen = [
#     'beast'
#     '.act',
#     'minion',
#     '.ao',
#     'minion2',
#     'boss.ao'
# ]


# # SpiderPlagued...
# fen_arach = [
#     'minion2',
#     'boss.ao',
#     'clone.act',
#     'close',
#     'beast',
#     'minion',
#     '.act'
# ]

# # Farric Pit Hound
# location_content = {"location_content": [
#     "Farric Wolf Alpha [Add Prefix, Remove Suffix]", # -
#     "Einhar, Beastmaster",
#     "Craicic Chimeral [Imprint of a Magic Item]", # -
#     "Farric Pit Hound [Level 21 Corrupted Gem]" #
# ]}

import os
import orjson

ROOT_PATH: str = os.path.dirname(os.path.abspath(__file__))
loaded_data: list[str] = orjson.loads(open(os.path.join(
    ROOT_PATH, 'all_row_content.json'
), 'r').read())['data']

# values: set[str] = set()

grouped: dict = dict()

# for value in loaded_data:
#     if len(value.split('/')) == 1:
#         print(value)
#     values.add(len(value.split('/')))


def falldown(dict_: dict, keys: list[str]) -> list:
    if len(keys) < 1:
        return dict_

    key = keys.pop(0)

    if keys and key not in dict_:
        dict_[key] = dict()
    elif not keys and key not in dict_:
        dict_[key] = list()
        return dict_[key]
    elif type(dict_.get(key)) is list:
        return dict_

    return falldown(dict_[key], keys)


for value in loaded_data:
    categories = value.split('/')
    if len(categories) == 1:
        continue

    place = falldown(grouped, categories[:-1])
    if type(place) is dict:
        if 'values' not in place:
            place['values'] = list()
        place['values'].append(categories[-1])
    else:
        place.append(categories[-1])

# print(grouped.keys())

# DATA IN LOCATION CONTENT
# "location_content": [
#     "Einhar, Beastmaster",
#     "Farric Goliath [Unique Bow][Crusader Mod]",
#     "Essence of Woe",
#     "Tormented Poisoner",
#     "Fenumal Plagued Arachnid [Split an Item in Two]", # -
#     "Farric Wolf Alpha [Add Prefix, Remove Suffix]", # -
#     "Crafting Recipe",
#     "Essence of Suffering",
#     "Essence of Anger",
#     "Craicic Sand Spitter [Orb of Fusing][Orbs of Binding]"
#   ]

# FOUNDED 2 RED -  Farric Goliath [Unique Bow][Crusader Mod] and Craicic Sand Spitter [Orb of Fusing][Orbs of Binding]

with open('groped_content.json', 'a+') as handle:
    handle.write(orjson.dumps(grouped).decode())
