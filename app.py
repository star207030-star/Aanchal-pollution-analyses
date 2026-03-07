from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        aqi_values = request.form['aqi']
        aqi_list = list(map(float, aqi_values.split(",")))

        days = np.arange(1, len(aqi_list)+1).reshape(-1,1)

        model = LinearRegression()
        model.fit(days, aqi_list)

        next_day = np.array([[len(aqi_list)+1]])
        prediction = model.predict(next_day)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)