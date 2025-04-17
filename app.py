from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Render the form page without prediction text initially
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve form data
        hours = float(request.form['hours'])
        previous_scores = float(request.form['previous_scores'])
        activities = request.form['extracurricular_activities'].strip().lower()
        sleep = float(request.form['sleep'])
        papers = float(request.form['sample_question_papers'])

        # Convert extracurricular activities input to binary
        extra_value = 1 if activities == 'yes' else 0

        # Simple predictive formula (replace with your trained model as needed)
        result = (hours * 2) + (previous_scores * 0.3) + (extra_value * 5) + (sleep * 1.5) + (papers * 3)

        prediction_text = f'Predicted Performance Index: {round(result, 2)}'
    except Exception as e:
        prediction_text = f"Error: {str(e)}"

    # Render the same page with prediction result
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
