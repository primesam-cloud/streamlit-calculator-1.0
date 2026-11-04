
import streamlit as st

st.title("Welcome to Calculator 1.0")
st.write("Perform any mathematical operation of your choice.")

a = st.number_input("Enter your first number")
b = st.number_input("Enter your second number")

c = st.selectbox(
    "Enter the operation you wish to perform",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Integer Division",
        "Power"
    ]
)

if st.button("Calculate"):

    if c.lower() == "addition":
        st.write(a + b)

    elif c.lower() == "subtraction":
        st.write(a - b)

    elif c.lower() == "power":
        st.write(a ** b)

    elif c.lower() == "division":
        if b == 0:
            st.error("Cannot be divided by zero")
        else:
            st.write(a / b)

    elif c.lower() == "integer division":
        if b == 0:
            st.error("Cannot be divided by zero")
        else:
            st.write(a // b)

    elif c.lower() == "multiplication":
        st.write(a * b)

    else:
        st.error("Enter a valid operation")

