from save_json import writeAJson
from database import Database

db = Database(database="dex", collection="pokemons")
db.reset_database()
pokemons = db.collection.find()


# for pokemon in pokemons:
# print(pokemon)

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})


bulbasaur = getPokemonByDex(1)
writeAJson(bulbasaur, "bulbasaur")


pokemon = db.collection.find({"type": "Grass", "base.Attack": { "$lte": 50 }})
writeAJson(pokemon, "pokemon_grass")


def get_4_letters_or_less(collection):
  names = collection.find({}, {"name": 1})
  four_letters_or_less = []
  for name in names:
    if len(name["name"].keys()) <= 4:
      if all(len(word) <= 4 for word in name["name"].values()):
        four_letters_or_less.append(name["name"].values())
  return four_letters_or_less

writeAJson(get_4_letters_or_less(db.collection), "pokemon_4_words_or_less")