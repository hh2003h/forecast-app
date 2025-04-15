
import streamlit as st
import pickle

# تحميل النموذج
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="📈 Sales Forecast", layout="centered")
st.title("🔮 Sales Forecasting Model")

quantity = st.number_input("Enter quantity:", min_value=0, value=10)

if st.button("Predict"):
    prediction = model.predict([[quantity]])
    st.success(f"Predicted Sales: {prediction[0]:.2f}")
