def get_logo():
    """
    funktio, joka palauttaa Hirsipuu ASCII ART logo 
    """
    logo ="""

  _    _ _          _                   
 | |  | (_)        (_)                  
 | |__| |_ _ __ ___ _ _ __  _   _ _   _ 
 |  __  | | '__/ __| | '_ \| | | | | | |
 | |  | | | |  \__ \ | |_) | |_| | |_| |
 |_|  |_|_|_|  |___/_| .__/ \__,_|\__,_|
                     | |                
                     |_|                

"""
    return logo
def description():
    sisälto="""
Tervetuloa 'Hirsipuun' peliin!

Pelin säännöt ovat yksinkertaiset.
Mina arvan sana ja ilmoitn sinulle montako kirjainta siinä on. 
Sinun täytyy arvata sen, nimet kirjaimia vuorottellen. 
Jos kirjain on minun sanassa, näytän sen sinulle.
Voit arvata väärin enintään 6 kertaa
    """

    return sisälto





def display_hangman(lives):
    """
    retuns a display of hirsipuu from the list stages depending on how many attempts left
    the function takes an int lives as argument and it is the index of the list item
    """
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

    return stages[lives]