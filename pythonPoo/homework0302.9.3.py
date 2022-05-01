# Exercicio 9.3 Curso intensivo de python

class User():

    def __init__(self,first_name,last_name,idade,estado_civil,peso):
        self.first_name=first_name
        self.last_name=last_name
        self.idade=idade
        self.estado_civil=estado_civil
        self.peso=peso

    def describe_user(self):
        print("O nome desse usuario eh " + self.first_name.title() + " " + self.last_name.title() + " sua idade eh",self.idade,
              "anos, seu estado civil eh " + self.estado_civil + " e seu peso eh",self.peso,"kg.")

    def greet_user(self):
        print("Ola " + self.first_name.title() + " " + self.last_name.title() + ", eh um grande prazer te-lo conosco!")

user1=User('jorge','harbes',38,'divorciado',84)
user2=User('carolina','alcantara',27,'solteira',69)
user3=User('joao','das couves',23,'casado',90)

user1.describe_user()
user1.greet_user()
print("\n")
user2.describe_user()
user2.greet_user()
print("\n")
user3.describe_user()
user3.greet_user()