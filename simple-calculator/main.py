import streamlit as st

def main():
    st.title("Simple Calculator")
    st.write("Enter two numbers and persorm an operaton")

    col1,col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter first number :", value=0)
    
    with col2:
        num2 = st.number_input("Enter second number :", value=0)

    operaton = st.selectbox("Choose Operation :", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Dividation (/)"])

    if st.button("Calculate"):
        try:
            if operaton == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operaton == "Subtraction (-)":
                 result = num1 - num2
                 symbol = "-"
            elif operaton == "Multiplication (*)":
                 result = num1 * num2
                 symbol = "*"
            else:
                if num2 == 0:
                    st.error("Error! Dividing by zero!")
                    return
                result = num1 / num2
                symbol = "/"

            st.success(f"{num1}  {symbol} {num2} = {result}")
        except Exception as e:
            st.error(f"An error occured!", {str(e)})

main()