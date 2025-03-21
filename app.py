
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return f"Thank you, {name}! Your message has been received."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"),debug=True)