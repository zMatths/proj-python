from flask import render_template, request, redirect
from database.db_connection import get_db_connection

def register_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Insere o usuário no banco de dados
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            connection.commit()
        except:
            return "User already exists."
        finally:
            cursor.close()
            connection.close()

        return redirect('/login')

    return render_template('register.html')