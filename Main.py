from animal_shelter import AnimalShelter
from bson.objectid import ObjectId

animals = AnimalShelter("aacuser", "aacuser")

#Valid document create
print(animals.create ({ 
 'age_upon_outcome': '2 years',
  'animal_id': 'A716330',
  'animal_type': 'Dog',
  'breed': 'Chihuahua Shorthair Mix',
  'color': 'Brown/White',
  'date_of_birth': '2013-11-18',
  'datetime': '2015-12-28 18:43:00',
  'monthyear': '2015-12-28T18:43:00',
  'name': 'Frank',
  'outcome_subtype': '',
  'outcome_type': 'Adoption',
  'sex_upon_outcome': 'Neutered Male',
  'location_lat': 30.7595748121648,
  'location_long': -97.5523753807133,
  'age_upon_outcome_in_weeks': 110.111408730159}))

#Invalid Document
print(animals.create({0:0}))

#Valid query
query = animals.read({"name": "Binx"})
for animal in query:
    print(animal)
    
#invalid query throws exception
print(list(animals.read({0:0})))
