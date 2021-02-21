from my_model import My_model
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = My_model()

def thread_function():
    import time
    time.sleep(7)
    import webbrowser
    webbrowser.open("http://127.0.0.1:5000/")
import threading
x = threading.Thread(target=thread_function)
x.start()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    str_features = list(request.form.values())[0]
    from ast import literal_eval
    d = literal_eval(str_features)
    d['book_review_count'] = int(d['book_review_count'])
    d['book_rating_count'] = int(d['book_rating_count'])
    print(d)
    prediction = model.predict(d)

    output = round(prediction[0], 2)
    def cut_ind(x, n):
        if len(x) <= n:
            return x
        return x[:n-3]+"..."
    n=18
    return render_template('index.html', prediction_text='Mark would be {}'.format(output), id = str(d['id']), book_title = cut_ind(str(d['book_title']), n), book_genre = cut_ind(str(d['book_genre']), n), book_desc = cut_ind(str(d['book_desc'])[:20], n), book_authors = cut_ind(str(d['book_authors']), n)  )

@app.route('/results',methods=['POST'])
def results():
    d = request.get_json(force=True)
    d['book_review_count'] = int(d['book_review_count'])
    d['book_rating_count'] = int(d['book_rating_count'])
    print(d)
    prediction = model.predict(d)

    output = round(prediction[0], 2)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
