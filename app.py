from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("house_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    city = request.form["city"]
    locality = request.form["locality"]

    area = float(request.form["area"])
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])
    floor = int(request.form["floor"])
    age = int(request.form["age"])

    input_df = pd.DataFrame({
        "city": [city],
        "locality": [locality],
        "area_sqft": [area],
        "bhk": [bhk],
        "bath": [bath],
        "floor": [floor],
        "age_years": [age]
    })

    prediction = model.predict(input_df)[0]

    if prediction >= 100:
        result = f"₹ {prediction/100:.2f} Crore"
    else:
        result = f"₹ {prediction:.2f} Lakhs"

    return render_template(
        "index.html",
        prediction=result
    )

if __name__ == "__main__":
    app.run(debug=True)