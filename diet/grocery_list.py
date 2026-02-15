def create_grocery_list(meals):

    grocery = []

    for m in meals:
        grocery.append(m["food"])

    return grocery
