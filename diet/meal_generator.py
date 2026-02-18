import os
from groq import Groq

# ---------------- GROQ CLIENT ----------------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ---------------- AI DIET RESPONSE ----------------
def ai_diet_response(user, macros):

    prompt = f"""
You are a professional Indian fitness nutritionist.

Create a PERSONALIZED FULL DAY DIET PLAN.

-----------------------------
TARGET DAILY NUTRITION (STRICT)
-----------------------------
Calories Target: {user['calories']} kcal
Protein Target: {macros['protein_g']} g
Carbs Target: {macros['carbs_g']} g
Fat Target: {macros['fat_g']} g
Fiber Target: {macros['fiber_g']} g

User Meals Per Day: {user['meals_per_day']}
Diet Type: {user['diet_type']}
Goal: {user['goal']}

-----------------------------
VERY IMPORTANT RULES
-----------------------------
- Total calories from ALL meals MUST be very close to the Calories Target.
- Total protein, carbs, fat and fiber across meals MUST match the targets.
- You MUST calculate meal macros mathematically.
- Distribute macros evenly across meals.

Meal naming rules:
- If meals_per_day = 3 → Breakfast, Lunch, Dinner
- If meals_per_day = 4 → Breakfast, Snack, Lunch, Dinner
- If meals_per_day = 5 → Breakfast, Snack, Lunch, Snack, Dinner

-----------------------------
MEAL STRUCTURE (STRICT FORMAT)
-----------------------------
Generate EXACTLY {user['meals_per_day']} meals.

Each meal MUST look like:

Breakfast (Time)
Food – grams
Food – grams
Calories: X kcal | Protein: X g | Carbs: X g | Fat: X g | Fiber: X g

Leave ONE blank line between meals.

-----------------------------
FOOD RULES
-----------------------------

Breakfast foods ONLY:
Oats, Poha, Upma, Idli, Banana, Apple,
Milk, Almond milk, Boiled eggs, Sprouts,
Peanut butter, Dry fruits

Snack foods ONLY:
Roasted chana, Fruits, Buttermilk, Nuts,
Protein shake, Curd, Corn salad, Boiled peanuts

Lunch foods ONLY:
Brown rice, White rice, Wheat roti,
Dal, Rajma, Chole, Paneer, Chicken breast,
Fish, Mixed vegetable sabzi, Curd, Salad

Dinner foods ONLY:
Wheat roti, Soya chunks, Dal, Paneer bhurji,
Egg omelette, Vegetable curry, Salad,

-----------------------------
FINAL RULES
-----------------------------
- Indian foods only
- Budget friendly
- Respect diet type (veg/nonveg/vegan)
- Return ONLY the meal plan text
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )

        # Clean output so frontend parsing stays perfect
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"AI Error: {e}"


# ---------------- MAIN FUNCTION ----------------
def generate_meal_plan(user, macros):

    ai_plan = ai_diet_response(user, macros)

    # Keep SAME structure so all existing modules keep working
    return [
        {
            "meal": "AI Diet Plan",
            "food": ai_plan
        }
    ]
