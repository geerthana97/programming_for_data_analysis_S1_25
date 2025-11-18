import streamlit as st
import math

# --- App Configuration and Title ---
st.set_page_config(page_title="BMI Calculator", layout="centered")
st.title("Body Mass Index (BMI) Calculator")
st.markdown("Calculate your BMI based on your weight (kg) and height (m).")

# --- Input Fields ---

st.subheader("Enter Your Measurements")

# Input for Weight (kg)
weight = st.number_input(
    'Weight (kg)',
    min_value=1.0,
    max_value=500.0,
    value=70.0,
    step=0.1,
    help="Enter your body mass in kilograms."
)

# Input for Height (m)
height = st.number_input(
    'Height (m)',
    min_value=0.5,
    max_value=3.0,
    value=1.75,
    step=0.01,
    help="Enter your height in meters (e.g., 1.75 for 175 cm)."
)

# --- Calculation and Interpretation Logic ---

def get_bmi_category(bmi):
    """Returns the BMI category, color for display, and interpretation."""
    if bmi < 18.5:
        return "Underweight", "warning", "You are in the Underweight range. It may be beneficial to consult a health professional."
    elif 18.5 <= bmi < 25:
        return "Normal weight", "success", "You are in the Normal weight range. This is generally considered a healthy weight range."
    elif 25 <= bmi < 30:
        return "Overweight", "warning", "You are in the Overweight range. Consider adopting healthy lifestyle changes."
    else: # bmi >= 30
        return "Obesity", "error", "You are in the Obesity range. Consulting a doctor is highly recommended."

def calculate_bmi(weight_kg, height_m):
    """Calculates BMI using the formula: BMI = weight / (height^2)."""
    if height_m <= 0:
        return None, "Error: Height must be greater than zero."

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)

    return bmi

# --- Display Result ---

if st.button('Calculate BMI'):
    bmi_value = calculate_bmi(weight, height)

    if bmi_value is None:
        st.error("Calculation Error: Height must be a positive value.")
    else:
        category, color, interpretation = get_bmi_category(bmi_value)

        st.success("Calculation Successful!")
        st.markdown("---")

        # Display the calculated BMI value with st.metric
        st.metric(label="Your Calculated BMI is", value=f"{bmi_value:.2f}")

        # Display the category and interpretation using Streamlit's built-in colored text
        st.subheader("BMI Category")

        if color == "success":
            st.markdown(f"**Status:** :green[{category}]")
            st.info(interpretation)
        elif color == "warning":
            st.markdown(f"**Status:** :orange[{category}]")
            st.warning(interpretation)
        elif color == "error":
            st.markdown(f"**Status:** :red[{category}]")
            st.error(interpretation)

        st.caption("Disclaimer: BMI is a screening tool, not a diagnostic one. Consult a healthcare provider for personalized advice.")
