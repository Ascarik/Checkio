def my_animal_generator():
 yield 'корова'
 for animal in ['кот', 'собака', 'медведь']:
  yield animal
 yield 'кит'
for animal in my_animal_generator():
 print(animal)