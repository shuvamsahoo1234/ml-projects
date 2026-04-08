from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['STATIC_FOLDER'] = 'static'

import pickle
f=open('p.dat','rb')
y_pred=pickle.load(f)
f.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('plot', filename=file.filename))
    return render_template('index.html',prediction=y_pred)

@app.route('/plot/<filename>', methods=['GET', 'POST'])
def plot(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_csv(filepath)

    plot_url = None
    if request.method == 'POST':
        x_axis = request.form['x_axis']
        y_axis = request.form['y_axis']
        chart_type = request.form['chart']

        plt.figure(figsize=(8, 6))

        if chart_type == 'scatter':
            plt.scatter(df[x_axis], df[y_axis], color='blue')
        elif chart_type == 'bar':
            plt.bar(df[x_axis], df[y_axis], color='o')
        elif chart_type == 'line':
            plt.plot(df[x_axis], df[y_axis], color='red', marker='o')

        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f'{chart_type.capitalize()} plot of {y_axis} vs {x_axis}')
        plt.tight_layout()

        plot_path = os.path.join(app.config['STATIC_FOLDER'], 'plot.png')
        plt.savefig(plot_path)
        plt.close()

        plot_url = '/static/plot.png'

    return render_template('plot.html', columns=df.columns, plot_url=plot_url, filename=filename)

@app.route('/prediction',methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
      p=request.form['wind']
    yp =ed.predict(p)
    return render_template('index.html',prediction=yp)

if __name__ == '__main__':
    app.run(debug=True)
