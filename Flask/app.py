from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    # Handle the login logic here
    # You can retrieve the form data using request.form
    username = request.form['username']
    password = request.form['password']
    user_type = request.form['userType']

    # Add your authentication logic here (for simplicity, checking if username and password are not empty)
    if username and password:
        # Redirect to the appropriate route based on user type
        if user_type == 'student':
            return redirect('web1')
        elif user_type == 'teacher':
            return redirect('web2')
    
    # If authentication fails or form data is incomplete, redirect back to the login page
    return redirect('login.html')
@app.route('/web1')
def web1():
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
