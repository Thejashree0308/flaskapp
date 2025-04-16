from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # NOT "Hello World"

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])
    previous_scores = float(request.form['previous_scores'])
    activities = request.form['extracurricular_activities'].strip().lower()
    sleep = float(request.form['sleep'])
    papers = float(request.form['sample_question_papers'])

    extra_value = 1 if activities == 'yes' else 0
    result = (hours * 2) + (previous_scores * 0.3) + (extra_value * 5) + (sleep * 1.5) + (papers * 3)

    return render_template('index.html', prediction_text=f'Predicted Performance Index: {round(result, 2)}')
