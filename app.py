from flask import Flask, render_template, request
import numpy as np
import pickle

application = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@application.route("/")
@application.route("/home")
def hello():
    return render_template("index.html")

@application.route("/visualization")
def visualization():
    return render_template("visual.html")

@application.route("/pred", methods=['GET', 'POST'])
def pred():
    if request.method == 'POST':
        lat = request.form['lat']
        long = request.form['long']
        alt = request.form['alt']
        x_pred = np.array([[float(alt), float(lat), float(long)]]).reshape(-1, 3)
        y_pred = model.predict(x_pred)
        pred_text = 'Download speed (mbps): {0:.6f},  Upload speed (mbps): {1:.6f}'.format(y_pred[0][0],y_pred[0][1])
        res = {"pred": pred_text}
        return res
    return render_template("pred.html", type="GET")

if __name__ == "__main__":
    application.run(host='0.0.0.0')
