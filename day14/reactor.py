import math

high_bar = 10**12

class Ingredient():
    def __init__(self, ingredient):
        A, B = ingredient.strip().split()
        self.quantity = int(A)
        self.chemical = B
    
    def __hash__(self):
        return hash((self.chemical, self.quantity))
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return (self.chemical == other.chemical and self.quantity == other.quantity)
    
    def __str__(self):
        return "<" + str(self.quantity) + "," + self.chemical + ">" 

def get_reactions(input):
    reactions = {}
    for expression in input.split("\n"):
        rule, outcome = expression.split("=>")
        outcome = Ingredient(outcome)
        ingredients = []
        for ingredient in rule.split(","):
            ingredients.append(Ingredient(ingredient))
        if reactions.get(outcome.chemical, False):
            reactions[outcome.chemical].append((outcome, ingredients))
        else:
            reactions[outcome.chemical] = (outcome.quantity, ingredients)
    return reactions

def ensure(reactions, totals, chemical, quantity):
    if totals[chemical] >= quantity:
        return True
    if chemical == 'ORE':
        return False
    production_quantity, ingredients = reactions[chemical]
    need = math.ceil((quantity - totals[chemical]) / production_quantity)
    ensured = True
    for ingredient in ingredients:
        ensured = ensured and ensure(reactions, totals, ingredient.chemical, need * ingredient.quantity)
        totals[ingredient.chemical] -= need * ingredient.quantity
    if ensured:
        totals[chemical] += need * production_quantity
    return ensured

def ore_required(reactions):
    low, high = 0, high_bar
    while low < high:
        mid = low + (high - low) // 2
        totals = {element: 0 for element in reactions}
        totals['ORE'] = mid
        if ensure(reactions, totals, 'FUEL', 1):
            high = mid
        else:
            low = mid + 1
    return low

def max_fuel(reactions):
    low, high = 0, high_bar
    while low < high:
        mid = low + (high - low) // 2
        totals = {element: 0 for element in reactions}
        totals['ORE'] = high_bar
        if ensure(reactions, totals, 'FUEL', mid):
            low = mid
        else:
            high = mid - 1
    return high if ensure(reactions, totals, 'FUEL', high) else low

if __name__ == "__main__":
    input = open("input.txt").read()
    reactions = get_reactions(input)
    print("Part1:", ore_required(reactions))
    print("Part2:", max_fuel(reactions))