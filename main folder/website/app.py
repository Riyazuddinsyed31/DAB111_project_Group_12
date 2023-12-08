from flask import Flask, render_template
import sqlite3
import pathlib

app = Flask(__name__)

base_path = pathlib.Path().cwd() #note: here, the db_creation.ipynb file should be kept and executed in the same path where this file app.py is, in order to get the results from the db 
db_name = "imdb.db"
file_path = base_path / db_name


@app.route("/")
def index():
    return render_template( "index_fillin.html")

@app.route("/about")
def about():
    return render_template( "about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    # Getting the  column names
    cursor.execute("PRAGMA table_info(movies_shows)")
    columns = [column[1] for column in cursor.fetchall()]

    # Getting data
    cursor.execute("SELECT * FROM movies_shows")
    movies_shows = cursor.fetchall()

    con.close()
    return render_template("data_table_fillin.html", columns=columns, movies_shows=movies_shows)

if __name__=="__main__":
    app.run(debug=True)