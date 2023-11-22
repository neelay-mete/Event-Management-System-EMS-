from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/web2')
def web2():
    return render_template('web2.html')

@app.route('/web3')
def web3():
    return render_template('web3.html')

@app.route('/web4')
def web4():
    return render_template('web4.html')

@app.route('/web5')
def web5():
    return render_template('web5.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
