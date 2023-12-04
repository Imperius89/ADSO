import os
import random

lista=["CSS","HTML","JAVASCRIPT","PHP","JAVA","PYTHON","GO","RUBY","C#","TYPESCRIPT","MYSQL","POSTGRES","ORACLE"]
palabra = random.choice(lista)
tamaño= len(palabra)
print(palabra,tamaño)

def play():

    Animacion = ["""
      +---+
      |   |
      o   |
     /|\  |
     / \  |
          |
    =========""", """
      +---+
      |   |
      o   |
     /|\  |
     /    |
          |
    =========""", """
      +---+
      |   |
      o   |
     /|\  |
          |
          |    
    =========""", """ 
      +---+
      |   |
      o   |
     /|   |
          |
          |
    =========""", """
      +---+
      |   |
      o   |
      |   |
          |
          |
    =========""", """
      +---+
      |   |
      o   |
          |
          |
          |
    =========""", """
      +---+
      |   |
          |
          |
          |
          |
    ========="""
    ]
    var = 0
    while (var <=7 ):
        os.system("cls")
        print (palabra,tamaño)
        print (Animacion[var])
        print ("oliwi")
        os.system("pause")
        var = var +1
if __name__ == "__main__":
        play()
