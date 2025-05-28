import json

class ItemList():
    def __init__(self):
        self._items = {}
        self.load()

    def load(self):
        with open("data/data.json") as infile:
            json_data = infile.read()
            game_data = json.loads(json_data)
            
            # Items are defined using the Item Class
            for item_data in game_data["items"]:
                new_item = Item.fromJSON(item_data)
                self._items[new_item.name] = new_item

    def save(self):
        data = {
            "items": [item.toJSON() for item in self._items.values],
        }
        with open("data/data.json", "w") as outfile:
            outfile.write(json.dumps(data,indent=4))
    
    def addItem(self, newItem):
        self._items[newItem.name] = newItem
        self.save()
    
    def getItem(self, itemName):
        if itemName in self._items.keys():
            return self._items[itemName]
        else:
            return None



class Item():
    def __init__(self):
        self.name = ""
        self.base = False
        self.components = {}

        #Arbitrary default value
        self.quantity = 1
    
    def fromJSON(data):
        new_item = Item()
        new_item.name = data["name"]
        if "base" in data:
            new_item.base= data["base"]
        if "components" in data:
            for component in data["components"]:
                new_item.components[component["name"]] = component["quantity"]
        if "quantity" in data:
            new_item.quantity = data["quantity"]
            
        return new_item

    def toJSON(self):
        data = {
            "name": self.name,
            "base": self.base,
            "components": list(),
            "quantity": self.quantity,
        }

        if not self.base:
            for key, value in self.components.items():
                comp_data = {
                    "name": key,
                    "quantity": value,
                }
                data["components"].add(comp_data)
        else:
            data["base"] = True
        return data