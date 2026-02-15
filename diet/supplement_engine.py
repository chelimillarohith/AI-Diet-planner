def recommend_supplements(user):

    supplements = ["Creatine 3-5g", "Omega-3 1000mg"]

    if user.get("low_sunlight"):
        supplements.append("Vitamin D3 2000 IU")

    if user.get("deficiency"):
        supplements.append("Multivitamin")

    return supplements
