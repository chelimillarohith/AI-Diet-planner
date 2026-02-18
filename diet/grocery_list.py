def create_grocery_list(meals):

    grocery = []

    for m in meals:

        if "food" in m:
            grocery.append(m["food"])

        elif "foods" in m:
            grocery.append(m["foods"])

    return grocery
