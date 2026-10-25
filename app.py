from flask import Flask

app = Flask(name)

@app.route('/')
def home():
    return "Bonjour ! Mon TP4 Cloud Computing fonctionne."

if name == 'main':
    app.run()
