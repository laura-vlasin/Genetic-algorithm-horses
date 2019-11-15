from itertools import repeat
import random
import statistics_module




def parents(horse_fitness, number_of_parents):
    
    roulet_wheel_list=[]
    parents_fitness_list=[]

    for val_fitness in horse_fitness:

        if val_fitness >= 8:
             roulet_wheel_list.extend(repeat(val_fitness,100))
        elif val_fitness >= 6:
             roulet_wheel_list.extend(repeat(val_fitness,50))
        elif val_fitness >=3:
             roulet_wheel_list.extend(repeat(val_fitness,25))
        else:
            roulet_wheel_list.append(val_fitness)

    while len(parents_fitness_list) < number_of_parents:
        fitness=random.choice(roulet_wheel_list)
        roulet_wheel_list.remove(fitness)
        if fitness not in parents_fitness_list:
            parents_fitness_list.append(fitness)
        
        
    return parents_fitness_list


list_fitness=statistics_module.list_fitness
my_horse_fitness=statistics_module.my_horse.fitness


parents(list_fitness,2)