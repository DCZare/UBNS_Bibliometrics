from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Redirecting to the home route
    return redirect(url_for('home'))

@app.route('/home')
def home():
    # Rendering the home page
    return render_template('home.html')

@app.route('/search_results')
def search_results():
    query = request.args.get('query', '')
    # Rendering the search results page with the query parameter
    return render_template('search_results.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
