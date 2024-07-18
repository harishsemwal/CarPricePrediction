from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model_path = 'car_price_prediction_model.pkl'
model = joblib.load(model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    if request.method == 'POST':
        try:
            present_price = float(request.form['present_price'])
            kms_driven = int(request.form['kms_driven'])
            owner = int(request.form['owner'])
            years_old = int(request.form['years_old'])
            fuel_type = request.form['fuel_type']
            seller_type = request.form['seller_type']
            transmission = request.form['transmission']
            
            # Validation
            if present_price > 50:
                error = "Present Price should not be greater than 50 lakhs."
            elif kms_driven > 200000:
                error = "Kms Driven should not be greater than 2 lakhs."
            elif years_old > 15:
                error = "Years Old should not be greater than 15 years."
            else:
                # One-hot encoding for categorical features
                fuel_type_diesel = 1 if fuel_type == 'Diesel' else 0
                fuel_type_petrol = 1 if fuel_type == 'Petrol' else 0
                seller_type_individual = 1 if seller_type == 'Individual' else 0
                transmission_manual = 1 if transmission == 'Manual' else 0
                
                # Create a DataFrame for the input
                input_data = pd.DataFrame([[present_price, kms_driven, owner, years_old, 
                                            fuel_type_diesel, fuel_type_petrol, 
                                            seller_type_individual, transmission_manual]], 
                                          columns=['Present_Price', 'Kms_Driven', 'Owner', 'Years Old', 
                                                   'Fuel_Type_Diesel', 'Fuel_Type_Petrol', 
                                                   'Seller_Type_Individual', 'Transmission_Manual'])

                # Predict the selling price
                prediction = model.predict(input_data)[0]

        except ValueError:
            error = "Invalid input. Please enter valid values."

    return render_template('index.html', prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)
