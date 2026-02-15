import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_diet_response(user, macros):

    prompt = f"""
You are a professional Indian fitness nutritionist.

Generate a FULL DAY diet plan STRICTLY in this format:

■ Breakfast (time range)
Food Item – grams
Food Item – grams
Approx Macros: Protein X g | Carbs X g | Fats X g | Calories X kcal

■ Lunch (time range)
Food Item – grams
Food Item – grams
Approx Macros: Protein X g | Carbs X g | Fats X g | Calories X kcal

■ Evening Snack (time range)
Food Item – grams
Approx Macros: Protein X g | Carbs X g | Fats X g | Calories X kcal

■ Dinner (time range)
Food Item – grams
Approx Macros: Protein X g | Carbs X g | Fats X g | Calories X kcal

Rules:
- Use Indian foods
- Mention exact quantities in grams
- Show macros for EACH meal
- Budget friendly according to user
- Include veg/nonveg options if applicable
- NO extra explanation outside this structure

User Details:
Goal: {user['goal']}
Weight: {user['weight']} kg
Height: {user['height']} cm
Age: {user['age']}
Gender: {user['gender']}
Activity Level: {user['activity_level']}
Body Type: {user['body_type']}
Weight Tendency: {user['weight_tendency']}
Diet Type: {user['diet_type']}
Health Issues: {user['health_issues']}
Budget: {user['budget']}
Meals Per Day: {user['meals_per_day']}
Cooking Style: {user['cooking_style']}

Target Macros:
Protein {macros['protein_g']} g
Carbs {macros['carbs_g']} g
Fat {macros['fat_g']} g
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Error: {e}"


def generate_meal_plan(user, macros):

    ai_plan = ai_diet_response(user, macros)

    return [
        {"meal": "AI Diet Plan", "food": ai_plan}
    ]
