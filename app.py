import streamlit as st

def calculate_monthly_payment(cost, years, interest_rate, maintenance_price, parking_cost, other_expenses):
    # Calculate the total loan amount
    loan_amount = cost + maintenance_price + parking_cost + other_expenses

    # Convert the interest rate from percentage to decimal
    monthly_interest_rate = (interest_rate / 100) / 12

    # Convert the years to months
    months = years * 12

    # Calculate the monthly payment using the formula for fixed monthly payments
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)

    return monthly_payment

def main():
    st.title("Calculadora de Pago Mensual de Apartamento")

    cost_of_apartment = st.number_input("Costo total del apartamento (en Q):")
    payment_years = st.number_input("Tiempo de pago (en años):")
    interest_rate = st.number_input("Tasa de interés anual (%):")
    maintenance_price = st.number_input("Precio mensual de mantenimiento (en Q):")
    parking_cost = st.number_input("Costo mensual de parqueo (en Q):")
    other_expenses = st.number_input("Otros gastos mensuales (en Q):")

    if st.button("Calcular"):
        monthly_payment = calculate_monthly_payment(cost_of_apartment, payment_years, interest_rate, maintenance_price, parking_cost, other_expenses)
        st.success(f"Pago mensual: Q {round(monthly_payment, 2)}")

if __name__ == "__main__":
    main()

