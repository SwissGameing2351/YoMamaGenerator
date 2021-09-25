# yo mama gen gui verison
import random
from zenipy import message
from zenipy.zenipy import warning

# "Yo Mama so" part (please put very good adjectives in YoMamaSo.txt)
with open("YoMamaSo.txt", "r") as file:
    allText = file.read()
    words = allText.split()
    random_word = random.choice(words) 

# the final joke part (please put very good jokes in She.txt)
with open("She.txt", 'r') as file: 
    lines = file.readlines() 
    random_line = random.choice(lines) 

warning(title=f'Yo Mama so {random_word}', text=f'She {random_line}', width=330, height=75, timeout=None)