from itertools import repeat
import horse
import hipodrome
from fitness_function import fitness_function


initial_population=horse.Horse.generate_population(10)
my_hipodrome=hipodrome.Hipodrome(8,7,3,2) 


roulet_wheel_list=[]

def parents(horse_fitness):
    for val_fitness in horse_fitness:
        if val_fitness >= 8:
             roulet_wheel_list.extend(repeat(val_fitness,100))
        elif val_fitness >= 6:
             roulet_wheel_list.extend(repeat(val_fitness,50))
        elif val_fitness >=3:
             roulet_wheel_list.extend(repeat(val_fitness,25))
        else:
            roulet_wheel_list.append(val_fitness)

    print(roulet_wheel_list)


list_fitness_function=fitness_function(initial_population,my_hipodrome)
parents(list_fitness_function)