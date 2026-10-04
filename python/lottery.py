

import random

participants=["parnia","kimia","arman","arsham"]

chances=[100,1,1,1]

winner= random.choices(population=participants,weights=chances,k=1)
print(winner)
