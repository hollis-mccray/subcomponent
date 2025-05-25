class ItemList():
    def __init__(self):
        self._base = []
        self._recipes = {}
        self.load()

    def load(self):
        with open("data/items.json") as infile:
            json_data = infile.read()
            game_data = json.loads(json_data)

    def save(self):
        pass


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