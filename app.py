
import streamlit as st
import requests
API_URL = "https://house-price-prediction-pa9n.onrender.com/predict"

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)
st.markdown("""
<style>
div[data-testid="stFormSubmitButton"] button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #1D4ED8;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🏠 House Price Prediction")
st.write("Enter your house details to estimate its price.")

# House details form
with st.form("house_details_form"):

    area_sqft = st.number_input(
        "Area (square feet)",
        min_value=100,
        max_value=10000,
        value=1500
    )

    bedrooms = st.number_input(
        "Number of bedrooms",
        min_value=1,
        max_value=10,
        value=3
    )

    bathrooms = st.number_input(
        "Number of bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )

    property_age_years = st.number_input(
        "Property age (years)",
        min_value=0,
        max_value=100,
        value=5
    )

    location = st.text_input(
        "Location",
        value="Hyderabad"
    )

    property_type = st.selectbox(
        "Property type",
        ["Apartment", "Independent House", "Villa"]
    )

    parking = st.selectbox(
        "Parking available?",
        ["Yes", "No"]
    )

    submit = st.form_submit_button("Predict House Price")

    if submit:
       

        data = {
        "area_sqft": area_sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "property_age_years": property_age_years,
        "location": location,
        "property_type": property_type,
        "parking": parking
          }

        try:
            response = requests.post(API_URL, json=data)

            if response.status_code == 200:
                result = response.json()
 
                st.success("Prediction Successful!")

                st.subheader(f"Predicted Price: ₹{result['predicted_price']:,.2f}")
            else:
                st.error(f"Prediction failed: {response.text}")

        except requests.exceptions.RequestException as e:
             st.error(f"Connection error: {e}")