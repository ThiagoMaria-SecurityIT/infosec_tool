from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the main route for the homepage
@app.route('/')
def index():
    """
    This function handles requests to the homepage.
    It renders the main layout.
    """
    # The 'page' variable will help us highlight the active link in the sidebar
    return render_template('layout.html', page='explanation')

# This allows us to run the app directly from the command line
if __name__ == '__main__':
    # debug=True will auto-reload the server when you save changes
    app.run(debug=True)
