# Exercicio 9.1 Curso intensivo de python

class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print("O nome do restaurante eh " + self.restaurant_name.title() + " e seu tipo de culinaria eh " + self.cuisine_type.title())

    def open_restaurant(self):
        print("O restaurante esta aberto.")

restaurant=Restaurant('mcdonalds','fast food')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()



