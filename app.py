from flask import Flask, render_template, request, session
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Generate synthetic dataset and train model
np.random.seed(42)
X = np.random.rand(100, 5) * [10, 100, 1, 10, 10]
y = X @ [2.5, 0.35, 4.8, 1.8, 2.9] + np.random.normal(0, 3, 100)
model = LinearRegression().fit(X, y)

def create_plot(features):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10,6))
    feature_names = ['Hours', 'Scores', 'Activities', 'Sleep', 'Papers']
    contributions = model.coef_ * features
    ax.barh(feature_names, contributions, color=['#4CAF50','#2196F3','#FFC107','#9C27B0','#FF5722'])
    ax.set_title('Feature Contributions', pad=20)
    
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['hours']),
            float(request.form['previous_scores']),
            1 if request.form['extracurricular_activities'].strip().lower() == 'yes' else 0,
            float(request.form['sleep']),
            float(request.form['sample_question_papers'])
        ]
        prediction = model.predict([features])[0]
        plot_url = create_plot(features)
        return render_template('result.html', 
                            prediction_text=f'Predicted Score: {prediction:.2f}',
                            plot_url=plot_url)
    except Exception as e:
        return render_template('index.html', 
                            prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
