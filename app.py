# app.py

from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    try:
        summary = wikipedia.summary(query)
    except wikipedia.exceptions.DisambiguationError as e:
        summary = "Sorry, there are multiple articles related to this topic. Please provide more specific information."
    except wikipedia.exceptions.PageError as e:
        summary = "Sorry, I couldn't find any information related to this topic."
    return render_template('result.html', query=query, summary=summary)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
