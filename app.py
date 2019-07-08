from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servico-online')
def servicoOnline():
    return render_template('servico-online.html')

@app.route('/informativo')
def informativo():
    return render_template('informativo.html')

@app.route('/servico')
def servico():
    return render_template('servico.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run()
