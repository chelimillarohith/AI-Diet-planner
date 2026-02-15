from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from calorie_engine import calculate_calories
from macros import calculate_macros
from meal_generator import generate_meal_plan
from supplement_engine import recommend_supplements
from grocery_list import create_grocery_list

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate", response_class=HTMLResponse)
async def generate_plan(
    request: Request,
    goal: str = Form(...),
    weight: float = Form(...),
    height: float = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    activity_level: str = Form(...),
    body_type: str = Form(...),
    weight_tendency: str = Form(...),
    diet_type: str = Form(...),
    health_issues: str = Form(""),
    budget: str = Form(...),
    meals_per_day: int = Form(...),
    cooking_style: str = Form(...)
):

    user_data = {
        "goal": goal,
        "weight": weight,
        "height": height,
        "age": age,
        "gender": gender,
        "activity_level": activity_level,
        "body_type": body_type,
        "weight_tendency": weight_tendency,
        "diet_type": diet_type,
        "health_issues": health_issues,
        "budget": budget,
        "meals_per_day": meals_per_day,
        "cooking_style": cooking_style,
        "low_sunlight": True,
        "deficiency": False
    }

    calories = calculate_calories(user_data)
    macros = calculate_macros(user_data, calories)
    meals = generate_meal_plan(user_data, macros)
    supplements = recommend_supplements(user_data)
    grocery = create_grocery_list(meals)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": {
            "calories": calories,
            "macros": macros,
            "meals": meals,
            "supplements": supplements,
            "grocery": grocery
        }
    })
