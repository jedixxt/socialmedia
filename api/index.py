from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cif/')
def about():
    return render_template('cif.html')
    
@app.route('/bt1')
def bt1():
    print('BT 1')
    return "Nothing"

@app.route('/bt2')
def bt2():
    print('BT 2')
    return "Nothing"

if __name__ == '__main__':
   app.run(debug=True, use_reloader=True)
