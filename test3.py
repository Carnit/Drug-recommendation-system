import streamlit as st
import pickle
import pandas as pd
import requests  # To make HTTP requests

## Application Backend ##

# To load medicine-dataframe from pickle in the form of dictionary
medicines_dict = pickle.load(open("medicine_dict.pkl", "rb"))
medicines = pd.DataFrame(medicines_dict)

# To load similarity-vector-data from pickle in the form of dictionary
similarity = pickle.load(open("similarity.pkl", "rb"))

# Function to get medicine description and side effects from OpenFDA API
def get_medicine_info(medicine_name):
    url = f"https://api.fda.gov/drug/label.json?search=generic_name:{medicine_name}"
    try:
        response = requests.get(url)
        data = response.json()
        if "results" in data:
            result = data["results"][0]  # Get the first result
            description = result.get("description", ["No description available"])[0]
            side_effects = result.get("adverse_reactions", ["No side effects data available"])[0]
            return description, side_effects
        else:
            return "No data available", "No data available"
    except Exception as e:
        return "Error fetching data", str(e)


# Medicine recommendation function
def recommend(medicine):
    medicine_index = medicines[medicines["Drug_Name"] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines


## Application Frontend ##

# Title of the Application
st.title("Prescription Recommendation System with Drug Info")

# Custom CSS (unchanged)
st.markdown(
    """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f6;
            color: #333;
            margin: 0;
            padding: 0;
        }
        h1 {
            color: #ff6666;
            background-color: #ffffcc;
            border: 2px solid #000;
            border-radius: 20px;
            padding: 10px;
            text-align: center;
            margin-bottom: 20px;
        }
        .stButton>button {
            font-size: 18px;
            font-weight: bold;
            background-color: #328188;
            color: #fff;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            margin-bottom: 20px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #2c6e70;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background-color: #a1d6ea;
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            margin-bottom: 10px;
        }
        a {
            padding: 5px 10px;
            background-color: #000;
            color: #fff;
            border: 1px solid #000;
            border-radius: 5px;
            text-decoration: none;
            transition: background-color 0.3s;
        }
        a:hover {
            background-color: #333;
        }
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Searchbox for medicine
selected_medicine_name = st.selectbox(
    "Type your medicine name whose alternative is to be recommended",
    medicines["Drug_Name"].values,
)

# Recommendation Program
if st.button("Recommend Medicine"):
    recommendations = recommend(selected_medicine_name)
    j = 1
    for i in recommendations:
        st.write(f"{j}. {i}")  
        st.write(f"Click here -> https://pharmeasy.in/search/all?name={i}")

        # Fetch and display description and side effects using OpenFDA API
        description, side_effects = get_medicine_info(i)
        st.write(f"**Description**: {description}")
        st.write(f"**Side Effects**: {side_effects}")

        j += 1

# Image
st.image(
    "images/image.jpg", caption="Recommended Medicines", use_column_width=True
)
