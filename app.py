from flask import Flask,render_template,request
import joblib
model=joblib.load('marks_model.pkl')
app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def add():
        return render_template('add.html')

@app.route('/predictmarks',methods = ['POST'])
def adddata():
    hr = float(request.form['hours'])
    att = float(request.form['attendance'])
    input_data =[[hr,att]]
    predicted_marks = model.predict(input_data)[0]
    return render_template('show.html', hours=hr, attendance=att, marks=round(predicted_marks, 2))


if __name__ == "__main__":
    app.run(debug=True)