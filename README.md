# 🏠 House Price Prediction – Streamlit Frontend

## 📌 Project Overview

This project is the frontend application for a Machine Learning-based House Price Prediction system.

It is developed using Streamlit and connected to a deployed FastAPI backend.

Users can enter property details through an interactive web interface and receive predicted house prices from the trained Machine Learning model.

## 🎯 Project Objectives

- Build an interactive frontend using Streamlit.
- Collect house details through user input fields.
- Connect the frontend with a deployed FastAPI backend.
- Send prediction requests using HTTP POST.
- Display the predicted house price in a user-friendly format.

## 🛠️ Technologies Used

- Python
- Streamlit
- Requests
- FastAPI (backend integration)
- GitHub
- Streamlit Community Cloud

## ✨ Features

- Interactive house price prediction form.
- Input fields for property details.
- Dropdown selection for property type and parking.
- API integration with FastAPI.
- Real-time prediction response display.
- Error handling for API communication.

## 📊 User Input Features

- Area in square feet
- Number of bedrooms
- Number of bathrooms
- Property age
- Location
- Property type
- Parking availability

## ⚙️ [er.com/predict](https://house-price-prediction-pa9n.onrender.com/predict)

## Project Structure

```text
House-Price-Prediction-Frontend/
│
├── app.py
├── requirements.txt
└── README.md
```

## 🔗 Backend API Integration

The frontend communicates with the deployed FastAPI backend.

**Backend URL:**

[https://house-price-prediction-pa9n.onrender.com](https://house-price-prediction-pa9n.onrender.com)

**Prediction Endpoint:**

[https://house-price-prediction-pa9n.onrend](https://house-price-prediction-pa9n.onrend)

The frontend sends house details as JSON data using the Python Requests library.

The backend processes the input through the trained Machine Learning model and returns the predicted price.

## 🚀 Installation and Setup

Clone the repository:

```bash
git clone YOUR_FRONTEND_GITHUB_REPOSITORY_URL
```

Navigate to the folder:

```bash
cd House-Price-Prediction-Frontend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at:

[http://localhost:8501](http://localhost:8501)

## ☁️ Deployment

The frontend is prepared for deployment using **Streamlit Community Cloud**.

Deployment steps:

1. Push the source code to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Connect the GitHub repository.
4. Select `app.py` as the main application file.
5. Deploy the application.

**Live Frontend:** Add your Streamlit application URL here after deployment.

## 🔮 Future Improvements

- Improve the user interface and design.
- Add prediction history.
- Display additional property insights.
- Add input validation.
- Improve the overall user experience.

## 👩‍💻 Author

**GADDAM LATHIKA**

Aspiring AI Engineer | Machine Learning | Python | FastAPI | Streamlit

---

*This frontend uses a Machine Learning backend trained on synthetic practice data. Predictions are for demonstration and learning purposes, not real-world property valuation.*
