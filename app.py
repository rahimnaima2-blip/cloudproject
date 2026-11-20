
from flask import Flask
from database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue dans le système de gestion universitaire !"

@app.route("/departments")
def departments():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM departments")

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
