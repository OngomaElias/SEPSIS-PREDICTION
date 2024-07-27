import streamlit as st
import requests

# Define the backend URL
backend_url = "http://api:80"

# Set page configurations
st.set_page_config(
    page_title='Sepsis Prediction App',
    layout='wide',
    page_icon=None
)

def show_form():
    st.title('Sepsis Prediction App')

    with st.form('input-feature'):
        # Input fields for sepsis prediction features
        st.header("Input Patient Features")

        col1, col2, col3 = st.columns(3)

        with col1:
            PRG = st.number_input("Plasma Glucose (PRG)", min_value=0.0, step=0.1, key='PRG')
            PL = st.number_input("Blood Work Result (PL)", min_value=0.0, step=0.1, key='PL')
            PR = st.number_input("Pulse Rate (PR)", min_value=0.0, step=0.1, key='PR')
            SK = st.number_input("Skin Thickness (SK)", min_value=0.0, step=0.1, key='SK')

        with col2:
            TS = st.number_input("Thyroid Stimulating (TS)", min_value=0.0, step=0.1, key='TS')
            M11 = st.number_input("M11", min_value=0.0, step=0.1, key='M11')
            BD2 = st.number_input("Body Density (BD2)", min_value=0.0, step=0.1, key='BD2')

        with col3:
            Age = st.number_input("Age", min_value=0.0, step=1.0, key='Age')
            Insurance = st.number_input("Insurance (0 for No, 1 for Yes)", min_value=0, step=1, key='Insurance')

        model_option = st.selectbox("Choose Model", ["Support Vector", "Gradient Boost", "Random Forest"])

        # Predict button
        if st.form_submit_button('Predict Sepsis Status'):
            # Create a dictionary with the input data
            input_data = {
                "PRG": PRG,
                "PL": PL,
                "PR": PR,
                "SK": SK,
                "TS": TS,
                "M11": M11,
                "BD2": BD2,
                "Age": Age,
                "Insurance": Insurance
            }

            # Determine the endpoint based on model choice
            endpoint = ""
            if model_option == "Support Vector":
                endpoint = "/support_vector_prediction"
            elif model_option == "Gradient Boost":
                endpoint = "/gradient_boost_prediction"
            elif model_option == "Random Forest":
                endpoint = "/random_forest_prediction"

            # Send a request to the FastAPI backend
            response = requests.post(f"{backend_url}{endpoint}", json=input_data)

            # Display the prediction
            if response.status_code == 200:
                prediction = response.json()['prediction']
                st.success(f'The predicted sepsis status is: {prediction}')
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")

if __name__ == "__main__":
    show_form()