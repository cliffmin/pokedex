from flask import request
from flask import Flask, render_template
app = Flask(__name__)


class compareObject:
    def __init__(self, idNum):
        if(idNum == '007'):
            self.name = 'Squirtle'
            self.description = 'It shelters itself in its shell, then strikes back with spouts of water at every opportunity.'
            self.picture = "images/squirtle.png"
        elif(idNum == '025'):
            self.name = 'Pikachu'
            self.description = 'It raises its tail to check its surroundings. The tail is sometimes struck by lightning in this pose.'
            self.picture = "images/pikachu.gif"
        elif(idNum == '116'):
            self.name = 'Horsea'
            self.description = 'Known to shoot down flying bugs with precision blasts of ink from the surface of the water.'
            self.picture = "images/horsea.jpg" 

charizard = {'name': 'Charizard', 'number': '006', 'type': 'Fire/Flying', 'height': "5\' 7\" (1.70m)", 'weight': '199.5 lbs (90.5 kg)', 'picture': 'http://img.pokemondb.net/artwork/charizard.jpg'}
bulbasor = {'name': 'Bulbasor', 'number': '001', 'type': 'Grass/Poison', 'height': "2\' 4\" (0.71m)", 'weight': '15.2 lbs (6.9 kg)', 'picture': 'http://img.pokemondb.net/artwork/bulbasaur.jpg'}

poke_dict = {'1': bulbasor, '6': charizard}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search')
def search():    
    return render_template('search.html')

@app.route('/compare')
def compare():
    idOne = request.args.get('idOne','')
    idTwo = request.args.get('idTwo','')

    obj = compareObject(idOne)
    obj2 = compareObject(idTwo);
    return render_template('compare.html', obj = obj, obj2 = obj2)
    
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
