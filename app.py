from flask import Flask, redirect, url_for

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
  # This is the new view function for the "/home" route
  # You can add any content or logic you want to display on the home page here
  return '''
      <html>
          <head><title>Home Page</title></head>
          <body>
              <h1>Welcome to the Home Page</h1>
          </body>
      </html>
  '''

if __name__ == '__main__':
    app.run(debug=True)