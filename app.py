from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return '<h1>Welcome! You have successfully authenticated with ORCID.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
