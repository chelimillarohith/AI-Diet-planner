def calculate_macros(user, calories):

    weight = user["weight"]

    protein = weight * 2
    fat_calories = calories * 0.25
    fat = fat_calories / 9

    remaining = calories - (protein*4 + fat*9)
    carbs = remaining / 4

    return {
        "protein_g": round(protein),
        "carbs_g": round(carbs),
        "fat_g": round(fat),
        "fiber_g": 30
    }
