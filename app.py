from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serve index.html

@app.route('/redirect')
def redirect_to_welcome():
    return redirect('https://dczare.github.io/UBNS_Bibliometrics/welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')  # Serve home.html

if __name__ == '__main__':
    app.run(debug=True)
