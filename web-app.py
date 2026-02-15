import streamlit as st

# Streamlit UI
st.title("Basic Calculator App -- ")
st.write("Perform basic arithmetic operations on two numbers.")

# User inputs
num1 = st.number_input("Enter first number - ", value=0.0)
num2 = st.number_input("Enter second number - ", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose an operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculation
if operation == "Addition":
    result = num1 + num2
    st.write(f"Result: {num1} + {num2} = {result}")

elif operation == "Subtraction":
    result = num1 - num2
    st.write(f"Result: {num1} - {num2} = {result}")

elif operation == "Multiplication":
    result = num1 * num2
    st.write(f"Result: {num1} × {num2} = {result}")

elif operation == "Division":
    if num2 == 0:
        st.error("Division by zero is not allowed.")
    else:
        result = num1 / num2
        st.write(f"Result: {num1} ÷ {num2} = {result}")


# Calculate results
square1 = num1 ** 2
square2 = num2 ** 2

# Display results
st.write(f"The square of {num1} is: {square1}")
st.write(f"The square of {num2} is: {square2}")