from flask import Flask, request, jsonify
import joblib

# load your trained model
model = joblib.load("./model.pkl")

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Calories Burnt Estimation API!"

@app.route ('/predict', methods = ['POST'])
def predict():
    try:
        data = request.get_json()
        steps = data.get("steps")

        if steps is None:
            return jsonify({"error": "Missing 'steps' in request"}), 400
        prediction = model.predict([[steps]])
        return jsonify({"steps": steps, "predicted calories_burnt": round(prediction[0], 2)})
    
    except Exception as e:
        return jsonify ({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)