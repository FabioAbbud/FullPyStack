from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Parâmetros passados do python para o html
    params = {
        'title': 'Um dos sites que existe',
        'css': 'home.css',
        'js': 'home.js'
    }
    return render_template('home.html', params=params) # Primeiro params é uma variável criada quando o html for executado

@app.route('/contatos')
def contacts():
    params = {
        'title': 'Faça contato',
        'css': 'contacts.css',
        'js': 'contacts.js'
    }
    return render_template('contacts.html', params=params)

@app.route('/sobre')
def about():
    params = {
        'title': 'Sobre nós',
        'css': 'about.css',
        'js': 'about.js'
    }
    return render_template('about.html', params=params)

@app.route('/privacidade')
def policies():
    params = {
        'title': 'Políticas de privacidade',
        'css': 'policies.css',
        'js': 'policies.js'
    }
    return render_template('policies.html', params=params)

@app.errorhandler(404)
def not_found(e):
    params = {
        'title': 'Erro 404',
        'css': '404.css',
        'js': '404.js'
    }
    return render_template('404.html', params=params)




if __name__ == '__main__':
    app.run(debug=True)