"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

   """ read a list of words from a file and pick a random one to return """
import random
def generate_random_word():
    Words="angry hungry money school".split()
    return random.choice(Words)
print(generate_random_word())
  

def play_hangman():
   """ this is the python script version of the game """
   print("The hangman app is under construction. Try again later!")

if __name__ == '__main__':
    play_hangman()
