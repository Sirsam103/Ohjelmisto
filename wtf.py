import random
import math
for _ in range(90):
    alpha = random.randint(1, 90)
    g = 9.81
    s = random.randint(1, 100)
    m = random.randint(20, 200)
    a = g * math.sin(math.radians(alpha))

    #print(alpha)
    #print(math.sin(math.radians(alpha)))
    print(f'{m} * {a} * {s} = {m*a*s}')
    print(f'1/2 * {m} * ({a} * sqrt((2 * {s}) / ({a})))^2 = {1/2*m*(a*math.sqrt((2*s)/(a)))**2}\n\n')
