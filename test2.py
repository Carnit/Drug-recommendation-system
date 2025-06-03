from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle
import pandas as pd
import requests  # To make HTTP requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="css"), name="static")
templates = Jinja2Templates(directory="templates")

# Load medicine data (assuming these functions are defined elsewhere)
def load_medicines():
    medicines_dict = pickle.load(open("medicine_dict.pkl", "rb"))
    return pd.DataFrame(medicines_dict)

def load_similarity():
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return similarity

# Caching for medicine information (efficiency)
medicine_info_cache = {}

def get_medicine_info(medicine_name):
    if medicine_name in medicine_info_cache:
        return medicine_info_cache[medicine_name]

    url = f"https://api.fda.gov/drug/label.json?search=generic_name:{medicine_name}"
    try:
        response = requests.get(url)
        data = response.json()
        if "results" in data:
            result = data["results"][0]
            description = result.get("description", ["No description available"])[0]
            side_effects = result.get("adverse_reactions", ["No side effects data available"])[0]
            medicine_info_cache[medicine_name] = (description, side_effects)
            return description, side_effects
        else:
            return "No data available", "No data available"
    except Exception as e:
        return "Error fetching data", str(e)


# Medicine recommendation function
def recommend(medicine):
    medicines = load_medicines()
    similarity = load_similarity()

    try:
        medicine_index = medicines[medicines["Drug_Name"] == medicine].index[0]
    except IndexError:
        return ["Medicine not found"]

    distances = similarity[medicine_index]
    medicines_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicine = medicines.iloc[i[0]].Drug_Name
        description, side_effects = get_medicine_info(recommended_medicine)
        recommended_medicines.append(
            {
                "name": recommended_medicine,
                "url": f"https://pharmeasy.in/search/all?name={recommended_medicine}",
                "description": description,
                "side_effects": side_effects,
            }
        )
    return recommended_medicines


# Application Frontend
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    medicines = load_medicines()
    return templates.TemplateResponse(
        "index.html", {"request": request, "medicines": medicines["Drug_Name"].values}
    )


@app.post("/recommend", response_class=HTMLResponse)
async def recommend_medicine(request: Request, selected_medicine_name: str = Form(...)):
    recommendations = recommend(selected_medicine_name)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "selected_medicine_name": selected_medicine_name,
            "recommendations": recommendations,
        },
    )