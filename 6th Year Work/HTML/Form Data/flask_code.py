from flask import Flask, render_template, url_for, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')
@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route('/forms_test')
def forms_test():
    return render_template("forms_test.html")

@app.route('/receive_form_data', methods=["POST"])
def receive_form_data():
    db_connection = sqlite3.connect("Databas.db")
#cursor object
    cursor = db_connection.cursor()
    addData = '''
insert into weigo (Name, Sex, Country, Message, Subscribe) values (?,?,?,?,?);
'''
    data = request.form
    print(data)
    vals = []
    for values in data.values():
        vals.append(values)
    cursor.execute(addData,vals)
    db_connection.commit()
    cursor.close()
    db_connection.close()
    return "Apple"

if __name__ == "__main__":
    app.run()


