from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/') 
def main():
    return render_template('query.html')

@app.route('/process', methods=['POST']) 
def process():
    _username = request.form.get('username')
    if _username:     
        return render_template('response.html', username=_username)
    else:
     return 'Please go back and enter your name...', 400 # 400 Bad Request

