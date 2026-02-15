import os
from groq import Groq

# ---------------- GROQ CLIENT ----------------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------- AI DIET RESPONSE ----------------
def ai_diet_response(user, macros):

    prompt = f"""
You are a professional Indian fitness nutritionist.

Create a PERSONALIZED FULL DAY DIET PLAN.

Use these EXACT targets:
Calories Target: {user['calories']} kcal
Protein Target: {macros['protein_g']} g
Carbs Target: {macros['carbs_g']} g
Fat Target: {macros['fat_g']} g

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

STRICT FORMAT RULES (VERY IMPORTANT):
- Create EXACTLY {user['meals_per_day']} meals.
- Use this structure for EACH meal:

■ Meal Name (time range)
Food Item – grams
Food Item – grams
Approx Macros: Protein X g | Carbs X g | Fats X g | Calories X kcal

- Leave ONE blank line between meals.
- Do NOT add explanations outside this format.

Additional Rules:
- Indian foods only
- Budget friendly
- Respect veg/nonveg preference
- Include hydration suggestion at the end
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Error: {e}"


# ---------------- MAIN FUNCTION ----------------
def generate_meal_plan(user, macros):

    ai_plan = ai_diet_response(user, macros)

    return [
        {"meal": "AI Diet Plan", "food": ai_plan}
    ]
