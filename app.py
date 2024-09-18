from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head><title>ORCID Auth</title></head>
            <body>
                <h1>Welcome to the ORCID Auth Example</h1>
                <a href="/redirect">Redirect to Welcome Page</a>
            </body>
        </html>
    '''

@app.route('/redirect')
def redirect_to_welcome():
    return redirect('https://dczare.github.io/UBNS_Bibliometrics/welcome.html')

@app.route('/home')
def home():
    return render_template('https://dczare.github.io/UBNS_Bibliometrics/home.html')  # Renders the home.html template

if __name__ == '__main__':
    app.run(debug=True)
