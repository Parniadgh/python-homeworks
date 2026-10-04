

import random

characters=["a","b","c","d","e","f","g","h","i","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","@","#","&"]
password= random.choices(population=characters , k=18)
print(password)
