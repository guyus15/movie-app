from flask import Flask, render_template
import requests

app = Flask('__name__')

@app.route('/')
def index():
    films = requests.get('http://www.omdbapi.com/?apikey=501fb2ae&s=Game%20of%20Thrones')
    films = films.json()['Search']

    return render_template('index.html', films=films)

if __name__ == '__main__':
    app.run(debug=True)
