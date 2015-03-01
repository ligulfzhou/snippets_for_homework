from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    hello_world = "hello world!"
    return render_template('index.html', hello_world = hello_world)

if __name__ == "__main__":
    app.run()

