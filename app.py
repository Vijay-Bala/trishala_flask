import streamlit as st
import pandas as pd
import pickle

# Load the pickled model
with open('model1.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the dataset to get the unique village names
data = pd.read_excel(r'C:\Users\vijay\OneDrive\Desktop\Trishala\KSP Hackathon\Final-dataset1.xlsx')  # Adjust the file path as necessary

# Function to make predictions
def predict_total_crimes(Village_Area_Name, Year):
    # Check if the village name is valid
    if Village_Area_Name not in data['Village_Area_Name'].unique():
        return "Unknown village name. Please provide a valid village name."

    # Prepare input data for prediction
    input_data = pd.DataFrame({'Village_Area_Name': [Village_Area_Name], 'Year': [Year]})

    # One-hot encode categorical variables using the same categories as in the training data
    input_data_encoded = pd.get_dummies(input_data, columns=['Village_Area_Name'])
    input_data_encoded = input_data_encoded.reindex(columns=data.columns, fill_value=0)

    # Make predictions
    prediction = model.predict(input_data_encoded)

    return prediction[0]


# Streamlit UI
def main():
    st.title('Predict Total Crimes')
    st.write('Enter the village name and year to predict the total crimes.')

    # User inputs
    Village_Area_Name = st.text_input('Enter the village name:')
    Year = st.number_input('Enter the year:', value=2022)

    # Make prediction when user clicks the button
    if st.button('Predict'):
        prediction = predict_total_crimes(Village_Area_Name, Year)
        st.write(f'Predicted number of crimes in {Village_Area_Name} for the year {Year}: {prediction}')

if __name__ == '__main__':
    main()
