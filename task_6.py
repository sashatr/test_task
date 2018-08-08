recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}


def count(recipe, available):
    check = list(set(recipe) - set(available))
    if len(check) is not 0:
        return "Not enough ingredients!"
    else:
        result = []
        for i in [i for i in recipe]:
            result.append(available[i] // recipe[i])

        return  min(result)

print('Result:', count(recipe, available))