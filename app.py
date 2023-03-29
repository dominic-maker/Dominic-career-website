from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Nairobi, Kenya',
    'salary': 'Kes. 50,000'
  },
  {
    'id': 2,
    'title': 'Data Science',
    'location': 'Nairobi, Kenya',
    'salary': 'kes. 100,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Nakuru, Kenya',
    'salary': 'kes. 105,000',
  }
]

@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
