from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pickled model
model = pickle.load(open(r'model1.pkl', 'rb'))

# Load the dataset
data = pd.read_csv(r"Final-dataset1.csv")

# One-hot encode 'Village_Area_Name'
data_encoded = pd.get_dummies(data, columns=['Village_Area_Name'])

# Ensure all columns are in the same order as during training
data_encoded = data_encoded.reindex(columns=data_encoded.columns, fill_value=0)

# Load accused data
accused_df = pd.read_csv(r"AccusedData.csv")

# Function to get accused details by location, time, and year
def get_accused_by_location_year(location, year):
    accused_details = accused_df[(accused_df['PresentAddress'] == location) &
                                 (accused_df['Year'] == year)]
    print(accused_details)
    return accused_details

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/main.html')
def main():
    return render_template('main.html')

@app.route('/login', methods=['POST'])
def login():
    # Handle login logic here
    return render_template('login1.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)  # Print form data for debugging

        location = request.form.get('location')
        year = request.form.get('year')

        if not location or not year:
            print("Missing location or year")  # Print debug message
            return render_template('error.html', message="Please provide both location and year.")

        year = int(year)
        accused_details = get_accused_by_location_year(location, year)

        if accused_details.empty:
            message = "No accused found."
        else:
            message = "Accused Details in {} in the year {}: ".format(location, year)
            accused_data = accused_details[['Person_Name', 'age', 'Caste', 'Sex']]
            accused_data = accused_data.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
            return render_template('results.html', accused_data=accused_data, message=message)

    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    # if request.method == 'POST':
    location = request.form.get('location')
    year = request.form.get('year')
    # print(location, year)
    if not location or not year:
        return render_template('error.html', message="Please provide both location and year.")

    year = int(year)
    accused_details = get_accused_by_location_year(location, year)

    if accused_details.empty:
        message = "No accused found."
        print("hello")
    else:
        message = "Accused Details in {} in the year {}: ".format(location, year)
        accused_data = accused_details[['Person_Name', 'age', 'Caste', 'Sex']]
        accused_data = accused_data.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
        print(accused_data)
        return render_template('results.html', accused_data=accused_data, message=message)
        
    return render_template('index.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/chatbot.html')
def chatbot():
    return render_template('chatbot.html')

@app.route('/map.html')
def map():
    return render_template('map.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Function to calculate total crimes for a village and year
    def total_crimes_for_village_and_year(village_name, year, data):
        # Filter the dataset based on the provided village name and year
        village_name = village_name.upper()
        filtered_data = data[(data['Village_Area_Name'] == village_name) & (data['Year'] == year)]

        # Check if there are any records matching the filtering criteria
        if filtered_data.empty:
            return None

        # Extract the target variable value (Total Crimes) for the filtered data
        total_crimes = filtered_data['Total Crimes'].iloc[0]

        return total_crimes

    village_name = request.form.get('village_name')
    year = request.form.get('year')

    if not village_name or not year:
        return render_template('error.html', message="Please provide both village name and year.")

    year = int(year)
    prediction = total_crimes_for_village_and_year(village_name, year, data)

    warning_image = False
    if prediction is not None:
        if prediction > 100:
            warning_image = True

    return render_template('prediction.html', prediction=prediction, warning_image=warning_image, location=village_name, year=year)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
