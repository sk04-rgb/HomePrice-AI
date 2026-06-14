import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

files = [
    "data/mumbai.csv",
    "data/pune.csv",
    "data/bangalore.csv",
    "data/delhi.csv",
    "data/chennai.csv",
    "data/hyderabad.csv",
    "data/kolkata.csv",
    "data/ahmedabad.csv",
    "data/jaipur.csv",
    "data/chandigarh.csv"
]

df = pd.concat([pd.read_csv(file) for file in files])

print("Total Records:", len(df))

X = df.drop("price_lakhs", axis=1)
y = df["price_lakhs"]

categorical_features = ["city", "locality"]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

model = Pipeline([
    ("preprocessor", preprocessor),
    (
        "regressor",
        RandomForestRegressor(
            n_estimators=200,
            random_state=42
        )
    )
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

score = r2_score(y_test, predictions)

print("R2 Score:", score)

joblib.dump(model, "house_model.pkl")

print("Model Saved Successfully")