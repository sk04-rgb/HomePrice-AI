📌 About
HomePrice AI is a machine learning web application that predicts residential property prices across India. You enter details like the city, locality, area, number of bedrooms, bathrooms, floor, and age of the property — and the model returns an estimated price in Lakhs or Crores within seconds.
The model is trained on 5,253+ real estate records collected from 10 Indian cities. It uses a Random Forest Regressor with OneHot encoding for categorical features like city and locality, achieving an R² score of 90.4% on the test set.
This project is end-to-end: from raw CSV data → model training → a Flask web app with a clean, responsive UI.

✨ Features
🔮 Instant price prediction — results in under a second
🏙️ 10 Indian cities — Mumbai, Pune, Bangalore, Delhi, Chennai, Hyderabad, Kolkata, Ahmedabad, Jaipur, Chandigarh
📍 Locality-aware — hundreds of localities across all cities, dynamically loaded in the UI
🤖 Random Forest model — 200 estimators, 90.4% accuracy (R²)
💾 Serialized model — trained once, loaded at runtime via joblib for fast responses
📱 Responsive UI — works on desktop and mobile

