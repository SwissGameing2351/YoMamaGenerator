# HELLO YO MAMER FANS !Like yo mama?make sure to like this viedo
import random
import time

# "Yo Mama so" part (please put very good adjectives in this textfile)
with open("YoMamaSo.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

# the final joke part (please put very good jokes in this textfile again)
with open("She.txt", 'r') as file: 
    lines = file.readlines() 
    random_line = random.choice(lines) 
        
# create the joke
print(f"Yo Mama so {random.choice(words)}")
time.sleep(3)
print(f"She {random_line}")