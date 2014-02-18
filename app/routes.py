from flask import Flask, render_template
app = Flask(__name__)

charizard = {'name': 'Charizard', 'number': '006', 'type': 'Fire/Flying', 'height': "5\' 7\" (1.70m)", 'weight': '199.5 lbs (90.5 kg)', 'picture': 'http://img.pokemondb.net/artwork/charizard.jpg'}
bulbasor = {'name': 'Bulbasor', 'number': '001', 'type': 'Grass/Poison', 'height': "2\' 4\" (0.71m)", 'weight': '15.2 lbs (6.9 kg)', 'picture': 'http://img.pokemondb.net/artwork/bulbasaur.jpg'}

poke_dict = {'1': bulbasor, '6': charizard}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search')
def search():    
    return render_template('search.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/view/<id>')
def view_poke(id=None):
    if(id == '6'):
    	return render_template('view.html', id=poke_dict['6'])
    elif(id == '1'):
    	return render_template('view.html', id=poke_dict['1'])
    else:
    	return render_template('view.html', id=None)

if __name__ == '__main__':
    app.run(debug=True)