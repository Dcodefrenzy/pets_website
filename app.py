from flask import Flask
from helper import pets
app = Flask(__name__)

@app.route('/')
def index():
  return '''
        <h1>Adopt a Pet!</h1>
        <p>Browse through the links bellow to   find your new furry friend:</p>
        <ul>
          <li><a href='/animals/dogs'>Dogs</a></li>
          <li><a href='/animals/cats'>Cats</a></li>
          <li><a href='/animals/rabbits'>Rabbits</a></li>
        </ul>

         '''

@app.route('/animals/<pet_type>')
@app.route('/animals')
def animals(pet_type):
  html = f'<h1>List of {pet_type}</h1>'
  html += '<ul>'

  for count, pet in enumerate(pets[pet_type]):
    html += f'<li><a href="/animals/{pet_type}/{count}">{pet["name"]}</a></li>'

  html += '</ul>'
  html += '<a href="/"> Go back to Animals </a>'
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pid = abs(pet_id)
  pet = pets[pet_type][pet_id]
  return f'''
          <img src="{pet["url"]}" />
          <h1>{pet["name"]}</h1>
          <p>{pet["description"]}</p>
          <ul>
            <li>Breed: {pet["breed"]}</li>
            <li>Age: {pet['age']}</li>
          </ul>
          <a href="/animals/{pet_type}"> Go back to {pet_type} Page</a>
          '''

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000) 