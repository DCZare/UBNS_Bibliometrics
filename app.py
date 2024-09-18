from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Default landing page (Welcome Page)
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Home Page (where the user is redirected after clicking login)
@app.route('/home')
def home():
    return render_template('home.html')

# Search Route with dynamic results
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    return redirect(url_for('dynamic_search_results', query=query))

# Dynamic search results page
@app.route('/search/results/<query>')
def dynamic_search_results(query):
    return render_template('search_results.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
