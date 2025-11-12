import streamlit as st
import math

# App Configuration and Title
st.set_page_config(page_title="Simple Calculator", layout="centered")
st.title("Simple Calculator App")
st.markdown("Perform basic arithmetic operations: addition, subtraction, multiplication, and division.")

# Operation Selection
operation = st.selectbox(
    'Select Operation',
    [
        'Addition (+)', 
        'Subtraction (-)', 
        'Multiplication (*)', 
        'Division (/)',
    ]
)

# Initialize variables
result = None
error = None
num1, num2 = None, None

# Input Fields
st.subheader("Enter Two Numbers")
num1 = st.number_input('First Number', value=0.0, step=0.01, key='num1')
num2 = st.number_input('Second Number', value=0.0, step=0.01, key='num2')

# Calculation Logic
if st.button('Calculate'):
    try:
        # Basic Binary Operations
        if operation == 'Addition (+)':
            result = num1 + num2
        elif operation == 'Subtraction (-)':
            result = num1 - num2
        elif operation == 'Multiplication (*)':
            result = num1 * num2
        elif operation == 'Division (/)' :
            if num2 == 0:
                error = "Cannot divide by zero!"
            else:
                result = num1 / num2

    except Exception as e:
        # Catch unexpected calculation errors
        error = f"An unexpected error occurred: {e}"

# Display Result
st.markdown("---")

if error:
    st.error(f"Calculation Error: **{error}**")
elif result is not None:
    # Display the final numerical result using st.metric for visual emphasis
    st.metric(label="Result", value=f"{result:,.6f}")
