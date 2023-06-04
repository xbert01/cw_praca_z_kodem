from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        name = "Hubert"
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
