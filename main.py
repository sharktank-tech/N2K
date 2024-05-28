from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template ('homepage.html')

@app.route('/catalogo')
def catalogo():
    return render_template ('catalogo.html')

@app.route('/sobre')
def about():
    return render_template ('sobre.html')

@app.route('/politica-de-privacidade')
def contact():
    return render_template ('politica_privacidade.html')
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
