import os

def play():

    Animacion = ["""
      _   _    
    =========""", """
      _   _
      ^   ^
    =========""", """
      _   _
      ^   ^
     _  >  _
    =========""", """
      _   _
      ^   ^  
     _  >  _
      -----  
    ========="""
    ]

    var = 0
    while (var <=3 ):
        os.system("cls")
        print (Animacion[var])
        os.system("pause")
        var = var +1
if __name__ == "__main__":
        play()
