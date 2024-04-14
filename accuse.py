from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load accused data
accused_df = pd.read_csv(r"C:\Users\vijay\OneDrive\Desktop\Trishala\KSP Hackathon\AccusedData.csv")

# Function to get accused details by location, time, and year
def get_accused_by_location_year(location, year):
    accused_details = accused_df[(accused_df['PresentAddress'] == location) &
                                 (accused_df['Year'] == year)]
    return accused_details

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        year = int(request.form['year'])
        accused_details = get_accused_by_location_year(location, year)
        if accused_details.empty:
            message = "No accused found."
        else:
            message = "Accused Details in {} in the year {}: ".format(location, year)
            accused_details = accused_details[['Person_Name', 'age', 'Caste', 'Sex']]
            accused_data = accused_details.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
            return render_template('results.html', accused_data=accused_data, message=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
