from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head><title>ORCID Auth</title></head>
            <body>
                <h1>Welcome to the ORCID Auth Example</h1>
                <a href="/redirect">Redirect to Welcome Page</a>
                <br>
                <a href="/search">Search for Something</a>
            </body>
        </html>
    '''

@app.route('/redirect')
def redirect_to_welcome():
    return redirect('https://dczare.github.io/UBNS_Bibliometrics/welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')  # Renders the home.html template

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('query', '')  # Retrieves the 'query' parameter
    return render_template('search_results.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
