from flask import Flask, render_template
from database.db_connection import get_db_connection
from routes.login import login_user
from routes.register import register_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set up database connection
db_connection = get_db_connection()

# Register routes
app.add_url_rule('/login', 'login', login_user, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', register_user, methods=['GET', 'POST'])

# Home route
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)