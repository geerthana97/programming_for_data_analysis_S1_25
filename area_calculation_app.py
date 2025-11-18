import streamlit as st
import math

# --- App Configuration and Title ---
st.set_page_config(page_title="Area Calculation App", layout="centered")
st.title("Geometric Area Calculator")
st.markdown("Calculate the area of common geometric shapes.")

# --- 1. Shape Selection ---
selected_shape = st.selectbox(
    'Select the Shape',
    ['Circle', 'Rectangle', 'Triangle']
)

# Initialize variables
area = None
error = None

# --- 2. Dynamic Input Fields ---
st.subheader(f"Enter Dimensions for {selected_shape}")

if selected_shape == 'Circle':
    radius = st.number_input('Radius (r)', min_value=0.0, value=5.0, step=0.1)

elif selected_shape == 'Rectangle':
    length = st.number_input('Length (l)', min_value=0.0, value=10.0, step=0.1)
    width = st.number_input('Width (w)', min_value=0.0, value=5.0, step=0.1)

elif selected_shape == 'Triangle':
    base = st.number_input('Base (b)', min_value=0.0, value=8.0, step=0.1)
    height = st.number_input('Height (h)', min_value=0.0, value=4.0, step=0.1)

# --- 3. Calculation Logic ---

if st.button('Calculate Area'):
    if selected_shape == 'Circle':
        if radius < 0:
            error = "Radius cannot be negative."
        else:
            # Area = π * r²
            area = math.pi * (radius ** 2)
            # Display the formula using LaTeX markdown
            st.markdown(f"**Formula:** $A = \pi r^2$")

    elif selected_shape == 'Rectangle':
        if length < 0 or width < 0:
            error = "Length and width cannot be negative."
        else:
            # Area = l * w
            area = length * width
            # Display the formula using LaTeX markdown
            st.markdown(f"**Formula:** $A = l \\times w$")

    elif selected_shape == 'Triangle':
        if base < 0 or height < 0:
            error = "Base and height cannot be negative."
        else:
            # Area = 0.5 * b * h
            area = 0.5 * base * height
            # Display the formula using LaTeX markdown
            st.markdown(f"**Formula:** $A = \\frac{1}{2} b \\times h$")

# --- 4. Display Result ---
st.markdown("---")

if error:
    st.error(f"Calculation Error: **{error}**")
elif area is not None:
    # Display the final numerical result
    st.metric(label=f"Area of the {selected_shape}", value=f"{area:,.4f} units²")
