from flask import render_template, request, redirect, session
from database.db_connection import get_db_connection

def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verifica o usuário no banco de dados
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user:
            session['username'] = user['username']
            return f"Hello, {user['username']}!"
        else:
            return "Invalid username or password."

    return render_template('login.html')