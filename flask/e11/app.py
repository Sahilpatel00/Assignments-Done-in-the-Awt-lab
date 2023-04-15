from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def insert_data(name, email, address, hobby):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email, address, hobby) VALUES (?, ?, ?, ?)", (name, email, address, hobby))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        hobby = request.form['hobby']
        
        insert_data(name, email, address, hobby)
        
    return render_template('index.html')

@app.route('/view')
def view():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    conn.close()
    return render_template('view.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
