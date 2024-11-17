from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('formulaire.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    nom = request.form.get('nom')
    email = request.form.get('email')

    with open('data.txt', 'a') as file:
        file.write(f"Nom: {nom}, Email: {email}\n")

    return "Données bien reçues et enregistrées !"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
