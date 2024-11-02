from flask import Flask, render_template, jsonify
import psycopg2
from psycopg2 import Error

app = Flask(__name__)

# Function to connect to the PostgreSQL database
def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="raywu1990",
            password="test",
            host="127.0.0.1",
            port="5432",
            database="dvdrental"
        )
        return connection
    except Error as e:
        return str(e)

# Route to insert a new row into basket_a
@app.route('/api/update_basket_a')
def update_basket_a():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # Insert a new row into basket_a
        cursor.execute("INSERT INTO basket_a (id, fruit) VALUES (5, 'Cherry')")
        connection.commit()

        cursor.close()
        connection.close()

        return "Success!"
    except Error as e:
        return str(e)

# Route to show unique fruits in basket_a and basket_b
@app.route('/api/unique')
def unique_fruits():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # Get unique fruits from basket_a
        cursor.execute("SELECT DISTINCT fruit FROM basket_a")
        basket_a_fruits = [row[0] for row in cursor.fetchall()]

        # Get unique fruits from basket_b
        cursor.execute("SELECT DISTINCT fruit FROM basket_b")
        basket_b_fruits = [row[0] for row in cursor.fetchall()]

        cursor.close()
        connection.close()

        return render_template('unique_fruits.html', basket_a=basket_a_fruits, basket_b=basket_b_fruits)
    except Error as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
