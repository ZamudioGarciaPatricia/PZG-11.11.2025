from flask import Flask, render_template,request,redirect,url_for,flash,jsonify

app = Flask(__name__)
API = "https://pokeapi.co//api/v2/pokemon/"
app.secret_key = "avenita"
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/search', methods={'POST'})
def search_pokemon():
    pokemon_name =request.form.get('pokemon_name', '').strip().strip
    
    if not pokemon_name:
        flash("por favor escribe el nombre de un pokemon")
        return redirect(url_for('index.html'))
    
resp = request.get(f"(API)pokemon_name")
pokemon_info={
    'name', pokemon_data('name')
}
nombre ide imagen tipo de pokemon

if __name__ == '__main__':
    app.run(debug=True)