class ItemList():
    def __init__(self):
        self._base = []
        self._items = {}
        self.load()

    def load(self):
        with open("data/items.json") as infile:
            json_data = infile.read()
            game_data = json.loads(json_data)

            # Base items are stored as strings in an array
            for item in game_data["base"]:
                self._base.append(item)
            
            # Items that are crafted use the Item class
            for item_data in game_data["items"]:
                new_item = Item.fromJSON(item_data)
                self._items[new_item.name] = new_item

    def save(self):
        game_data = [game.toJSON() for game in self.games]
        data = {
            "base": self._base,
            "items": [item.toJSON() for item in self._items.values],
        }
        with open("data/data.json", "w") as outfile:
            outfile.write(json.dumps(data,indent=4))


class Item():
    def __init__(self):
        self.name = ""
        self.components = {}
        self.quantity = 0
    
    def fromJSON(data) -> Item:
        new_item = Item()
        new_item.name = data["name"]
        for component in data["components"]:
            components[component["name"]] = component["quantity"]
        new_item.name = data["quantity"]
        return new_item

    def toJSON(self):
        data = {
            "name": self.name,
            "components": list(),
            "quantity": self.quantity,
        }

        for key, value in self.components.items():
            comp_data = {
                "name": key,
                "quantity": value,
            }
            data["components"].add(comp_data)
        return data