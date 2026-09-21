import streamlit as st
import joblib
import numpy as np

st.title('Delivery Delay Prediction')

# Load the trained model
model = joblib.load('delivery_delay.sav')

# Define the input features based on x.columns
feature_names = ['Delivery_Distance', 'Traffic_Congestion', 'Weather_Condition',
                 'Delivery_Slot', 'Driver_Experience', 'Num_Stops', 'Vehicle_Age',
                 'Road_Condition_Score', 'Package_Weight', 'Fuel_Efficiency',
                 'Warehouse_Processing_Time']

# Create input fields for each feature
input_data = {}
for feature in feature_names:
    if feature in ['Traffic_Congestion', 'Weather_Condition', 'Delivery_Slot', 'Num_Stops', 'Vehicle_Age', 'Driver_Experience', 'Road_Condition_Score', 'Warehouse_Processing_Time']:
        input_data[feature] = st.number_input(f'Enter {feature.replace("_", " ")}', min_value=0, max_value=100, value=5)
    elif feature in ['Delivery_Distance', 'Package_Weight', 'Fuel_Efficiency']:
        input_data[feature] = st.number_input(f'Enter {feature.replace("_", " ")}', min_value=0.0, value=10.0, format="%.2f")

# Make prediction when button is clicked
if st.button('Predict Delivery Delay'):
    # Convert input data to a numpy array in the correct order
    features_array = np.array([input_data[f] for f in feature_names]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features_array)

    # Display the result
    if prediction[0] == 1:
        st.error('Prediction: Delivery Delay')
    else:
        st.success('Prediction: No Delivery Delay')
