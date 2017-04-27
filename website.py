import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def webprint():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
