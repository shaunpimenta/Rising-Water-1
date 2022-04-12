from flask import Flask,render_template,redirect
import sea
app= Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/map')
def predict():
    return render_template('map1.html')
@app.route('/temp')
def temp():
    return render_template('temp.html')
@app.route('/tempvssea')
def sea():
    return render_template('')
if __name__=='__main__':
    app.run(debug=True)
