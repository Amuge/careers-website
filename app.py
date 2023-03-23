from flask import Flask,render_template

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location':'ShangHai',
        'salary':'$3000'
    },
    {
        'id':2,
        'title': 'Data Scientist',
        'location':'Beijing',
        'salary':'$5000'
    },
    {
        'id':3,
        'title': 'Fronted Engineer',
        'location':'ShangHai',
        'salary':'$3000'
    },
    {
        'id':4,
        'title': 'Backend Engineer',
        'location':'ShangHai',
        'salary':'$4000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)