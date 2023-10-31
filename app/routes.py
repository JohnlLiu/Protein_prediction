from flask import Flask, render_template, request
from app import protein as protein

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    user_input = None
    result = None

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        result = protein.create_protein(user_input) 

    return render_template('index.html', user_input=user_input, result=result)

if __name__ == '__main__':
    app.run(debug=True)