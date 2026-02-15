def calculate_calories(user):

    weight = user["weight"]
    height = user["height"]
    age = user["age"]
    gender = user["gender"]
    activity = user["activity_level"]
    goal = user["goal"]

    if gender.lower() == "male":
        bmr = 10*weight + 6.25*height - 5*age + 5
    else:
        bmr = 10*weight + 6.25*height - 5*age - 161

    activity_map = {
        "sedentary":1.2,
        "light":1.375,
        "moderate":1.55,
        "active":1.725
    }

    maintenance = bmr * activity_map[activity]

    if goal == "fat_loss":
        maintenance -= 400
    elif goal == "muscle_gain":
        maintenance += 300
    elif goal == "performance":
        maintenance += 150

    return round(maintenance)
