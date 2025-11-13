from flask import Flask, render_template, request, redirect, url_for, flash
import requests
# Se eliminó la importación de 'json' ya que no se utiliza directamente. 

# 1. Inicialización de Flask
app = Flask(__name__)
# URL base de la PokeAPI
API = "https://pokeapi.co/api/v2/pokemon/"
# Clave secreta necesaria para usar 'flash' (mensajes temporales)
app.secret_key = "avenita"

# 2. Ruta principal (GET)
@app.route('/')
def index():
    """Muestra la página de inicio con el formulario de búsqueda."""
    return render_template('index.html')

# 3. Ruta de búsqueda (POST)
@app.route('/search', methods=['POST'])
def search_pokemon():
    """
    Procesa el formulario, busca el Pokémon en la PokeAPI y muestra la información.
    """
    # Obtiene el nombre/ID, lo limpia y lo convierte a minúsculas para la API
    pokemon_name = request.form.get('pokemon_name', '').lower().strip()

    if not pokemon_name:
        flash("Por favor, escribe el nombre o ID de un Pokémon.")
        # Se redirige a 'index' (la función), no a 'index.html'
        return redirect(url_for('index'))

    pokemon_data = None
    
    try:
        # Construcción correcta del URL de la API
        resp = requests.get(f"{API}{pokemon_name}")

        if resp.status_code == 200:
            # pokemon_data es ahora el diccionario completo de la API.
            pokemon_data = resp.json()
            
            # Reestructuramos la información para que sea fácil de consumir en la plantilla
            # y realizamos las conversiones de unidades aquí.
            pokemon_info =  {
                'name': pokemon_data['name'].title(),
                'id': pokemon_data['id'],
                # Conversión de decímetros a metros y hectogramos a kg
                'height': pokemon_data['height'] / 10,
                'weight': pokemon_data['weight'] / 10,
                'image': pokemon_data['sprites']['front_default'],
                # List comprehension para 'types'
                'types': [t['type']['name'].title() for t in pokemon_data['types']],
                'abilities': [a['ability']['name'].title() for a in pokemon_data['abilities']]
            }
        else:
            # Manejo de cualquier código de estado diferente a 200 (como 404, 500, etc.)
            error_code = resp.status_code
            flash(f"No se pudo encontrar el Pokémon '{pokemon_name.title()}'. La API devolvió el error: {error_code}")
            return redirect(url_for('index'))

    except resp.status_code == 500:
        flash(f"Ocurrió un error :c")
        return redirect(url_for('index'))

    # Si todo es exitoso, se renderiza la plantilla de resultados
    return render_template('Pokemon.html', pokemon=pokemon_info)

# 4. Inicialización de la aplicación
if __name__ == '__main__':
    # Ejecuta el servidor en modo debug
    app.run(debug=True)