import random
from hirsipuu_utils import get_logo,description , display_hangman


class HangmanGame:
    """
    Tämä luokka edustaa Hangman-peliä
    """
    
    def __init__(self, get_logo, word_list_filename, description):
        self.logo = get_logo()  # logo (str): Hangman-pelin logo, joka palautetaan get_logo-toiminnolla.
        self.word_list = self.load_word_list(word_list_filename)  # Luettelo sanoista, joista valita peliä varten.
        self.description = description()
        self.chosen_word = "" # The word to be guessed by the player.
        self.word_length = 0
        self.display = []
        self.end_of_game = False # (bool) "A flag" joka osoittaa, onko peli päättynyt.
        self.lives = 6
        self.guessed_letters = set()
        

    def load_word_list(self, filename):
        """
        Lataa sanaluettelon määritetystä tiedostosta, ottaa tiedostonimen (str) argumenttina ja palauttaa luettelon tiedostosta luetuista sanoista, poistaa etu- ja jälkimmäiset välilyönnit. Jos määritettyä tiedostoa ei löydy, palautetaan tyhjä lista.
        """
        
        try:
            with open(filename, "r") as file:
                return [line.strip() for line in file]
        except FileNotFoundError:
            return []

    def choose_word(self):
        self.chosen_word = random.choice(self.word_list)
        self.word_length = len(self.chosen_word)
        self.display = ["_" for _ in range(self.word_length)] # alustaa näyttöluettelon, jossa on alaviivoja paljastamattomille kirjaimille.

    def play(self):
        while True:  # Jatka pelaamista, kunnes pelaaja päättää olla pelaamatta uudelleen.
            self.choose_word()
            print(self.logo)
            print(self.description)
            
           # print(f'Pssst, ratkaisu on {self.chosen_word}.')

            while not self.end_of_game:
                
                guess = input("Syötä kirjain: ").lower()
                
                try:
                    if not guess.isalpha() or len(guess) != 1 :
                        raise ValueError("Syötä yksi suomen aakkosten kirjain:")
                except ValueError as e:
                    print(e)
                    
                    
                    continue  # Pyydä uutta arvausta

                    
                if guess in self.guessed_letters:
                    
                    print(f"Olet jo arvannut {guess}")
                    continue

                self.guessed_letters.add(guess)

                for position in range(self.word_length):
                    try:
                        letter = self.chosen_word[position]
                    except IndexError:
                        continue  # Käsittele indeksin rajojen ulkopuolella sulavasti
                    if letter == guess:
                        self.display[position] = letter

                if guess not in self.chosen_word:
                    print(f"kirjain {guess}, ei löytyy sanasta. Menetät elämän.")
                    self.lives -= 1
                    if self.lives == 0:
                        self.end_of_game = True
                        print("Valitettavasti olet hävinnyt.")

                print(" ".join(self.display))

                if "_" not in self.display:
                    self.end_of_game = True
                    print("Olet voittanut.")

                self.display_hangman()

            print(f'Sana oli: {self.chosen_word}.')
            play_again = input("Haluatko pelata uudestaan (joo/ei)? ").lower()
            while not (play_again == "joo" or play_again == "ei"):
                play_again = input("Vasta vain \"joo\" tai \"ei\": ").lower()
            if play_again == "ei":
                print("Kiitos pelista!")
                break   # Poistu silmukasta, jos pelaaja ei halua pelata uudelleen.
                

            # Nollaa pelin tila
            self.end_of_game = False
            self.lives = 6
            self.guessed_letters = set()
    

    def display_hangman(self):
        # Käytä tuotua display_hangman-funktiota
        print(display_hangman(self.lives))


def main():
    word_list_filename = "sanat.txt"
    game = HangmanGame(get_logo, word_list_filename, description)  # Käytä get_logo-toimintoa saadaksesi logon.
    game.play()

if __name__ == "__main__":
    main()