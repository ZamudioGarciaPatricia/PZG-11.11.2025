from flask import Flask, render_template,request,redirect,url_for,flash,jsonify
import requests 

app = Flask(__name__)
API = "https://pokeapi.co//api/v2/pokemon/"
app.secret_key = "avenita"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods={'POST'})
def search_pokemon():
    pokemon_name =request.form.get('pokemon_name', '')
    
    if not pokemon_name:
        flash("por favor escribe el nombre de un pokemon")
        return redirect(url_for('index.html'))
    
resp = request.get(f"(API)pokemon_name")
pokemon_info={'name', pokemon_data('name')
}
try:
    resp = requests.get(f"{API}(pokemon_name)")
    if resp.status_code == 200:
    pokemon_data = resp.json()
    
    pokemon_info =  {
        'name': pokemon_data ['name'].title(),
        'id': pokemon_data ['id'],
        'height': pokemon_data['height']/10,
        'weight': pokemon_data['weight']/10,
        'image': pokemon_data['sprites']['front_default']
        'types': [t['type']['name'].title]() for t a in pokemon_data['ability'],
        'stats': {}
        
    }
    
    return render_template('pokemon2.html', pokemon= pokemon_info)
if __name__ == '__main__':
    app.run(debug=True)