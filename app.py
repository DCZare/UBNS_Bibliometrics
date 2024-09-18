from flask import Flask, redirect, render_template, request, url_for

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
                <br><br>
                <form action="/search" method="get">
                    <input type="text" name="query" placeholder="Enter search term">
                    <button type="submit">Search</button>
                </form>
            </body>
        </html>
    '''

@app.route('/redirect')
def redirect_to_welcome():
    if 'localhost' in request.host:
        return redirect(url_for('local_welcome'))
    else:
        return redirect('https://dczare.github.io/UBNS_Bibliometrics/welcome.html')

@app.route('/welcome')
def local_welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')  # Retrieves the 'query' parameter
    return render_template('search_results.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
