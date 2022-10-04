from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Fuck Programming. This shit is too hard"

if __name__ == '__main__':
    app.env = 'development'
    app.run(debug=True)