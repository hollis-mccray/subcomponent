class ItemList():
    def __init__(self):
        self._item_items = {}
        self.load()

    def load(self):
        with open("data/items.json") as infile:
            json_data = infile.read()
            item_data = json.loads(json_data)
            for item_data in recipes["items"]:
                item = Item.fromJSON(item_data)
                self._item_list[item.name] = item

    def save(self):
        item_data = [recipe.toJSON() for (name, recipe) in self._recipe_list.items()]
        data = {
            "items": item_data
        }
        with open("data/items.json", "w") as outfile:
            outfile.write(json.dumps(data,indent=4))

class Item():
    def __init__(self):
        self.name = ""
        self.base = False
        self.recipes = []
    
    def fromJSON(data):
        new_item = Item()
        if "name" in data:
            new_item = data["name"]
        if "base" in data:
            new.base = data["base"]
        for recipe_data in data["recipes"]:
            recipe = Recipe.fromJSON(recipe_data)
            new_item.recipes.append(recipe)
        return new_item


    def toJSON(self):
        return self.name

class recipe():
    def __init__(self):
        self.inputs = {}
        self.made = []
        self.quantity = 0

    def fromJSON(recipe_data):
        new_recipe = Recipe()
        for (input, quantity) in recipe_data["inputs"]:
            new_recipe.inputs[input] = quantity
        for source in recipe_data["made"]:
            new_recipe.made.append(source)
        new_recipe.quantity = recipe_data["quantity"]
        return new_recipe